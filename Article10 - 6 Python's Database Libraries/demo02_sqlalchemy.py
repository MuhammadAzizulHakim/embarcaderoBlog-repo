# Version Check
import sqlalchemy
 
print(sqlalchemy.__version__)
 
# Connecting
from sqlalchemy import create_engine
 
engine = create_engine('sqlite:///:memory:', echo=True)
 
# Declare a Mapping
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
 
 
from sqlalchemy import Column, Integer, String
 
class User(Base):
    __tablename__ = 'users'
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
 
    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)
 
# Create a Schema
print(User.__table__)
print(User.__tablename__)
print(User.id)
print(User.name)
print(User.fullname)
print(User.nickname)
print(User.__repr__)
 
Base.metadata.create_all(engine)