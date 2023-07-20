from peewee import Model, CharField, DateTimeField
from datetime import datetime
from .database import database


class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        database = database
        table_name = 'movies'
