from PyQt4 import QtCore, QtGui
from Entity import User, ActionRestrict
from actions import actions, user_root_acts
from Ui_AuthWindow import Ui_AuthDialog

    
class AuthWindow(QtGui.QDialog, Ui_AuthDialog):
    def __init__(self, dbhandler, parent=None):
        QtGui.QDialog.__init__(self,parent)        
        self.setupUi(self)       
        self.dbhandler = dbhandler
        
        
    def accept(self):
        self.dbhandler.Authenticate(self.txtLogin.text().__str__(),self.txtPassword.text().__str__())
        if self.dbhandler.getCurrentUser() == None:
            msgBox = QtGui.QMessageBox.critical(self, 'Authentication error',
            "Login or password are invalid")
        else:
            self.close()
        pass
    
    def reject(self):
        self.parent.close()
        pass
    
    
    def closeEvent(self, event):        
        event.accept()
        pass