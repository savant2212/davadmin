# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
#
# Created: Thu Oct 28 16:43:11 2010
#      by: PyQt4 UI code generator 4.8
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AuthDialog(object):
    def setupUi(self, AuthDialog):
        AuthDialog.setObjectName(_fromUtf8("AuthDialog"))
        AuthDialog.resize(350, 93)
        self.verticalLayoutWidget = QtGui.QWidget(AuthDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 91))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lblLogin = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblLogin.setObjectName(_fromUtf8("lblLogin"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblLogin)
        self.lblPassword = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblPassword.setObjectName(_fromUtf8("lblPassword"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lblPassword)
        self.txtLogin = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtLogin.setObjectName(_fromUtf8("txtLogin"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.txtLogin)
        self.txtPassword = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtPassword.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txtPassword.setObjectName(_fromUtf8("txtPassword"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.txtPassword)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(AuthDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AuthDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AuthDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AuthDialog)

    def retranslateUi(self, AuthDialog):
        AuthDialog.setWindowTitle(QtGui.QApplication.translate("AuthDialog", "Authentication", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLogin.setText(QtGui.QApplication.translate("AuthDialog", "Login:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPassword.setText(QtGui.QApplication.translate("AuthDialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))

