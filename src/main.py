#!/usr/bin/python2
# simple.py

import sys
from PyQt4 import QtGui, QtCore
from MainWindow import Ui_MainWindow
from Ui_AuthWindow import Ui_AuthDialog
import os
from DBHandler import DBHandler
from UserWindow import UserWindow
from Entity import Group, User
from GroupWindow import GroupWindow
from RestrictionsWindow import RestrictionsWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    currentUser = None
    currentGroup = None
    def __init__(self, parent=None ):
        QtGui.QMainWindow.__init__(self, parent)        
        self.setupUi(self)  
        
        self.connection_string="sqlite:///%s/../../davstorage/db/devel.db" % (os.getcwd())
        self.dbhandler = DBHandler(self.connection_string)
        self.update_data()
        
    def event(self, event):
        if event == QtCore.QEvent.Close:
            self.update_data()
            
        return super(MainWindow, self).event(event)
       
    def add_user(self):
        widget = UserWindow(self.dbhandler,parent=self)
        widget.show()
        
    def delete_user(self):
        user = self.dbhandler.session.query(User).filter_by(login=self.currentUser.__str__()).first()
        user.is_deleted=True
        self.dbhandler.session.add(user)
        self.dbhandler.session.commit()
        self.update_data() 
        
    def edit_user(self):  
        widget = UserWindow(self.dbhandler,self.currentUser,parent=self)
        widget.show()      
        pass
    
    def add_group(self):
        widget = GroupWindow(self.dbhandler,None,parent=self)
        widget.show()
        pass
    def edit_group(self):
        widget = GroupWindow(self.dbhandler,self.currentGroup,parent=self)
        widget.show()
        pass
    
    def delete_group(self):
        user = self.dbhandler.session.query(Group).filter_by(name=self.currentGroup.__str__()).first()
        user.is_deleted=True
        self.dbhandler.session.add(user)
        self.dbhandler.session.commit()
        self.update_data()
        
    def tab_changed(self, widget):
        self.update_data()
        pass
    def restr_group(self):
        widget = RestrictionsWindow(self.dbhandler,self.currentGroup,parent=self)
        widget.show()
        pass
    
    def update_data(self):
        users = self.dbhandler.getUsers()
        self.lstUsers.clear()
        for u in users:
            self.lstUsers.addItem(QtGui.QListWidgetItem(u.login))                
        
        self.treeGroups.clear()
        for group in self.dbhandler.getGroups():                
            item=QtGui.QTreeWidgetItem([group.name])
            item.addChildren(self.get_groupWidgetTree(group))
            #item = self.get_groupWidgetTree(group)                
            self.treeGroups.addTopLevelItem(item)
        
    def get_groupWidgetTree(self, group):
        lst = []
        for g in group.subgroups:
            gi = QtGui.QTreeWidgetItem([g.name])
            gi.addChildren(self.get_groupWidgetTree(g))
            lst.append(gi)
        
        return lst
    def groupItemChanged(self, item):
        self.currentGroup = item.text(0)
        pass
    
    def userItemChanged(self, item):
        self.currentUser = item.text()
        pass
    
    
class MyListModel(QtCore.QAbstractListModel):
    def __init__(self, datain, parent=None, *args):
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.listdata = datain

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.listdata)

    def data(self, index, role):
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.listdata[index.row()])
        else:
            return QtCore.QVariant()
    
class AuthWindow(QtGui.QDialog, Ui_AuthDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)        
        self.setupUi(self)  
    def accept(self):
        pass
    def reject(self):
        pass
    
app = QtGui.QApplication(sys.argv)

widget = MainWindow()
widget.show()

sys.exit(app.exec_())