'''
Created on 07.11.2010

@author: savant
'''
import sys
from Entity import Group, User, ActionRestrict
from PyQt4 import QtGui, QtCore, Qt
from RestrictionsUI import Ui_Restrictions
from actions import actions

class RestrictionsWindow(QtGui.QDialog, Ui_Restrictions ):
    '''
    classdocs
    '''
       
    def __init__(self, dbhandler, group, parent=None):
        '''
        Constructor
        '''       
        QtGui.QDialog.__init__(self,parent)
        
        if group == None:
            self.close()
                    
        self.setupUi(self)       
        self.dbhandler = dbhandler       
        
        table_flags = QtCore.Qt.ItemFlags(49)
        
        self.tblUserRestriction.insertColumn(self.tblUserRestriction.columnCount())
        self.tblUserRestriction.setHorizontalHeaderItem(self.tblUserRestriction.columnCount()-1,QtGui.QTableWidgetItem("Login") )
        
        for r in actions:
            self.tblUserRestriction.insertColumn(self.tblUserRestriction.columnCount())
            self.tblUserRestriction.setHorizontalHeaderItem(self.tblUserRestriction.columnCount()-1,QtGui.QTableWidgetItem(r) )
            
        if group != None:
            self.group = dbhandler.session.query(Group).filter_by(name=group.__str__()).first()
            self.txtGroupName.setText(self.group.name)
                        
            for u in self.group.users:
                item = QtGui.QTableWidgetItem(u.login)
                item.setFlags(table_flags)
                self.tblUserRestriction.insertRow(self.tblUserRestriction.rowCount())
                self.tblUserRestriction.setItem(self.tblUserRestriction.rowCount()-1,0,item)
                restrictions = u.getRestrictions(self.group,dbhandler.session)                
                for r in restrictions:
                    for i in xrange(1,self.tblUserRestriction.columnCount()):
                        item = QtGui.QTableWidgetItem()
                        act = actions[self.tblUserRestriction.horizontalHeaderItem(i).text().__str__()]
                        if r.action & act == act :                            
                            item.setCheckState(2)
                        else:
                            item.setCheckState(0)
                            
                        item.setFlags(table_flags)
                        self.tblUserRestriction.setItem(self.tblUserRestriction.rowCount()-1,i,item)                           
                    
    def tblUserRestriction_itemChanged(self, item):
        if item.column() == 0:
            return
        
        action = self.tblUserRestriction.horizontalHeaderItem(item.column()).text().__str__()
        login =  self.tblUserRestriction.item(item.row(),0).text().__str__()             
        
        
        
        user = self.dbhandler.session.query(User).filter_by(login=login).first()
        
        restr = user.getRestrictions(self.group, self.dbhandler.session).first()
        
        if restr == None:
            restr = ActionRestrict(user.id, 1, self.group.id, 0, 2)
            pass
        
        if item.checkState() == QtCore.Qt.Unchecked:
            restr.action = restr.action & ~actions[action]
        else:
            restr.action = restr.action | actions[action]
            
        self.dbhandler.session.add(restr)
        self.dbhandler.session.commit()
        pass      
    
    def closeEvent(self, event):
        self.parent().update_data()
        event.accept()
        
    def accept(self):
        self.dbhandler.session.commit()
        self.close()
    
    def reject(self):
        self.close()