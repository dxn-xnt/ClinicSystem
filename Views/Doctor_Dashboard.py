# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Doctor_Dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 791)
        MainWindow.setStyleSheet("*{\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    font: 900 10pt \"Satoshi Black\";\n"
"    background-color: transparent;\n"
"     border-radius: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 25px;\n"
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
"#User, #UserSpecialty {\n"
"    color: #F4F7ED;\n"
"}\n"
"#DoctorSidePanel {\n"
"     background-color: #2E6E65;\n"
"}\n"
"\n"
"#RecentText {\n"
"    color: #F4F7ED;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.NavBar)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DashBoardButton = QtWidgets.QPushButton(self.NavBar)
        self.DashBoardButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DashBoardButton.setIcon(icon)
        self.DashBoardButton.setIconSize(QtCore.QSize(30, 30))
        self.DashBoardButton.setObjectName("DashBoardButton")
        self.verticalLayout.addWidget(self.DashBoardButton)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.MainButtons = QtWidgets.QVBoxLayout()
        self.MainButtons.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.MainButtons.setSpacing(20)
        self.MainButtons.setObjectName("MainButtons")
        self.pushButton_3 = QtWidgets.QPushButton(self.NavBar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/lucide/icons/layout-dashboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.MainButtons.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.NavBar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/lucide/icons/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainButtons.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.NavBar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/lucide/icons/user-round-pen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.MainButtons.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.MainButtons)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.NavBar)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/lucide/icons/user-round-cog.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.NavBar)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/lucide/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.NavBar)
        self.MainBodyContainer = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy)
        self.MainBodyContainer.setStyleSheet("#MainBodyContainer {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QGraphicsView {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 100px;\n"
"    background: white;\n"
"}\n"
"\n"
"#TotalPatientOverview {\n"
"    border: 2px solid #2E6E65;\n"
"    border-radius: 15px;\n"
"    color: #2E6E65;\n"
"    text-align: left top;\n"
"}\n"
"\n"
"#DiagnosisButton, #TEXT {\n"
"    background-color: #2E6E65;\n"
"    text-align: left top;\n"
"}\n"
"\n"
"#InterfaceTitle  {\n"
"    font-size: 35px;\n"
"}\n"
"\n"
"#DoctorSidePanel {\n"
"    background-color: #b9cec4;\n"
"}\n"
"\n"
"#SeeAllButton {\n"
"    text-align: right;\n"
"    color: #2E6E65;\n"
"    font-size: 18px\n"
"}\n"
"\n"
"#Line {\n"
"    background-color: gray;\n"
"}\n"
"\n"
"#RecentText {\n"
"    color: #2E6E65;\n"
"}\n"
"\n"
"#User {\n"
"    color: #2B3752;\n"
"}\n"
"\n"
"#UserSpecialty {\n"
"    color: #2B3752;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"    text-align: center;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"QFrame#Histories QFrame {\n"
"    background-color: #8fb1a8;\n"
"}\n"
"\n"
"#TotalInfo {\n"
"    color: #2b3752;\n"
"    font-size: 33px;\n"
"}\n"
"\n"
"#TotalDescription {\n"
"    color: #2b3752;\n"
"    font-weight: 300;\n"
"    font-size: 12px;\n"
"}\n"
"")
        self.MainBodyContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainBodyContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainBodyContainer.setObjectName("MainBodyContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.MainBodyContainer)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Body = QtWidgets.QFrame(self.MainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy)
        self.Body.setMinimumSize(QtCore.QSize(0, 0))
        self.Body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Body.setObjectName("Body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Body)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Header = QtWidgets.QFrame(self.Body)
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.InterfaceTitle = QtWidgets.QLabel(self.Header)
        self.InterfaceTitle.setObjectName("InterfaceTitle")
        self.horizontalLayout_3.addWidget(self.InterfaceTitle)
        self.verticalLayout_6.addWidget(self.Header)
        self.ShortcutButtons = QtWidgets.QFrame(self.Body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShortcutButtons.sizePolicy().hasHeightForWidth())
        self.ShortcutButtons.setSizePolicy(sizePolicy)
        self.ShortcutButtons.setMinimumSize(QtCore.QSize(150, 150))
        self.ShortcutButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ShortcutButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ShortcutButtons.setObjectName("ShortcutButtons")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ShortcutButtons)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.TotalPatientOverview = QtWidgets.QFrame(self.ShortcutButtons)
        self.TotalPatientOverview.setMinimumSize(QtCore.QSize(450, 0))
        self.TotalPatientOverview.setMaximumSize(QtCore.QSize(500, 16777215))
        self.TotalPatientOverview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TotalPatientOverview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TotalPatientOverview.setObjectName("TotalPatientOverview")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.TotalPatientOverview)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.TotalPatientOverview)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("#pushButton_6 {\n"
"    color: black;\n"
"}")
        self.pushButton_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignLeft)
        self.TotalLabel = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TotalLabel.sizePolicy().hasHeightForWidth())
        self.TotalLabel.setSizePolicy(sizePolicy)
        self.TotalLabel.setObjectName("TotalLabel")
        self.horizontalLayout_5.addWidget(self.TotalLabel, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_8.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.TotalPatientOverview)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.TotalInfo = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TotalInfo.sizePolicy().hasHeightForWidth())
        self.TotalInfo.setSizePolicy(sizePolicy)
        self.TotalInfo.setObjectName("TotalInfo")
        self.horizontalLayout_7.addWidget(self.TotalInfo)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_7.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.TotalDescription = QtWidgets.QLabel(self.TotalPatientOverview)
        self.TotalDescription.setObjectName("TotalDescription")
        self.verticalLayout_8.addWidget(self.TotalDescription)
        self.horizontalLayout_6.addWidget(self.TotalPatientOverview)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_6.addWidget(self.ShortcutButtons)
        self.MainBody = QtWidgets.QFrame(self.Body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainBody.sizePolicy().hasHeightForWidth())
        self.MainBody.setSizePolicy(sizePolicy)
        self.MainBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainBody.setObjectName("MainBody")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.MainBody)
        self.verticalLayout_7.setContentsMargins(9, 10, 9, 30)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.LabelHolder = QtWidgets.QHBoxLayout()
        self.LabelHolder.setObjectName("LabelHolder")
        self.PatRec = QtWidgets.QLabel(self.MainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PatRec.sizePolicy().hasHeightForWidth())
        self.PatRec.setSizePolicy(sizePolicy)
        self.PatRec.setObjectName("PatRec")
        self.LabelHolder.addWidget(self.PatRec)
        self.SeeAllButton = QtWidgets.QPushButton(self.MainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SeeAllButton.sizePolicy().hasHeightForWidth())
        self.SeeAllButton.setSizePolicy(sizePolicy)
        self.SeeAllButton.setObjectName("SeeAllButton")
        self.LabelHolder.addWidget(self.SeeAllButton)
        self.verticalLayout_7.addLayout(self.LabelHolder)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_7.addItem(spacerItem3)
        self.tableWidget = QtWidgets.QTableWidget(self.MainBody)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    border: 2px solid white;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    border-color: #2e6e65;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: none;\n"
"    font: 700 16pt \"Arial\";\n"
"    background-color: #2e6e65;\n"
"    color: #f4f7ed;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    text-align: left;\n"
"    font: 700 16pt \"Arial\";\n"
"    background-color: #2e6e65;\n"
"    color: #f4f7ed;\n"
"    padding: 5px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_7.addWidget(self.tableWidget)
        self.verticalLayout_6.addWidget(self.MainBody)
        self.horizontalLayout_2.addWidget(self.Body)
        self.DoctorSidePanel = QtWidgets.QWidget(self.MainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DoctorSidePanel.sizePolicy().hasHeightForWidth())
        self.DoctorSidePanel.setSizePolicy(sizePolicy)
        self.DoctorSidePanel.setObjectName("DoctorSidePanel")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.DoctorSidePanel)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Profile = QtWidgets.QVBoxLayout()
        self.Profile.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.Profile.setContentsMargins(20, 50, 20, 50)
        self.Profile.setObjectName("Profile")
        self.PP = QtWidgets.QFrame(self.DoctorSidePanel)
        self.PP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PP.setObjectName("PP")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.PP)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ProfilePic = QtWidgets.QGraphicsView(self.PP)
        self.ProfilePic.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProfilePic.sizePolicy().hasHeightForWidth())
        self.ProfilePic.setSizePolicy(sizePolicy)
        self.ProfilePic.setMinimumSize(QtCore.QSize(0, 0))
        self.ProfilePic.setMaximumSize(QtCore.QSize(150, 150))
        self.ProfilePic.setStyleSheet("#ProfilePic {\n"
"    border-radius: 70px;\n"
"}")
        self.ProfilePic.setObjectName("ProfilePic")
        self.verticalLayout_5.addWidget(self.ProfilePic, 0, QtCore.Qt.AlignHCenter)
        self.Profile.addWidget(self.PP)
        self.User = QtWidgets.QLabel(self.DoctorSidePanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.User.sizePolicy().hasHeightForWidth())
        self.User.setSizePolicy(sizePolicy)
        self.User.setMinimumSize(QtCore.QSize(272, 0))
        self.User.setMaximumSize(QtCore.QSize(272, 16777215))
        self.User.setAlignment(QtCore.Qt.AlignLeading)
        self.User.setWordWrap(True)
        self.User.setObjectName("User")
        self.Profile.addWidget(self.User, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.UserSpecialty = QtWidgets.QLabel(self.DoctorSidePanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserSpecialty.sizePolicy().hasHeightForWidth())
        self.UserSpecialty.setSizePolicy(sizePolicy)
        self.UserSpecialty.setMinimumSize(QtCore.QSize(114, 0))
        self.UserSpecialty.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UserSpecialty.setAlignment(QtCore.Qt.AlignCenter)
        self.UserSpecialty.setWordWrap(True)
        self.UserSpecialty.setObjectName("UserSpecialty")
        self.Profile.addWidget(self.UserSpecialty, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.Profile)
        self.Histories = QtWidgets.QWidget(self.DoctorSidePanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Histories.sizePolicy().hasHeightForWidth())
        self.Histories.setSizePolicy(sizePolicy)
        self.Histories.setStyleSheet("#Histories QFrame {\n"
"    background-color: #8fb1a8;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#Histories QLabel {\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.Histories.setObjectName("Histories")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Histories)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RecentText = QtWidgets.QLabel(self.Histories)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RecentText.sizePolicy().hasHeightForWidth())
        self.RecentText.setSizePolicy(sizePolicy)
        self.RecentText.setObjectName("RecentText")
        self.verticalLayout_3.addWidget(self.RecentText)
        self.TextHolder = QtWidgets.QFrame(self.Histories)
        self.TextHolder.setMinimumSize(QtCore.QSize(0, 129))
        self.TextHolder.setMaximumSize(QtCore.QSize(16777215, 129))
        self.TextHolder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TextHolder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TextHolder.setObjectName("TextHolder")
        self.verticalLayout_3.addWidget(self.TextHolder, 0, QtCore.Qt.AlignTop)
        self.TextHolder_2 = QtWidgets.QFrame(self.Histories)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextHolder_2.sizePolicy().hasHeightForWidth())
        self.TextHolder_2.setSizePolicy(sizePolicy)
        self.TextHolder_2.setMinimumSize(QtCore.QSize(0, 129))
        self.TextHolder_2.setMaximumSize(QtCore.QSize(16777215, 129))
        self.TextHolder_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TextHolder_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TextHolder_2.setObjectName("TextHolder_2")
        self.verticalLayout_3.addWidget(self.TextHolder_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_4.addWidget(self.Histories)
        self.horizontalLayout_2.addWidget(self.DoctorSidePanel)
        self.horizontalLayout.addWidget(self.MainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Dashboard"))
        self.pushButton_2.setText(_translate("MainWindow", "Records"))
        self.pushButton.setText(_translate("MainWindow", "Patients"))
        self.pushButton_5.setText(_translate("MainWindow", "Profile"))
        self.pushButton_4.setText(_translate("MainWindow", "Logout"))
        self.InterfaceTitle.setText(_translate("MainWindow", "Dashboard"))
        self.TotalLabel.setText(_translate("MainWindow", "Total Patient"))
        self.TotalInfo.setText(_translate("MainWindow", "000"))
        self.TotalDescription.setText(_translate("MainWindow", "00 more than yesterday"))
        self.PatRec.setText(_translate("MainWindow", "Patient Records"))
        self.SeeAllButton.setText(_translate("MainWindow", "See all"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Patient ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Diagnosis"))
        self.User.setText(_translate("MainWindow", "Jayson Gabriel L. Limosnero"))
        self.UserSpecialty.setText(_translate("MainWindow", "Cardiologist"))
        self.RecentText.setText(_translate("MainWindow", "Recent"))
import Images.resources
