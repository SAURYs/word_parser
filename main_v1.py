# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_v1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 792)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/word.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWhatsThis("")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 100, 75, 23))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(168, 100, 75, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 100, 75, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 100, 75, 23))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/file.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/pic/配置管理.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 30, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/pic/导出.svg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 30, 61, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pic/帮 助.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 60, 201, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 133, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 133, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 321, 501))
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 301, 471))
        self.listWidget.setObjectName("listWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 150, 691, 501))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 671, 471))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 80, 31, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/pic/当前选中.svg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 670, 302, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 157, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 157, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 157, 236))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setItalic(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 130, 991, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(130, 30, 20, 91))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(260, 30, 20, 91))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(380, 30, 20, 91))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(510, 30, 20, 91))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1168, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBook = QtWidgets.QAction(MainWindow)
        self.actionBook.setObjectName("actionBook")
        self.actionPaper = QtWidgets.QAction(MainWindow)
        self.actionPaper.setObjectName("actionPaper")
        self.actionNew_settings = QtWidgets.QAction(MainWindow)
        self.actionNew_settings.setObjectName("actionNew_settings")
        self.actionChange_exited_settings = QtWidgets.QAction(MainWindow)
        self.actionChange_exited_settings.setObjectName("actionChange_exited_settings")
        self.actionDirection_for_use = QtWidgets.QAction(MainWindow)
        self.actionDirection_for_use.setObjectName("actionDirection_for_use")
        self.actionContact_with_us = QtWidgets.QAction(MainWindow)
        self.actionContact_with_us.setObjectName("actionContact_with_us")
        self.actionView_license = QtWidgets.QAction(MainWindow)
        self.actionView_license.setObjectName("actionView_license")
        self.actionExport_file_as_PDF = QtWidgets.QAction(MainWindow)
        self.actionExport_file_as_PDF.setObjectName("actionExport_file_as_PDF")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.setting)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文档审查软件"))
        self.pushButton_7.setText(_translate("MainWindow", "打  开"))
        self.pushButton.setText(_translate("MainWindow", "配  置"))
        self.pushButton_2.setText(_translate("MainWindow", "导  出"))
        self.pushButton_3.setText(_translate("MainWindow", "帮  助"))
        self.label_6.setText(_translate("MainWindow", "状态显示"))
        self.groupBox.setTitle(_translate("MainWindow", "检测文件列表："))
        self.groupBox_2.setTitle(_translate("MainWindow", "预览"))
        self.pushButton_6.setText(_translate("MainWindow", "检查项选择"))
        self.pushButton_5.setText(_translate("MainWindow", "检    测"))
        self.pushButton_4.setText(_translate("MainWindow", "停止"))
        self.actionBook.setText(_translate("MainWindow", "book"))
        self.actionPaper.setText(_translate("MainWindow", "paper"))
        self.actionNew_settings.setText(_translate("MainWindow", "new settings"))
        self.actionChange_exited_settings.setText(_translate("MainWindow", "change existed settings"))
        self.actionDirection_for_use.setText(_translate("MainWindow", "direction for use"))
        self.actionContact_with_us.setText(_translate("MainWindow", "contact with us"))
        self.actionView_license.setText(_translate("MainWindow", "view license"))
        self.actionExport_file_as_PDF.setText(_translate("MainWindow", "export file as .doc"))

import help_rc
import mainapp_rc