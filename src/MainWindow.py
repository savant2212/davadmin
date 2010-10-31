# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Oct 29 15:58:07 2010
#      by: PyQt4 UI code generator 4.8
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
        MainWindow.resize(602, 309)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 231))
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
        self.lstUsers = QtGui.QListView(self.tab)
        self.lstUsers.setGeometry(QtCore.QRect(0, 0, 531, 161))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstUsers.sizePolicy().hasHeightForWidth())
        self.lstUsers.setSizePolicy(sizePolicy)
        self.lstUsers.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lstUsers.setFrameShadow(QtGui.QFrame.Sunken)
        self.lstUsers.setObjectName(_fromUtf8("lstUsers"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 170, 258, 29))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnAddUser = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnAddUser.setObjectName(_fromUtf8("btnAddUser"))
        self.horizontalLayout_2.addWidget(self.btnAddUser)
        self.btnEditUser = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnEditUser.setObjectName(_fromUtf8("btnEditUser"))
        self.horizontalLayout_2.addWidget(self.btnEditUser)
        self.btnDelUser = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnDelUser.setObjectName(_fromUtf8("btnDelUser"))
        self.horizontalLayout_2.addWidget(self.btnDelUser)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tabGroups = QtGui.QWidget()
        self.tabGroups.setObjectName(_fromUtf8("tabGroups"))
        self.tabWidget.addTab(self.tabGroups, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuF_ile = QtGui.QMenu(self.menubar)
        self.menuF_ile.setObjectName(_fromUtf8("menuF_ile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.menuF_ile.addAction(self.action_Exit)
        self.menubar.addAction(self.menuF_ile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.btnAddUser, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.add_user)
        QtCore.QObject.connect(self.btnDelUser, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.delete_user)
        QtCore.QObject.connect(self.btnEditUser, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.edit_user)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "davadmin", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddUser.setText(QtGui.QApplication.translate("MainWindow", "Add user", None, QtGui.QApplication.UnicodeUTF8))
        self.btnEditUser.setText(QtGui.QApplication.translate("MainWindow", "Edit user", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelUser.setText(QtGui.QApplication.translate("MainWindow", "Delete user", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Users", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGroups), QtGui.QApplication.translate("MainWindow", "Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.menuF_ile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))

