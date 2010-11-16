import sys
from Entity import Group, User, TreeObject, ActionRestrict
from PyQt4 import QtGui, QtCore
from GroupWindowUI import Ui_GroupEdit
import string
from actions import actions

class GroupWindow(QtGui.QDialog, Ui_GroupEdit):
    addlist = []
    rmlist = []
    
    def __init__(self, dbhandler, group, pgroup=None, parent=None):
        QtGui.QDialog.__init__(self,parent)        
        self.setupUi(self)       
        self.dbhandler = dbhandler
        self.group = None
        self.pgroup = None
        
        if group != None:
            self.group = dbhandler.session.query(Group).filter_by(name=group.__str__()).first()        
        
        if pgroup != None:
            self.pgroup = dbhandler.session.query(Group).filter_by(name=pgroup.__str__()).first()
        
        self.lstUsrIn.clear()
        self.lstUsrAvail.clear()
        
        if self.group != None:
            self.txtGroupName.setText(self.group.name)
            
            for u in self.group.users:
                self.lstUsrIn.addItem(u.login)
                
            for u in self.dbhandler.getUsersNotInGroup(self.group):
                self.lstUsrAvail.addItem(u.login)
        else:            
            self.group = Group("")
            
            for u in self.dbhandler.session.query(User):
                self.lstUsrAvail.addItem(u.login)
    
    def add_to_group(self):
        toAdd = self.lstUsrAvail.selectedItems()
        for item in toAdd:
            try :
                self.rmlist.remove(item.text().__str__())
            except ValueError:                
                self.addlist.append(item.text().__str__())
            
            self.lstUsrIn.addItem(item.text())
            self.lstUsrAvail.takeItem(self.lstUsrAvail.row(item))
        
    
    def remove_from_group(self):
        toRm = self.lstUsrIn.selectedItems()
        for item in toRm:
            try: 
                self.addlist.remove(item.text().__str__())
            except ValueError:                
                self.rmlist.append(item.text().__str__())
            
            self.lstUsrAvail.addItem(item.text())
            self.lstUsrIn.takeItem(self.lstUsrIn.row(item))
        
    
    def closeEvent(self, event):
        self.parent().update_data()
        event.accept()
    
    def accept(self):
        for item in self.rmlist:
            self.group.users.remove(self.dbhandler.session.query(User).filter_by(login=item).first())
        
        for item in self.addlist:
            self.group.users.append(self.dbhandler.session.query(User).filter_by(login=item).first())    
        
        if self.txtGroupName.text() == "":
            return
        
        self.group.name = self.txtGroupName.text().__str__()
        
        if self.pgroup != None:
            self.group.parent = self.pgroup
            
        if self.group.base_dir == None:
            base_dir = TreeObject(self.group.name
                                  , TreeObject.TYPE_COLLECTION
                                  , {True: self.pgroup.base_dir, False: None}[self.pgroup != None]
                                  , self.dbhandler.getCurrentUser().id
                                  , None
                                  , 0
                                  , None
                                  , string.join([{True: self.pgroup.base_dir.path, False: ''}[self.pgroup != None],self.group.name,''], '/')
                        )
            self.group.base_dir = base_dir
        
        self.dbhandler.session.add(self.group)
        self.dbhandler.session.commit()
        
        self.dbhandler.session.add(ActionRestrict(self.dbhandler.getCurrentUser().id, 1, self.group.base_dir.id, actions['ALL']))
        self.dbhandler.session.commit()
        self.close()
    
    def reject(self):
        self.close()