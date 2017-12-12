# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(977, 716)
        UserWindow.setStyleSheet("*{font-size:15px;font-family:\"微软雅黑\",\"宋体\";color:#333;font-weight:normal;outline:none;}\n"
"QLabel{background:transparent;outline:none;color:#333;}\n"
"\n"
"/**QComboBox,QDateEdit**/\n"
"QComboBox,QDateEdit,QDateTimeEdit{outline:none;color:#333;background-color:#fff;border:1px solid #a9a9a8;border-radius:0px;}\n"
"QComboBox:focus,QDateEdit:focus,QDateTimeEdit:focus{color: #333;border:1px solid #bfbfbf;background-color:#eefcfc;}\n"
"QComboBox::drop-down,QDateEdit::drop-down,QDateTimeEdit::drop-down{border-left:1px solid #a9a9a8;background-color:qlineargradient(y1: 0, x1: 0, y2: 1, x2: 0,stop: 0 #fcfcfb, stop: 0.5 #f1eeec,stop: 1 #e7e1dc);}\n"
"QComboBox::drop-down:hover{border-left:1px solid #a9a9a8;background-color:qlineargradient(y1: 0, x1: 0, y2: 1, x2: 0,stop: 0 #eee, stop: 0.5 #ddd,stop: 1 #ccc);}\n"
"\n"
"QPushButton{ color: white; background-color: #27a9e3; border-width: 0px; border-radius: 3px;}\n"
"\n"
"/**QRadioButton**/\n"
"QRadioButton {spacing: 5px;outline:none;}\n"
"QRadioButton::indicator {width: 21px;height: 21px;}\n"
"\n"
"/**QCheckBox**/\n"
"QCheckBox {color:#333;spacing:0px;outline:none;}\n"
"QCheckBox::indicator {width: 15px; height: 15px;margin-right:5px;}\n"
"\n"
"/**QTabWidget**/\n"
"QTabWidget{border:none;margin:0px;outline:none;}\n"
"QTabWidget[showHeader=\'true\']::pane{border:1px solid #55B023;border-radius:0px;position: absolute;top: -1px;}\n"
"QTabWidget[showHeader=\'false\']::pane{border:none;position: absolute;margin:0px;}\n"
"QTabWidget[showHeader=\'true\'] QTabBar::tab{alignment:left;color:white;padding:2px 16px;margin-top:3px;margin-left:5px;height:21px;border-top-left-radius: 5px;border-top-right-radius: 5px;background:#C9B084}\n"
"QTabWidget[showHeader=\'true\'] QTabBar::tab:selected{background:#55B023;margin-top:1px;height:23px;}\n"
"")
        self.centralwidget = QtWidgets.QWidget(UserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.regsiter = QtWidgets.QWidget()
        self.regsiter.setObjectName("regsiter")
        self.layoutWidget = QtWidgets.QWidget(self.regsiter)
        self.layoutWidget.setGeometry(QtCore.QRect(-10, 120, 961, 314))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 4, 1, 1)
        self.username_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.username_input.setObjectName("username_input")
        self.gridLayout.addWidget(self.username_input, 2, 2, 1, 2)
        self.lname_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.lname_input.setObjectName("lname_input")
        self.gridLayout.addWidget(self.lname_input, 1, 2, 1, 2)
        self.fname_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.fname_input.setObjectName("fname_input")
        self.gridLayout.addWidget(self.fname_input, 0, 2, 1, 2)
        self.password_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 3, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.public_key_file_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.public_key_file_input.setEnabled(False)
        self.public_key_file_input.setObjectName("public_key_file_input")
        self.gridLayout.addWidget(self.public_key_file_input, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.file_selection_btn_2 = QtWidgets.QPushButton(self.splitter_5)
        self.file_selection_btn_2.setObjectName("file_selection_btn_2")
        self.gridLayout.addWidget(self.splitter_5, 5, 3, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.register_btn_2 = QtWidgets.QPushButton(self.splitter_4)
        self.register_btn_2.setObjectName("register_btn_2")
        self.gridLayout.addWidget(self.splitter_4, 7, 2, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 5, 1, 1)
        self.image_2 = QtWidgets.QWidget(self.layoutWidget)
        self.image_2.setStyleSheet("image: url(:/newPrefix/register.png);")
        self.image_2.setObjectName("image_2")
        self.gridLayout.addWidget(self.image_2, 0, 4, 6, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        self.tabWidget.addTab(self.regsiter, "")
        self.login = QtWidgets.QWidget()
        self.login.setObjectName("login")
        self.layoutWidget1 = QtWidgets.QWidget(self.login)
        self.layoutWidget1.setGeometry(QtCore.QRect(220, 240, 481, 189))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.password_login_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.password_login_input.setObjectName("password_login_input")
        self.gridLayout_2.addWidget(self.password_login_input, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.login_btn = QtWidgets.QPushButton(self.splitter)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout_2.addWidget(self.splitter, 4, 2, 1, 1)
        self.username_login_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.username_login_input.setObjectName("username_login_input")
        self.gridLayout_2.addWidget(self.username_login_input, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)
        self.label_directory = QtWidgets.QLabel(self.layoutWidget1)
        self.label_directory.setText("")
        self.label_directory.setObjectName("label_directory")
        self.gridLayout_2.addWidget(self.label_directory, 2, 2, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.keys_dir_btn = QtWidgets.QPushButton(self.splitter_3)
        self.keys_dir_btn.setEnabled(True)
        self.keys_dir_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.keys_dir_btn.setStyleSheet("")
        self.keys_dir_btn.setIconSize(QtCore.QSize(16, 16))
        self.keys_dir_btn.setObjectName("keys_dir_btn")
        self.gridLayout_2.addWidget(self.splitter_3, 3, 2, 1, 1)
        self.image = QtWidgets.QWidget(self.login)
        self.image.setGeometry(QtCore.QRect(300, 40, 401, 181))
        self.image.setStyleSheet("image: url(:/newPrefix/emblem-secure-messaging.png);")
        self.image.setObjectName("image")
        self.tabWidget.addTab(self.login, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 80, 871, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.text_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.text_input.setObjectName("text_input")
        self.gridLayout_3.addWidget(self.text_input, 4, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.gridLayoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.send_btn = QtWidgets.QPushButton(self.splitter_2)
        self.send_btn.setObjectName("send_btn")
        self.gridLayout_3.addWidget(self.splitter_2, 4, 1, 1, 1)
        self.signCheck = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.signCheck.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.signCheck.setObjectName("signCheck")
        self.gridLayout_3.addWidget(self.signCheck, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 1, 1, 1)
        self.text_output = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.text_output.setObjectName("text_output")
        self.gridLayout_3.addWidget(self.text_output, 0, 0, 3, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.clientsLists = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.clientsLists.setObjectName("clientsLists")
        self.verticalLayout.addWidget(self.clientsLists)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        UserWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 32))
        self.menubar.setObjectName("menubar")
        UserWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UserWindow)
        self.statusbar.setObjectName("statusbar")
        UserWindow.setStatusBar(self.statusbar)
        self.actionMinimize = QtWidgets.QAction(UserWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionFull_screen = QtWidgets.QAction(UserWindow)
        self.actionFull_screen.setObjectName("actionFull_screen")
        self.actionWhat_s_this = QtWidgets.QAction(UserWindow)
        self.actionWhat_s_this.setObjectName("actionWhat_s_this")
        self.actionWho_are_We = QtWidgets.QAction(UserWindow)
        self.actionWho_are_We.setObjectName("actionWho_are_We")
        self.actionClose = QtWidgets.QAction(UserWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen_new_window = QtWidgets.QAction(UserWindow)
        self.actionOpen_new_window.setObjectName("actionOpen_new_window")

        self.retranslateUi(UserWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)
        UserWindow.setTabOrder(self.fname_input, self.lname_input)
        UserWindow.setTabOrder(self.lname_input, self.username_input)
        UserWindow.setTabOrder(self.username_input, self.password_input)
        UserWindow.setTabOrder(self.password_input, self.public_key_file_input)
        UserWindow.setTabOrder(self.public_key_file_input, self.username_login_input)
        UserWindow.setTabOrder(self.username_login_input, self.password_login_input)
        UserWindow.setTabOrder(self.password_login_input, self.login_btn)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "Secure mail transfert application"))
        self.label_4.setText(_translate("UserWindow", "Password"))
        self.label_3.setText(_translate("UserWindow", "login"))
        self.label_2.setText(_translate("UserWindow", "Last name"))
        self.label.setText(_translate("UserWindow", "First name"))
        self.label_11.setText(_translate("UserWindow", "Key directory"))
        self.file_selection_btn_2.setText(_translate("UserWindow", "browse"))
        self.register_btn_2.setText(_translate("UserWindow", "Register"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.regsiter), _translate("UserWindow", "register "))
        self.label_9.setText(_translate("UserWindow", "Password"))
        self.login_btn.setText(_translate("UserWindow", "Login"))
        self.label_8.setText(_translate("UserWindow", "Username"))
        self.keys_dir_btn.setText(_translate("UserWindow", "Select keys directory"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), _translate("UserWindow", "login    "))
        self.send_btn.setText(_translate("UserWindow", "Send"))
        self.signCheck.setText(_translate("UserWindow", "Sign your Message"))
        self.label_6.setText(_translate("UserWindow", "Select your correspondant:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("UserWindow", "Comunication"))
        self.actionMinimize.setText(_translate("UserWindow", "&Minimize"))
        self.actionFull_screen.setText(_translate("UserWindow", "&Full screen"))
        self.actionWhat_s_this.setText(_translate("UserWindow", "&What\'s this"))
        self.actionWho_are_We.setText(_translate("UserWindow", "W&ho are We ?"))
        self.actionClose.setText(_translate("UserWindow", "&close"))
        self.actionOpen_new_window.setText(_translate("UserWindow", "&open new window"))


import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserWindow = QtWidgets.QMainWindow()
    ui = Ui_UserWindow()
    ui.setupUi(UserWindow)
    UserWindow.show()
    sys.exit(app.exec_())

