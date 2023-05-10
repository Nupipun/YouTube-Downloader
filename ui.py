# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YTui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 270))
        MainWindow.setMaximumSize(QtCore.QSize(640, 270))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Asset_1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EasyYTDLlabel = QtWidgets.QLabel(self.centralwidget)
        self.EasyYTDLlabel.setGeometry(QtCore.QRect(120, 0, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.EasyYTDLlabel.setFont(font)
        self.EasyYTDLlabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EasyYTDLlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EasyYTDLlabel.setObjectName("EasyYTDLlabel")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setGeometry(QtCore.QRect(110, 200, 0, 21))
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progress_bar.setObjectName("progress_bar")
        self.link_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.link_entry.setGeometry(QtCore.QRect(110, 140, 411, 20))
        self.link_entry.setObjectName("link_entry")
        self.enter_link_button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_link_button.setGeometry(QtCore.QRect(110, 110, 201, 23))
        self.enter_link_button.setObjectName("enter_link_button")
        self.download_links_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_links_button.setGeometry(QtCore.QRect(330, 110, 191, 23))
        self.download_links_button.setObjectName("download_links_button")
        self.remaining_download_links_label = QtWidgets.QLabel(self.centralwidget)
        self.remaining_download_links_label.setGeometry(QtCore.QRect(110, 60, 411, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remaining_download_links_label.sizePolicy().hasHeightForWidth())
        self.remaining_download_links_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.remaining_download_links_label.setFont(font)
        self.remaining_download_links_label.setAlignment(QtCore.Qt.AlignCenter)
        self.remaining_download_links_label.setObjectName("remaining_download_links_label")
        self.clear_latest = QtWidgets.QPushButton(self.centralwidget)
        self.clear_latest.setGeometry(QtCore.QRect(110, 170, 201, 23))
        self.clear_latest.setObjectName("clear_latest")
        self.empty_list = QtWidgets.QPushButton(self.centralwidget)
        self.empty_list.setGeometry(QtCore.QRect(330, 170, 191, 23))
        self.empty_list.setObjectName("empty_list")
        self.get_specific_format_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_specific_format_button.setGeometry(QtCore.QRect(220, 200, 201, 23))
        self.get_specific_format_button.setObjectName("get_specific_format_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 381, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuConfig = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(8)
        self.menuConfig.setFont(font)
        self.menuConfig.setObjectName("menuConfig")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChange_download_location = QtWidgets.QAction(MainWindow)
        self.actionChange_download_location.setObjectName("actionChange_download_location")
        self.menuConfig.addAction(self.actionChange_download_location)
        self.menubar.addAction(self.menuConfig.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy YouTube Downloader"))
        self.EasyYTDLlabel.setText(_translate("MainWindow", "Easy YouTube Downloader"))
        self.enter_link_button.setText(_translate("MainWindow", "Enter Link"))
        self.download_links_button.setText(_translate("MainWindow", "Download Links"))
        self.remaining_download_links_label.setText(_translate("MainWindow", "Downloads: no active downloads"))
        self.clear_latest.setText(_translate("MainWindow", "Clear latest"))
        self.empty_list.setText(_translate("MainWindow", "Empty list"))
        self.get_specific_format_button.setText(_translate("MainWindow", "Change format"))
        self.label.setText(_translate("MainWindow", "Active download format: MP4"))
        self.menuConfig.setTitle(_translate("MainWindow", "Config"))
        self.actionChange_download_location.setText(_translate("MainWindow", "Change download location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
