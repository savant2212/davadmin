#!/usr/bin/python2
# simple.py

import sys
from PyQt4 import QtGui, QtCore
from MainWindow import Ui_MainWindow
from Ui_AuthWindow import Ui_AuthDialog
import os
from DBHandler import DBHandler
from UserWindow import UserWindow

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None ):
        QtGui.QWidget.__init__(self, parent)        
        self.setupUi(self)  
        
        self.connection_string="sqlite:///%s/../../davstorage/db/devel.db" % (os.getcwd())
        self.dbhandler = DBHandler(self.connection_string)
        
        users = self.dbhandler.getUsers()
        
        self.items=[]
        for u in users:
            self.items.append(u.login)
            
        lm = MyListModel(self.items, self)
        self.lstUsers.setModel(lm)
        
    def add_user(self):
        widget = UserWindow(self.dbhandler,parent=self)
        widget.show()
        
    def delete_user(self):
        pass
    def edit_user(self):
        
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