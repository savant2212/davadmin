from Ui_AuthDialog import Ui_AuthDialog
from PyQt4 import QtCore, QtGui
from Entity import User, ActionRestrict
from actions import actions, user_root_acts

    
class AuthWindow(QtGui.QDialog, Ui_AuthDialog):
    def __init__(self, dbhandler, user=None, parent=None):
        QtGui.QDialog.__init__(self,parent)        
        self.setupUi(self)       
        self.dbhandler = dbhandler
        
        
    def accept(self):
        user = self.dbhandler.Authenticate(self.txtLogin.text().__str__(),self.txtPassword.text().__str__())
        if user == None:
            msgBox = QtGui.MessageBox()
            msgBox.setText("Login or password are invalid")
            msgBox.show()            
        else:
            self.close()
        pass
    
    def reject(self):
        self.parent.close()
        pass
    
    
    def closeEvent(self, event):        
        event.accept()
        pass