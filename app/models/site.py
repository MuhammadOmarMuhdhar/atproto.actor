from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Site(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    subdomain = Column(String, unique=True, index=True, nullable=False)
    custom_domain = Column(String, unique=True, index=True)
    template_id = Column(Integer, ForeignKey("templates.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    is_published = Column(Boolean, default=False)
    is_custom_domain_verified = Column(Boolean, default=False)
    
    content_config = Column(JSON)
    style_config = Column(JSON)
    seo_config = Column(JSON)
    
    last_generated_at = Column(DateTime(timezone=True))
    last_synced_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    owner = relationship("User", back_populates="sites")
    template = relationship("Template", back_populates="sites")