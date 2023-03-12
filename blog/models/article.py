from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime
from sqlalchemy.orm import relationship

from blog.models.database import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    title = Column(String(255))
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship("Author", back_populates="article")
