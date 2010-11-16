'''
Created on 07.11.2010

@author: savant
'''
import sys
from Entity import Group, User
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
                        if r.action & actions[self.tblUserRestriction.horizontalHeaderItem(i).text().__str__()] != 0 :
                            item = QtGui.QTableWidgetItem()
                            item.setCheckState(2)
                            item.setFlags(table_flags)
                            self.tblUserRestriction.setItem(self.tblUserRestriction.rowCount()-1,i,item)                           
                    
    def tblUserRestriction_itemChanged(self, item):
        action = self.tblUserRestriction.horizontalHeaderItem(item.row()).text().__str__()
        login =  self.tblUserRestriction.item(item.row(),0).text().__str__()             
        
        user = self.dbhandler.session.query(User).filter_by(login==login)
        
        restr = user.getRestrictions(self.group, self.dbhandler.session).first()
        
        if item.checkState() == QtCore.Qt.Unchecked:
            restr.action = restr.action & ~actions[action]
        else:
            restr.action = restr.action | actions[action]
            
        self.dbhandler.session.add(restr)
        
        pass      
    
    def closeEvent(self, event):
        self.parent().update_data()
        event.accept()
        
    def accept(self):
        self.dbhandler.session.commit()
        self.close()
    
    def reject(self):
        self.close()