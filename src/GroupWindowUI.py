# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groups.ui'
#
# Created: Fri Nov  5 20:34:19 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GroupEdit(object):
    def setupUi(self, GroupEdit):
        GroupEdit.setObjectName(_fromUtf8("GroupEdit"))
        GroupEdit.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(GroupEdit)
        self.buttonBox.setGeometry(QtCore.QRect(50, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(GroupEdit)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 241))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblGroupName = QtGui.QLabel(self.verticalLayoutWidget)
        self.lblGroupName.setObjectName(_fromUtf8("lblGroupName"))
        self.horizontalLayout_2.addWidget(self.lblGroupName)
        self.txtGroupName = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.txtGroupName.setObjectName(_fromUtf8("txtGroupName"))
        self.horizontalLayout_2.addWidget(self.txtGroupName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lstUsrAvail = QtGui.QListWidget(self.verticalLayoutWidget)
        self.lstUsrAvail.setObjectName(_fromUtf8("lstUsrAvail"))
        self.horizontalLayout.addWidget(self.lstUsrAvail)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.btnAddToGroup = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnAddToGroup.setObjectName(_fromUtf8("btnAddToGroup"))
        self.verticalLayout_3.addWidget(self.btnAddToGroup)
        self.btnRemoveFromGroup = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnRemoveFromGroup.setObjectName(_fromUtf8("btnRemoveFromGroup"))
        self.verticalLayout_3.addWidget(self.btnRemoveFromGroup)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.lstUsrIn = QtGui.QListWidget(self.verticalLayoutWidget)
        self.lstUsrIn.setObjectName(_fromUtf8("lstUsrIn"))
        self.horizontalLayout.addWidget(self.lstUsrIn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(GroupEdit)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GroupEdit.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GroupEdit.reject)
        QtCore.QObject.connect(self.btnAddToGroup, QtCore.SIGNAL(_fromUtf8("clicked()")), GroupEdit.add_to_group)
        QtCore.QObject.connect(self.btnRemoveFromGroup, QtCore.SIGNAL(_fromUtf8("clicked()")), GroupEdit.remove_from_group)
        QtCore.QMetaObject.connectSlotsByName(GroupEdit)

    def retranslateUi(self, GroupEdit):
        GroupEdit.setWindowTitle(QtGui.QApplication.translate("GroupEdit", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGroupName.setText(QtGui.QApplication.translate("GroupEdit", "Group name", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GroupEdit", "Users", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GroupEdit", "Members", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddToGroup.setText(QtGui.QApplication.translate("GroupEdit", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRemoveFromGroup.setText(QtGui.QApplication.translate("GroupEdit", "<<", None, QtGui.QApplication.UnicodeUTF8))

