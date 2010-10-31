# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created: Fri Oct 29 19:50:07 2010
#      by: PyQt4 UI code generator 4.8
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_User(object):
    def setupUi(self, User):
        User.setObjectName(_fromUtf8("User"))
        User.resize(366, 139)
        self.buttonBox = QtGui.QDialogButtonBox(User)
        self.buttonBox.setGeometry(QtCore.QRect(20, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(User)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 101))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txtLogin = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtLogin.setObjectName(_fromUtf8("txtLogin"))
        self.gridLayout.addWidget(self.txtLogin, 0, 1, 1, 1)
        self.lblLogin = QtGui.QLabel(self.gridLayoutWidget)
        self.lblLogin.setObjectName(_fromUtf8("lblLogin"))
        self.gridLayout.addWidget(self.lblLogin, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.txtPassword = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.gridLayout.addWidget(self.txtPassword, 1, 1, 1, 1)
        self.txtFullName = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txtFullName.setObjectName(_fromUtf8("txtFullName"))
        self.gridLayout.addWidget(self.txtFullName, 2, 1, 1, 1)

        self.retranslateUi(User)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), User.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), User.reject)
        QtCore.QMetaObject.connectSlotsByName(User)

    def retranslateUi(self, User):
        User.setWindowTitle(QtGui.QApplication.translate("User", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLogin.setText(QtGui.QApplication.translate("User", "Login:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("User", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("User", "Full name:", None, QtGui.QApplication.UnicodeUTF8))

