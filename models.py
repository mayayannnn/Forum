from peewee import *
from flask import Flask

db = SqliteDatabase('forum.db')

class BaseModel(Model):
    class Meta:
        database = db

class Thread(BaseModel):
    title = CharField(max_length=200)
    created_at = DateTimeField()
    post_count = IntegerField(default=0)

class Post(BaseModel):
    thread = ForeignKeyField(Thread, backref='posts', on_delete='CASCADE')
    content = TextField()
    name = CharField(max_length=100)
    created_at = DateTimeField()

def init_app(app):
    """Flaskアプリケーションにデータベースを初期化"""
    db.init('forum.db')
