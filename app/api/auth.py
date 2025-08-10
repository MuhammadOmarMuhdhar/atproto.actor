from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional
import jwt

from app.database import get_db
from app.models.user import User
from app.models.subscription import Subscription
from app.core.atprotoClient import atproto_client
from app.config import settings

router = APIRouter()
security = HTTPBearer()


class LoginRequest(BaseModel):
    handle: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict


class UserResponse(BaseModel):
    id: int
    atproto_handle: str
    atproto_did: str
    display_name: Optional[str]
    avatar_url: Optional[str]
    bio: Optional[str]
    is_premium: bool


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    try:
        # Authenticate with ATProto
        auth_data = await atproto_client.authenticate(request.handle, request.password)
        
        # Check if user exists in our database
        user = db.query(User).filter(User.atproto_did == auth_data['did']).first()
        
        if not user:
            # Create new user
            user = User(
                atproto_handle=auth_data['handle'],
                atproto_did=auth_data['did'],
                display_name=auth_data['display_name'],
                avatar_url=auth_data['avatar'],
                last_login=datetime.utcnow()
            )
            db.add(user)
            
            # Create free subscription
            subscription = Subscription(
                user_id=user.id,
                plan_type="free",
                max_sites=1,
                max_custom_domains=0
            )
            db.add(subscription)
            db.commit()
            db.refresh(user)
        else:
            # Update existing user
            user.display_name = auth_data['display_name']
            user.avatar_url = auth_data['avatar']
            user.last_login = datetime.utcnow()
            db.commit()
        
        # Generate JWT token
        token_data = {
            "sub": str(user.id),
            "did": user.atproto_did,
            "handle": user.atproto_handle,
            "exp": datetime.utcnow() + timedelta(days=7)
        }
        access_token = jwt.encode(token_data, settings.SECRET_KEY, algorithm="HS256")
        
        return LoginResponse(
            access_token=access_token,
            user={
                "id": user.id,
                "atproto_handle": user.atproto_handle,
                "atproto_did": user.atproto_did,
                "display_name": user.display_name,
                "avatar_url": user.avatar_url,
                "bio": user.bio,
                "is_premium": user.is_premium
            }
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication failed: {str(e)}"
        )


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    try:
        token = credentials.credentials
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = int(payload.get("sub"))
        
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        
        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return UserResponse(
        id=current_user.id,
        atproto_handle=current_user.atproto_handle,
        atproto_did=current_user.atproto_did,
        display_name=current_user.display_name,
        avatar_url=current_user.avatar_url,
        bio=current_user.bio,
        is_premium=current_user.is_premium
    )


@router.post("/logout")
async def logout(current_user: User = Depends(get_current_user)):
    return {"message": "Logged out successfully"}