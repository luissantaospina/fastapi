from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserReview(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = Column(String(500), nullable=False)
    score = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
