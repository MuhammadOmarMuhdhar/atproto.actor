import asyncio
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta
import logging

from atproto import AsyncClient, Client
from atproto.exceptions import AtProtocolError

logger = logging.getLogger(__name__)


class ATProtoClient:
    def __init__(self):
        self.client = AsyncClient()
        self.session_cache = {}
        
    async def authenticate(self, handle: str, password: str) -> Dict[str, Any]:
        """Authenticate with ATProto and return session info"""
        try:
            profile = await self.client.login(handle, password)
            session_data = {
                'did': profile.did,
                'handle': profile.handle,
                'display_name': profile.display_name,
                'avatar': profile.avatar,
                'authenticated_at': datetime.utcnow()
            }
            self.session_cache[profile.did] = session_data
            return session_data
        except AtProtocolError as e:
            logger.error(f"ATProto authentication failed: {e}")
            raise
            
    async def get_user_profile(self, identifier: str) -> Dict[str, Any]:
        """Get user profile by DID or handle"""
        try:
            profile = await self.client.app.bsky.actor.get_profile({'actor': identifier})
            
            return {
                'did': profile.did,
                'handle': profile.handle,
                'display_name': profile.display_name or profile.handle,
                'description': profile.description or '',
                'avatar': profile.avatar,
                'banner': profile.banner,
                'followers_count': profile.followers_count or 0,
                'follows_count': profile.follows_count or 0,
                'posts_count': profile.posts_count or 0,
                'created_at': getattr(profile, 'created_at', None),
                'verified': getattr(profile, 'verified', False)
            }
        except AtProtocolError as e:
            logger.error(f"Failed to fetch profile for {identifier}: {e}")
            return None
            
    async def get_user_posts(self, identifier: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent posts for a user"""
        try:
            feed = await self.client.app.bsky.feed.get_author_feed({
                'actor': identifier,
                'limit': limit
            })
            
            posts = []
            for item in feed.feed:
                post = item.post
                posts.append({
                    'uri': post.uri,
                    'cid': post.cid,
                    'text': post.record.text,
                    'created_at': post.record.created_at,
                    'reply_count': post.reply_count or 0,
                    'repost_count': post.repost_count or 0,
                    'like_count': post.like_count or 0,
                    'embed': self._format_embed(post.embed) if post.embed else None
                })
            
            return posts
        except AtProtocolError as e:
            logger.error(f"Failed to fetch posts for {identifier}: {e}")
            return []
            
    async def get_social_stats(self, identifier: str) -> Dict[str, int]:
        """Get follower and following counts"""
        try:
            profile = await self.client.app.bsky.actor.get_profile({'actor': identifier})
            return {
                'followers': profile.followers_count or 0,
                'following': profile.follows_count or 0,
                'posts': profile.posts_count or 0
            }
        except AtProtocolError as e:
            logger.error(f"Failed to fetch social stats for {identifier}: {e}")
            return {'followers': 0, 'following': 0, 'posts': 0}
            
    def _format_embed(self, embed) -> Optional[Dict[str, Any]]:
        """Format embed data for landing page use"""
        if not embed:
            return None
            
        embed_data = {}
        
        if hasattr(embed, 'images') and embed.images:
            embed_data['type'] = 'images'
            embed_data['images'] = [
                {
                    'url': img.fullsize,
                    'alt': img.alt,
                    'thumb': img.thumb
                } for img in embed.images
            ]
        elif hasattr(embed, 'external') and embed.external:
            embed_data['type'] = 'external'
            embed_data['external'] = {
                'uri': embed.external.uri,
                'title': embed.external.title,
                'description': embed.external.description,
                'thumb': embed.external.thumb
            }
            
        return embed_data if embed_data else None
        
    async def format_profile_for_landing(self, identifier: str) -> Dict[str, Any]:
        """Get formatted profile data optimized for landing pages"""
        profile = await self.get_user_profile(identifier)
        if not profile:
            return None
            
        posts = await self.get_user_posts(identifier, limit=5)
        
        return {
            'profile': profile,
            'recent_posts': posts,
            'social_proof': {
                'total_engagement': sum(p['like_count'] + p['repost_count'] for p in posts),
                'avg_engagement': sum(p['like_count'] + p['repost_count'] for p in posts) / max(len(posts), 1)
            },
            'last_updated': datetime.utcnow().isoformat()
        }
        
    async def validate_handle(self, handle: str) -> bool:
        """Check if a handle exists and is valid"""
        try:
            profile = await self.get_user_profile(handle)
            return profile is not None
        except:
            return False


# Singleton instance
atproto_client = ATProtoClient()