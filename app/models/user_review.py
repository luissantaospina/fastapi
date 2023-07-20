from peewee import Model, ForeignKeyField, DateTimeField, TextField, IntegerField
from datetime import datetime
from .database import database
from .movie import Movie
from .user import User


class UserReview(Model):
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

    class Meta:
        database = database
        table_name = 'user_reviews'
