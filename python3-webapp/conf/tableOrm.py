from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Time,Boolean, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationships
from sqlalchemy import create_engine
import time, uuid

Base = declarative_base()

class User(Base):
    __table__ = 't_user'

    id = Column(Integer,primary_key=True)
    email = Column(String)
    passwd = Column(String)
    admin = Column(Boolean)
    name = Column(String)
    image = Column(String)
    create_at = Column(Time,default=time.time)

class Blog(Base):
    __table__ = 't_blogs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    user_name = Column(String)
    user_image = Column(String)
    name = Column(String)
    content = Column(String)
    create_at = Column(Time,default=time.time)

class Comment(Base):
    __table__ = 't_comments'

    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer)
    user_id = Column(Integer)
    user_name = Column(String)
    user_image = Column(String)
    content = Column(String)
    create_at = Column(Time, default=time.time)

settings = {
        'echo': True,
        'echo_pool': True,
        'encoding': 'utf-8',
        'pool_size': 128,
        'strategy': 'threadlocal'
    }
url = "mysql+pymysql://root:powerpeak@localhost/SQLAlchemySample"
engine = create_engine(url, **settings)
engine = create_engine()
session = sessionmaker()
session.configure(bind=engine)
