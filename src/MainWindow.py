# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Nov  5 22:03:17 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(602, 339)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 601, 261))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 591, 231))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lstUsers = QtGui.QListWidget(self.verticalLayoutWidget_3)
        self.lstUsers.setObjectName(_fromUtf8("lstUsers"))
        self.verticalLayout_3.addWidget(self.lstUsers)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btnAddUser = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.btnAddUser.setObjectName(_fromUtf8("btnAddUser"))
        self.horizontalLayout_2.addWidget(self.btnAddUser)
        self.btnEditUser = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.btnEditUser.setObjectName(_fromUtf8("btnEditUser"))
        self.horizontalLayout_2.addWidget(self.btnEditUser)
        self.btnDelUser = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.btnDelUser.setObjectName(_fromUtf8("btnDelUser"))
        self.horizontalLayout_2.addWidget(self.btnDelUser)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tabGroups = QtGui.QWidget()
        self.tabGroups.setObjectName(_fromUtf8("tabGroups"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tabGroups)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 591, 231))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.treeGroups = QtGui.QTreeWidget(self.verticalLayoutWidget_2)
        self.treeGroups.setTextElideMode(QtCore.Qt.ElideRight)
        self.treeGroups.setRootIsDecorated(True)
        self.treeGroups.setColumnCount(1)
        self.treeGroups.setObjectName(_fromUtf8("treeGroups"))
        self.treeGroups.headerItem().setText(0, _fromUtf8("1"))
        self.treeGroups.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.treeGroups)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnGroupAdd = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.btnGroupAdd.setObjectName(_fromUtf8("btnGroupAdd"))
        self.horizontalLayout_3.addWidget(self.btnGroupAdd)
        self.btnGroupEdit = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.btnGroupEdit.setObjectName(_fromUtf8("btnGroupEdit"))
        self.horizontalLayout_3.addWidget(self.btnGroupEdit)
        self.btnGroupDelete = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.btnGroupDelete.setObjectName(_fromUtf8("btnGroupDelete"))
        self.horizontalLayout_3.addWidget(self.btnGroupDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tabGroups, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuF_ile = QtGui.QMenu(self.menubar)
        self.menuF_ile.setObjectName(_fromUtf8("menuF_ile"))
        MainWindow.setMenuBar(self.menubar)
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.menuF_ile.addAction(self.action_Exit)
        self.menubar.addAction(self.menuF_ile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.btnAddUser, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.add_user)
        QtCore.QObject.connect(self.btnDelUser, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.delete_user)
        QtCore.QObject.connect(self.btnEditUser, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.edit_user)
        QtCore.QObject.connect(self.btnGroupAdd, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.add_group)
        QtCore.QObject.connect(self.btnGroupEdit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.edit_group)
        QtCore.QObject.connect(self.btnGroupDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.delete_group)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL(_fromUtf8("currentChanged(QWidget*)")), MainWindow.tab_changed)
        QtCore.QObject.connect(self.treeGroups, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.edit_group)
        QtCore.QObject.connect(self.treeGroups, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QTreeWidgetItem*,QTreeWidgetItem*)")), MainWindow.groupItemChanged)
        QtCore.QObject.connect(self.lstUsers, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), MainWindow.userItemChanged)
        QtCore.QObject.connect(self.lstUsers, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), MainWindow.edit_user)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "davadmin", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddUser.setText(QtGui.QApplication.translate("MainWindow", "Add user", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEditUser.setText(QtGui.QApplication.translate("MainWindow", "Edit user", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelUser.setText(QtGui.QApplication.translate("MainWindow", "Delete user", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Users", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGroupAdd.setText(QtGui.QApplication.translate("MainWindow", "Add group", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGroupEdit.setText(QtGui.QApplication.translate("MainWindow", "Edit group", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGroupDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete group", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGroups), QtGui.QApplication.translate("MainWindow", "Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.menuF_ile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))

