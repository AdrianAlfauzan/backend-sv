from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base
import enum

class PostStatus(str, enum.Enum):
    PUBLISH = "Publish"
    DRAFT = "Draft"
    THRASH = "Thrash"

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Title = Column("Title", String(200), nullable=False)
    Content = Column("Content", Text, nullable=False)
    Category = Column("Category", String(100), nullable=False)
    Status = Column("Status", String(100), default=PostStatus.DRAFT.value, nullable=False)
    Created_date = Column("Created_date", DateTime, server_default=func.now(), nullable=False)
    Updated_date = Column("Updated_date", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)