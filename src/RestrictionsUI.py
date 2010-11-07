# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restrictions.ui'
#
# Created: Sun Nov  7 16:32:55 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Restrictions(object):
    def setupUi(self, Restrictions):
        Restrictions.setObjectName(_fromUtf8("Restrictions"))
        Restrictions.resize(400, 305)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Restrictions.sizePolicy().hasHeightForWidth())
        Restrictions.setSizePolicy(sizePolicy)
        Restrictions.setLayoutDirection(QtCore.Qt.LeftToRight)
        Restrictions.setAutoFillBackground(True)
        Restrictions.setSizeGripEnabled(False)
        self.verticalLayoutWidget = QtGui.QWidget(Restrictions)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblName = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblName.setObjectName(_fromUtf8("lblName"))
        self.horizontalLayout.addWidget(self.lblName)
        self.txtGroupName = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtGroupName.setEnabled(False)
        self.txtGroupName.setObjectName(_fromUtf8("txtGroupName"))
        self.horizontalLayout.addWidget(self.txtGroupName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tblUserRestriction = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.tblUserRestriction.setObjectName(_fromUtf8("tblUserRestriction"))
        self.tblUserRestriction.setColumnCount(0)
        self.tblUserRestriction.setRowCount(0)
        self.verticalLayout.addWidget(self.tblUserRestriction)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Restrictions)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Restrictions.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Restrictions.reject)
        QtCore.QMetaObject.connectSlotsByName(Restrictions)

    def retranslateUi(self, Restrictions):
        Restrictions.setWindowTitle(QtGui.QApplication.translate("Restrictions", "Restrictions", None, QtGui.QApplication.UnicodeUTF8))
        self.lblName.setText(QtGui.QApplication.translate("Restrictions", "Group name", None, QtGui.QApplication.UnicodeUTF8))

