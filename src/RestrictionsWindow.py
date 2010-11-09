'''
Created on 07.11.2010

@author: savant
'''
import sys
from Entity import Group
from PyQt4 import QtGui, QtCore
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
        self.setupUi(self)       
        self.dbhandler = dbhandler       
        
        
        self.tblUserRestriction.insertColumn(self.tblUserRestriction.columnCount())
        self.tblUserRestriction.setHorizontalHeaderItem(self.tblUserRestriction.columnCount()-1,QtGui.QTableWidgetItem("Login") )
        
        for r in actions:
            self.tblUserRestriction.insertColumn(self.tblUserRestriction.columnCount())
            self.tblUserRestriction.setHorizontalHeaderItem(self.tblUserRestriction.columnCount()-1,QtGui.QTableWidgetItem(r) )
            
        if group != None:
            self.group = dbhandler.session.query(Group).filter_by(name=group.__str__()).first()
            self.txtGroupName = self.group.name
            
            for u in self.group.users:
                self.tblUserRestriction.insertRow(self.tblUserRestriction.rowCount())