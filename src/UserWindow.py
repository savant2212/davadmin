from UserUI import Ui_User
from PyQt4 import QtCore, QtGui
from Entity import User, ActionRestrict
from actions import actions, user_root_acts

    
class UserWindow(QtGui.QDialog, Ui_User):
    def __init__(self, dbhandler, user=None, parent=None):
        QtGui.QDialog.__init__(self,parent)        
        self.setupUi(self)       
        self.dbhandler = dbhandler
        self.user = dbhandler.session.query(User).filter_by(login=user.__str__()).first()
        
        if user != None:
            self.txtFullName.setText(self.user.full_name)
            self.txtLogin.setText(self.user.login)
    
    def validate(self):
        if self.user == None and self.txtPassword.text == '':
            return False
        
        return True
    
    def accept(self):
        if self.validate() != True:
            return
        
        if self.user == None:
            self.user = User(self.txtLogin.text().__str__(),self.txtPassword.text().__str__(),self.txtFullName.text().__str__())
        else:
            self.user.full_name = self.txtFullName.text().__str__() 
            self.user.login = self.txtLogin.text().__str__()
        
            if self.txtPassword != None:
                self.user.password = self.txtPassword.text().__str__()
        
        self.dbhandler.session.add(self.user)
        self.dbhandler.session.commit()
        
        restrict = ActionRestrict(self.user.id, '1', 1, user_root_acts )
        
        self.dbhandler.session.add(restrict)
        self.dbhandler.session.commit()
        
        self.close()
        
    def reject(self):
        self.close()
        
    def closeEvent(self, event):
        self.parent().update_data()
        event.accept()
        