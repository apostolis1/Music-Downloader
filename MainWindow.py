# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import downloader

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(423, 284)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(423, 266))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 401, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.LocationLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LocationLabel.sizePolicy().hasHeightForWidth())
        self.LocationLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.LocationLabel.setFont(font)
        self.LocationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LocationLabel.setObjectName("LocationLabel")
        self.gridLayout.addWidget(self.LocationLabel, 0, 0, 1, 1)
        self.UrlLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UrlLabel.sizePolicy().hasHeightForWidth())
        self.UrlLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UrlLabel.setFont(font)
        self.UrlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UrlLabel.setObjectName("UrlLabel")
        self.gridLayout.addWidget(self.UrlLabel, 1, 0, 1, 1)
        self.SearchBtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SearchBtn.setFont(font)
        self.SearchBtn.setObjectName("SearchBtn")
        self.gridLayout.addWidget(self.SearchBtn, 0, 2, 1, 1)
        self.UrlEntry = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UrlEntry.sizePolicy().hasHeightForWidth())
        self.UrlEntry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UrlEntry.setFont(font)
        self.UrlEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.UrlEntry.setObjectName("UrlEntry")
        self.gridLayout.addWidget(self.UrlEntry, 1, 1, 1, 2)
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 240, 22))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.LocationDisplayLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.LocationDisplayLabel.setGeometry(QtCore.QRect(0, 0, 241, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LocationDisplayLabel.sizePolicy().hasHeightForWidth())
        self.LocationDisplayLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LocationDisplayLabel.setFont(font)
        self.LocationDisplayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LocationDisplayLabel.setObjectName("LocationDisplayLabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.DownloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadBtn.setGeometry(QtCore.QRect(170, 140, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownloadBtn.sizePolicy().hasHeightForWidth())
        self.DownloadBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.DownloadBtn.setFont(font)
        self.DownloadBtn.setObjectName("DownloadBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.LocationToSave = self.SearchBtn.clicked.connect(self.getLocation)
        self.DownloadBtn.clicked.connect(self.download)


    def getLocation(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self.MainWindow, "Select Directory"))
        self.LocationDisplayLabel.setText(file)
        return file

    def download(self):
        
        """ Creating a quick error window.
            This may be better done in the main class for better code design.
        """
        self.windowError = QtWidgets.QMessageBox()
        self.windowError.setIcon(QtWidgets.QMessageBox.Critical)
        self.windowError.setText("Provide both a valid URL and a valid Download Location")
        self.windowError.setWindowTitle("Error")

        #Getting the variables from the GUI
        downloadLoc = self.LocationDisplayLabel.text()
        URL = self.UrlEntry.text()

        #Check if both URL and Download Location are chosen, if not display the error widget.
        if URL.replace(" ", '') == '' or downloadLoc.replace(" ", '') == '' or downloadLoc == '-':
            self.windowError.exec_()
            return


        downloadFinal = downloadLoc.replace("/", "\\")

        """
            This is a solution, maybe it will be the cause of some problems, it works for all the tested cases but 
            I am not really sure if this is the best way to convert the string to raw string
            The intended result is to get a string from the line edit and convert it to a path string, which is the argument
            of the downloader.Downloader
        """

        myBot = downloader.Downloader(downloadFinal, 30)
        myBot.downloadPlayilistFromUrl(URL)
        return

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Downloader"))
        self.LocationLabel.setText(_translate("MainWindow", "Location:"))
        self.UrlLabel.setText(_translate("MainWindow", "Playlist URL:"))
        self.SearchBtn.setText(_translate("MainWindow", "Search"))
        self.LocationDisplayLabel.setText(_translate("MainWindow", "-"))
        self.DownloadBtn.setText(_translate("MainWindow", "Download"))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
