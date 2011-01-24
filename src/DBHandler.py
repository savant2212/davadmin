import sys
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker, relationship
import hashlib

from sqlalchemy.sql.expression import desc, join
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
        m = hashlib.sha256()
        m.update(pw) 
        user = self.session.query(User).filter_by(login=user,password=m.hexdigest()).first()
        
        if user != None:
#            restrict = self.session.query(ActionRestrict).filter_by(actor_id=user.id, object_id=1, actor_type='1').first()
#            
#            if restrict.action & actions['ADMIN'] != 0:
#                self.currentUser = user
                self.currentUser = user
        else:        
            self.currentUser = None
    
    def getUsers(self):
        return self.session.query(User).filter_by(is_deleted=False)
    
    def getCurrentUser(self):
        return self.currentUser
        #return self.session.query(User).filter_by(id=1, is_deleted=False).first()
    
    def getGroups(self):
        return self.session.query(Group).filter_by(parent_id=None)
    
    def getUsersNotInGroup(self, group):        
        rs = self.session.query(User).from_statement("select * from \"Users\" left join \"UserGroups\" on \"Users\".id = \"UserGroups\".user_id where \"Users\".id not in (select user_id from \"UserGroups\" where group_id=:gid)").params(gid=group.id).all()        
        return rs   
    
#    def getUserRootGroup(self, user):
#        list = []
#        
#        rs = self.session.query(ActionRestrict).filter_by(actor_id=user.id, actor_type=1, object_type=2)
#        for r in rs:
#            if r.action & actions["ADMIN"] == 0:
#                continue 
#            
#            group = self.session.query(Group).filter_by(id=r.object_id).first()
#            
#            if group.parent == None:
#                for id in list:
#                     if id == group.id:
#                         append
#                pass
#            else:
#                pass
#        pass
        