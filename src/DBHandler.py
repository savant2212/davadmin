import sys
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker, relationship

from sqlalchemy.sql.expression import desc
import time
from Entity import *
from actions import actions


Base = declarative_base()

class DBHandler(object):
    def __init__(self, connection_string):
        self.metadata = Base.metadata
        self.engine = create_engine(connection_string, echo=True)
                
        self.SessionMK = sessionmaker(bind=self.engine)
        self.session = self.SessionMK()
        
    def Authenticate(self,user,pw):
        user = self.session.query(User).filter_by(login=user,password=pw).first()
        restrict = self.session.query(ActionRestrict).filter_by(actor_id=user.id, object_id=1, actor_type='1').first()
        
        if restrict.action & actions['ADMIN'] != 0:
            return user
        
        return None
    
    def getUsers(self):
        return self.session.query(User)
    
    def getGroups(self):
        return self.session.query(Group).filter_by(parent_id=None)