import sys
from Entity import Group
from PyQt4 import QtGui, QtCore
from GroupWindowUI import Ui_GroupEdit

class GroupWindow(QtGui.QDialog, Ui_GroupEdit):
    def __init__(self, dbhandler, group, parent=None):
        QtGui.QDialog.__init__(self,parent)        
        self.setupUi(self)       
        self.dbhandler = dbhandler
        self.group = dbhandler.session.query(Group).filter_by(name=group.__str__()).first()
        
        self.lstUsrIn.clear()
        self.lstUsrAvail.clear()
        
        if self.group != None:
            self.txtGroupName.setText(self.group.name)
            
            for u in self.group.users:
                self.lstUsrIn.addItem(u.login)
                
            for u in self.dbhandler.getUsersNotInGroup(self.group):
                self.lstUsrAvail.addItem(u.login)
    
    def add_to_group(self):
        pass
    
    def remove_from_group(self):
        pass
    
    def closeEvent(self, event):
        self.parent().update_data()
        event.accept()
    
    def reject(self):
        self.close()