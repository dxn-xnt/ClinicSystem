# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_AddLabTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 392)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 392))
        MainWindow.setBaseSize(QtCore.QSize(700, 300))
        MainWindow.setStyleSheet("*{\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border: 0px;\n"
"    background-color: #F4F7ED;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, -1, 20, 20)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        self.Header.setStyleSheet("QLabel {\n"
"    font: bold 20pt \"Satoshi Black\";\n"
"    color: #2E6E65;\n"
"    qproperty-wordWrap: true;\n"
"    background: transparent;\n"
"    text-align: center;\n"
"}\n"
"#Subheader {\n"
"    font: 500 14pt \"Satoshi Medium\";\n"
"}")
        self.Header.setObjectName("Header")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Header)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title = QtWidgets.QLabel(self.Header)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout_2.addWidget(self.Title)
        self.Subheader = QtWidgets.QLabel(self.Header)
        self.Subheader.setAlignment(QtCore.Qt.AlignCenter)
        self.Subheader.setObjectName("Subheader")
        self.verticalLayout_2.addWidget(self.Subheader)
        self.verticalLayout.addWidget(self.Header, 0, QtCore.Qt.AlignTop)
        self.Body = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Body.sizePolicy().hasHeightForWidth())
        self.Body.setSizePolicy(sizePolicy)
        self.Body.setStyleSheet("QLabel {\n"
"    font: 300 12pt \"Lexend Light\";\n"
"    color: #2E6E65;\n"
"}\n"
"#Title_1, #Title_2, #Title_3 {\n"
"    font: 14pt \"Lexend SemiBold\";\n"
"}\n"
"#Indicator {\n"
"    font: 300 10pt \"Lexend Light\";\n"
"}\n"
"#StaffTypeCon, #StaffNameCon, #StaffInfoCon, #SpecializationCon {\n"
"    background-color: transparent;\n"
"}\n"
"*{\n"
"    background-color: transparent;\n"
"}\n"
"#Body {\n"
"    background-color: rgba(46, 110, 101, 77);\n"
"    border-radius: 15px;\n"
"}\n"
"QLineEdit, QComboBox, QDateEdit {\n"
"    background-color: #F4F7ED;\n"
"    border: 1px solid #2E6E65;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QComboBox, QDateEdit {\n"
"    background-color: #F4F7ED;\n"
"    border: 1px solid #2E6E65;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font: 300 12pt \"Lexend Light\";\n"
"}\n"
"\n"
"/* Drop-down arrow styling (QComboBox only) */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left: 1px solid #2E6E65;\n"
"    background-color: #D9E4DC;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/lucide/icons/chevron-down.svg);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"/* ComboBox dropdown list view */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #F4F7ED;\n"
"    selection-background-color: #CCE3D0;\n"
"    border: 1px solid #2E6E65;\n"
"    border-radius: 2px;\n"
"    outline: 0;\n"
"    font: 300 12pt \"Lexend Light\";\n"
"}\n"
"\n"
"/* ===== QDateEdit ===== */\n"
"QDateEdit {\n"
"    background-color: #F4F7ED;\n"
"    border: 1px solid #2E6E65;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"    font: 300 12pt \"Lexend Light\";\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border-left: 1px solid #2E6E65;\n"
"    background-color: #D9E4DC;\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/lucide/icons/calendar.svg);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"\n"
"/* ===== QCalendarWidget Popup ===== */\n"
"QCalendarWidget {\n"
"    background-color: #F4F7ED;\n"
"    border: 2px solid #2E6E65;\n"
"    border-radius: 10px;\n"
"    font: 300 10pt \"Lexend Light\";\n"
"}\n"
"\n"
"/* Month & Year Navigation */\n"
"QCalendarWidget QToolButton {\n"
"    background-color: #F4F7ED;\n"
"    border: none;\n"
"    color: #2E6E65;\n"
"    font: 300 12pt \"Lexend Light\";\n"
"    padding: 5px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth {\n"
"    qproperty-icon: url(:/lucide/icons/chevron-left.svg);\n"
"    qproperty-iconSize: 16px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"    qproperty-icon: url(:/lucide/icons/chevron-right.svg);\n"
"    qproperty-iconSize: 16px;\n"
"}\n"
"\n"
"/* Month/Year ComboBox & SpinBox */\n"
"QCalendarWidget QComboBox,\n"
"QCalendarWidget QSpinBox {\n"
"    background-color: #F4F7ED;\n"
"    border: 1px solid #2E6E65;\n"
"    border-radius: 6px;\n"
"    padding: 2px 6px;\n"
"    font: 300 11pt \"Lexend Light\";\n"
"    color: #2E6E65;\n"
"}\n"
"\n"
"/* Calendar Table (Dates & Grid) */\n"
"QCalendarWidget QTableView {\n"
"    background-color: #F4F7ED;\n"
"    border: none;\n"
"    selection-background-color: #2E6E65;\n"
"    font: 300 11pt \"Lexend Light\";\n"
"    gridline-color: #2E6E65;\n"
"}\n"
"\n"
"\n"
"")
        self.Body.setObjectName("Body")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Body)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.StaffTypeCon = QtWidgets.QWidget(self.Body)
        self.StaffTypeCon.setObjectName("StaffTypeCon")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.StaffTypeCon)
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.JoinedDate = QtWidgets.QWidget(self.StaffTypeCon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JoinedDate.sizePolicy().hasHeightForWidth())
        self.JoinedDate.setSizePolicy(sizePolicy)
        self.JoinedDate.setMinimumSize(QtCore.QSize(0, 0))
        self.JoinedDate.setObjectName("JoinedDate")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.JoinedDate)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.JoinedDate)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.LabID = QtWidgets.QLineEdit(self.JoinedDate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabID.sizePolicy().hasHeightForWidth())
        self.LabID.setSizePolicy(sizePolicy)
        self.LabID.setMinimumSize(QtCore.QSize(250, 35))
        self.LabID.setMaximumSize(QtCore.QSize(16777215, 35))
        self.LabID.setObjectName("LabID")
        self.verticalLayout_4.addWidget(self.LabID, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_3.addWidget(self.JoinedDate, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.StaffTypeCon, 0, QtCore.Qt.AlignTop)
        self.Specialization = QtWidgets.QWidget(self.Body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Specialization.sizePolicy().hasHeightForWidth())
        self.Specialization.setSizePolicy(sizePolicy)
        self.Specialization.setObjectName("Specialization")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Specialization)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Title_2 = QtWidgets.QLabel(self.Specialization)
        self.Title_2.setObjectName("Title_2")
        self.verticalLayout_8.addWidget(self.Title_2, 0, QtCore.Qt.AlignTop)
        self.widget_6 = QtWidgets.QWidget(self.Specialization)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_11 = QtWidgets.QWidget(self.widget_6)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_11)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_9 = QtWidgets.QLabel(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_17.addWidget(self.label_9, 0, QtCore.Qt.AlignTop)
        self.LabName = QtWidgets.QLineEdit(self.widget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabName.sizePolicy().hasHeightForWidth())
        self.LabName.setSizePolicy(sizePolicy)
        self.LabName.setMinimumSize(QtCore.QSize(0, 35))
        self.LabName.setMaximumSize(QtCore.QSize(16777215, 35))
        self.LabName.setObjectName("LabName")
        self.verticalLayout_17.addWidget(self.LabName)
        self.horizontalLayout_6.addWidget(self.widget_11, 0, QtCore.Qt.AlignTop)
        self.widget_10 = QtWidgets.QWidget(self.widget_6)
        self.widget_10.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_8 = QtWidgets.QLabel(self.widget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_16.addWidget(self.label_8, 0, QtCore.Qt.AlignTop)
        self.Price = QtWidgets.QLineEdit(self.widget_10)
        self.Price.setMinimumSize(QtCore.QSize(0, 35))
        self.Price.setObjectName("Price")
        self.verticalLayout_16.addWidget(self.Price)
        self.horizontalLayout_6.addWidget(self.widget_10, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_8.addWidget(self.widget_6, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.Specialization, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.Body)
        self.Buttons = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buttons.sizePolicy().hasHeightForWidth())
        self.Buttons.setSizePolicy(sizePolicy)
        self.Buttons.setObjectName("Buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Buttons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.Buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Cancel = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel.sizePolicy().hasHeightForWidth())
        self.Cancel.setSizePolicy(sizePolicy)
        self.Cancel.setMinimumSize(QtCore.QSize(200, 45))
        self.Cancel.setMaximumSize(QtCore.QSize(200, 45))
        self.Cancel.setStyleSheet("QPushButton {\n"
"    font: 900 10pt \"Satoshi Black\";\n"
"    background-color:  #2E6E65;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    color: #F4F7ED;\n"
"    text-align: center;\n"
"}")
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_2.addWidget(self.Cancel)
        self.AddLabTest = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddLabTest.sizePolicy().hasHeightForWidth())
        self.AddLabTest.setSizePolicy(sizePolicy)
        self.AddLabTest.setMinimumSize(QtCore.QSize(200, 45))
        self.AddLabTest.setMaximumSize(QtCore.QSize(200, 45))
        self.AddLabTest.setStyleSheet("QPushButton {\n"
"    font: 900 10pt \"Satoshi Black\";\n"
"    background-color:  #2E6E65;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"    color: #F4F7ED;\n"
"    text-align: center;\n"
"}")
        self.AddLabTest.setObjectName("AddLabTest")
        self.horizontalLayout_2.addWidget(self.AddLabTest)
        self.horizontalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.Buttons, 0, QtCore.Qt.AlignBottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "COVHACHA DIAGNOSTIC SYSTEM"))
        self.Subheader.setText(_translate("MainWindow", "Laboratory Test Registration"))
        self.label.setText(_translate("MainWindow", "Lab Test ID"))
        self.Title_2.setText(_translate("MainWindow", "Lab Test Details"))
        self.label_9.setText(_translate("MainWindow", "Name"))
        self.label_8.setText(_translate("MainWindow", "Labt Test Charge"))
        self.Cancel.setText(_translate("MainWindow", "Cancel"))
        self.AddLabTest.setText(_translate("MainWindow", "Add Lab Test"))
import Images.resources
