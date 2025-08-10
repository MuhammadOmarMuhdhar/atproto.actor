from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    category = Column(String)
    
    preview_image_url = Column(String)
    demo_url = Column(String)
    
    is_active = Column(Boolean, default=True)
    is_premium = Column(Boolean, default=False)
    
    html_template = Column(Text, nullable=False)
    css_template = Column(Text)
    js_template = Column(Text)
    
    config_schema = Column(JSON)
    default_config = Column(JSON)
    
    usage_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    sites = relationship("Site", back_populates="template")