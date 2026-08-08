from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.models import PostStatus

class PostBase(BaseModel):
    title: str = Field(..., min_length=20, description="Minimal 20 karakter")
    content: str = Field(..., min_length=200, description="Minimal 200 karakter")
    category: str = Field(..., min_length=3, description="Minimal 3 karakter")
    status: PostStatus

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=20)
    content: Optional[str] = Field(None, min_length=200)
    category: Optional[str] = Field(None, min_length=3)
    status: Optional[PostStatus] = None

class PostResponse(PostBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True

class SuccessResponse(BaseModel):
    message: str
    data: Optional[PostResponse] = None