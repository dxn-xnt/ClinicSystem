# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Staff_TransactionList.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 693)
        MainWindow.setStyleSheet("*{\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    font: 900 16pt \"Satoshi Black\";\n"
"    background-color: transparent;\n"
"     border-radius: 10px;\n"
"    color: #F4F7ED;\n"
"    text-align: left;\n"
"    padding: 5px 5px;\n"
"}\n"
"#NavBar {\n"
"    background-color: #2E6E65;\n"
"}\n"
"QLabel {\n"
"    font: 900 10pt \"Satoshi Black\";\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    color: #2E6E65;\n"
"    qproperty-alignment: \'AlignLeft\';\n"
"    qproperty-wordWrap: true;\n"
"    background: transparent;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NavBar = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NavBar.sizePolicy().hasHeightForWidth())
        self.NavBar.setSizePolicy(sizePolicy)
        self.NavBar.setObjectName("NavBar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.NavBar)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DashBoardButton_2 = QtWidgets.QPushButton(self.NavBar)
        self.DashBoardButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/lucide/icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DashBoardButton_2.setIcon(icon)
        self.DashBoardButton_2.setIconSize(QtCore.QSize(40, 40))
        self.DashBoardButton_2.setObjectName("DashBoardButton_2")
        self.verticalLayout_3.addWidget(self.DashBoardButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.MainButtons_2 = QtWidgets.QVBoxLayout()
        self.MainButtons_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.MainButtons_2.setSpacing(20)
        self.MainButtons_2.setObjectName("MainButtons_2")
        self.DashboardButton = QtWidgets.QPushButton(self.NavBar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/lucide/icons/layout-dashboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DashboardButton.setIcon(icon1)
        self.DashboardButton.setIconSize(QtCore.QSize(40, 40))
        self.DashboardButton.setObjectName("DashboardButton")
        self.MainButtons_2.addWidget(self.DashboardButton)
        self.RecordsButton = QtWidgets.QPushButton(self.NavBar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/lucide/icons/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RecordsButton.setIcon(icon2)
        self.RecordsButton.setIconSize(QtCore.QSize(40, 40))
        self.RecordsButton.setObjectName("RecordsButton")
        self.MainButtons_2.addWidget(self.RecordsButton)
        self.TransactionsButton = QtWidgets.QPushButton(self.NavBar)
        self.TransactionsButton.setStyleSheet("QPushButton{\n"
"    font: 900 20pt \"Satoshi Black\";    \n"
"    border: 2px solid white;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/lucide/icons/tickets.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TransactionsButton.setIcon(icon3)
        self.TransactionsButton.setIconSize(QtCore.QSize(40, 40))
        self.TransactionsButton.setObjectName("TransactionsButton")
        self.MainButtons_2.addWidget(self.TransactionsButton)
        self.LabRequestButton = QtWidgets.QPushButton(self.NavBar)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/lucide/icons/test-tubes.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LabRequestButton.setIcon(icon4)
        self.LabRequestButton.setIconSize(QtCore.QSize(40, 40))
        self.LabRequestButton.setObjectName("LabRequestButton")
        self.MainButtons_2.addWidget(self.LabRequestButton)
        self.verticalLayout_3.addLayout(self.MainButtons_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ProfileButton = QtWidgets.QPushButton(self.NavBar)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/lucide/icons/user-round-cog.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProfileButton.setIcon(icon5)
        self.ProfileButton.setIconSize(QtCore.QSize(40, 40))
        self.ProfileButton.setObjectName("ProfileButton")
        self.verticalLayout_4.addWidget(self.ProfileButton)
        self.pushButton_10 = QtWidgets.QPushButton(self.NavBar)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/lucide/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_4.addWidget(self.pushButton_10)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.NavBar)
        self.MainBodyContainer = QtWidgets.QFrame(self.centralwidget)
        self.MainBodyContainer.setStyleSheet("#MainBodyContainer {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"#Header {\n"
"    padding: 10px 20px;\n"
"    padding-top: 20px;\n"
"}\n"
"QLabel {\n"
"    padding: 0px;\n"
"}\n"
"#UserType {\n"
"    font: 500 12pt \"Satoshi\";\n"
"    color: #2B3752;\n"
"}\n"
"#UserName {\n"
"    font: 900 16pt \"Satoshi\";\n"
"    color: #2B3752;\n"
"}\n"
"#InterfaceTitle{\n"
"    font-size: 35px;\n"
"}\n"
"QGraphicsView {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 25px;\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"")
        self.MainBodyContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainBodyContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainBodyContainer.setObjectName("MainBodyContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Header = QtWidgets.QFrame(self.MainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.InterfaceTitle = QtWidgets.QLabel(self.Header)
        self.InterfaceTitle.setObjectName("InterfaceTitle")
        self.horizontalLayout_2.addWidget(self.InterfaceTitle)
        self.UserPanel = QtWidgets.QHBoxLayout()
        self.UserPanel.setContentsMargins(-1, -1, 0, -1)
        self.UserPanel.setObjectName("UserPanel")
        self.UserInfo = QtWidgets.QVBoxLayout()
        self.UserInfo.setSpacing(0)
        self.UserInfo.setObjectName("UserInfo")
        self.UserPanel.addLayout(self.UserInfo)
        self.Profile = QtWidgets.QFrame(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Profile.sizePolicy().hasHeightForWidth())
        self.Profile.setSizePolicy(sizePolicy)
        self.Profile.setMinimumSize(QtCore.QSize(50, 50))
        self.Profile.setMaximumSize(QtCore.QSize(50, 50))
        self.Profile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Profile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Profile.setObjectName("Profile")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Profile)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.UserPanel.addWidget(self.Profile)
        self.horizontalLayout_2.addLayout(self.UserPanel)
        self.verticalLayout_5.addWidget(self.Header)
        self.MainBody = QtWidgets.QFrame(self.MainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainBody.sizePolicy().hasHeightForWidth())
        self.MainBody.setSizePolicy(sizePolicy)
        self.MainBody.setStyleSheet("#Searchbar {\n"
"    border: 2px solid #2E6E65;\n"
"    border-radius: 15px;\n"
"    text-align: center;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.MainBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainBody.setObjectName("MainBody")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.MainBody)
        self.verticalLayout_7.setContentsMargins(20, 0, 20, 20)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.SearchBarContainer = QtWidgets.QFrame(self.MainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchBarContainer.sizePolicy().hasHeightForWidth())
        self.SearchBarContainer.setSizePolicy(sizePolicy)
        self.SearchBarContainer.setMaximumSize(QtCore.QSize(16777215, 70))
        self.SearchBarContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchBarContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SearchBarContainer.setObjectName("SearchBarContainer")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SearchBarContainer)
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.SearchBar = QtWidgets.QWidget(self.SearchBarContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchBar.sizePolicy().hasHeightForWidth())
        self.SearchBar.setSizePolicy(sizePolicy)
        self.SearchBar.setStyleSheet("#SearchBar {\n"
"    background-color: #F4F7ED;\n"
"    border: 2px solid #2E6E65;\n"
"    border-radius: 15px;\n"
"}\n"
"#Search{\n"
"    background-color: transparent ;\n"
"    font: 300 14pt \"Lexend Light\";\n"
"}")
        self.SearchBar.setObjectName("SearchBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.SearchBar)
        self.horizontalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Search = QtWidgets.QLineEdit(self.SearchBar)
        self.Search.setObjectName("Search")
        self.horizontalLayout_3.addWidget(self.Search)
        self.SearchButton = QtWidgets.QPushButton(self.SearchBar)
        self.SearchButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/lucide/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon7)
        self.SearchButton.setIconSize(QtCore.QSize(30, 30))
        self.SearchButton.setObjectName("SearchButton")
        self.horizontalLayout_3.addWidget(self.SearchButton)
        self.horizontalLayout_4.addWidget(self.SearchBar)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.DiagnoseBox = QtWidgets.QComboBox(self.SearchBarContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DiagnoseBox.sizePolicy().hasHeightForWidth())
        self.DiagnoseBox.setSizePolicy(sizePolicy)
        self.DiagnoseBox.setStyleSheet("QComboBox {\n"
"    background-color: #D9E4DC;\n"
"    border: 2px solid #2E6E65;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font: 300 12pt \"Lexend Light\";\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left: 1px solid #2E6E65;\n"
"    background-color: #D9E4DC;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/icons/chevron-down.svg);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F4F7ED;\n"
"    selection-background-color: #CCE3D0;\n"
"    border: 1px solid #2E6E65;\n"
"    border-radius: 2px;\n"
"    outline: 0;\n"
"    font: 300 12pt \"Lexend Light\";\n"
"}")
        self.DiagnoseBox.setEditable(False)
        self.DiagnoseBox.setObjectName("DiagnoseBox")
        self.DiagnoseBox.addItem("")
        self.horizontalLayout_4.addWidget(self.DiagnoseBox)
        self.DateBox = QtWidgets.QComboBox(self.SearchBarContainer)
        self.DateBox.setStyleSheet("QComboBox {\n"
"    background-color: #D9E4DC;\n"
"    border: 2px solid #2E6E65;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font: 300 12pt \"Lexend Light\";\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left: 1px solid #2E6E65;\n"
"    background-color: #D9E4DC;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/icons/chevron-down.svg);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F4F7ED;\n"
"    selection-background-color: #CCE3D0;\n"
"    border: 1px solid #2E6E65;\n"
"    border-radius: 2px;\n"
"    outline: 0;\n"
"    font: 300 12pt \"Lexend Light\";\n"
"}")
        self.DateBox.setObjectName("DateBox")
        self.DateBox.addItem("")
        self.horizontalLayout_4.addWidget(self.DateBox)
        spacerItem3 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_7.addWidget(self.SearchBarContainer)
        self.widget = QtWidgets.QWidget(self.MainBody)
        self.widget.setStyleSheet("QPushButton {\n"
"    font: 900 10pt \"Satoshi Black\";\n"
"    background-color:  #2E6E65;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;    \n"
"    font-size: 20px;\n"
"    color: #F4F7ED;\n"
"    text-align: center;\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"     background: transparent;\n"
"     width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"        background: #C0C0C0;\n"
"        border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"        background: #A0A0A0;\n"
"}\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical{\n"
"        background: none;\n"
"        border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 498, 521))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TransactionTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.TransactionTable.setStyleSheet("QTableWidget {\n"
"    background-color: #F4F7ED;\n"
"    gridline-color: transparent;\n"
"    border-radius: 10px;\n"
"    border: 2px solid #2E6E65;\n"
"}\n"
"QTableWidget::item {\n"
"    border: none;\n"
"    font:500 16pt \"Satoshi\";\n"
"    color: #2B3752;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(46, 110, 101, 0.3);\n"
"}\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #2E6E65;\n"
"    color: white;\n"
"    font: 700 15pt \"Satoshi\";\n"
"    border: 2px solid #2E6E65;\n"
"}")
        self.TransactionTable.setObjectName("TransactionTable")
        self.TransactionTable.setColumnCount(4)
        self.TransactionTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TransactionTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TransactionTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TransactionTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TransactionTable.setHorizontalHeaderItem(3, item)
        self.TransactionTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.TransactionTable)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.addWidget(self.scrollArea)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(110, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ViewButton = QtWidgets.QPushButton(self.widget_2)
        self.ViewButton.setObjectName("ViewButton")
        self.verticalLayout.addWidget(self.ViewButton)
        self.horizontalLayout_5.addWidget(self.widget_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.widget)
        self.verticalLayout_5.addWidget(self.MainBody)
        self.horizontalLayout.addWidget(self.MainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DashboardButton.setText(_translate("MainWindow", " Dashboard"))
        self.RecordsButton.setText(_translate("MainWindow", " Records"))
        self.TransactionsButton.setText(_translate("MainWindow", " Transactions"))
        self.LabRequestButton.setText(_translate("MainWindow", " Lab Request"))
        self.ProfileButton.setText(_translate("MainWindow", " Settings"))
        self.pushButton_10.setText(_translate("MainWindow", " Logout"))
        self.InterfaceTitle.setText(_translate("MainWindow", "Transactions List"))
        self.DiagnoseBox.setItemText(0, _translate("MainWindow", "Sort By:"))
        self.DateBox.setItemText(0, _translate("MainWindow", "Sort Order: "))
        item = self.TransactionTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Check Up ID"))
        item = self.TransactionTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.TransactionTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Doctor"))
        item = self.TransactionTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.ViewButton.setText(_translate("MainWindow", "View"))
