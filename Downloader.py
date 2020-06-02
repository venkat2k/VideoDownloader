# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
from pytube import YouTube
from bs4 import BeautifulSoup
import os


class Ui_MainWindow(object):
    def __init__(self):
        self.busy = False

    def getLink(self, searchText): 
        ''' fetches the YouTube URL for the search text. 
            If success, returns a string
            else returns None.'''
        try:
            searchText = searchText.replace(" ", "+")
            url = "https://www.youtube.com/results?search_query=" + searchText
            response = urllib.request.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, "html") # html content of the webpage
            tags = soup.findAll('img')
            for tag in tags:
                if tag['src'][:5] == "https":
                    videoID = tag['src'][23:34]
                    break
            link = "https://www.youtube.com/watch?v=" + videoID
            return link
        except UnboundLocalError:
            message = "The specified video could not be downloaded. Try a different video."
            self.message_box.appendPlainText(message)
            return None
        except urllib.error.URLError:
            message = "Check your internet connection and try again."
            self.message_box.appendPlainText(message)
            return None
        except:
            message = "Something unexpected happened. Try again."
            self.message_box.appendPlainText(message)
            return None
    
    def download(self, searchText, savePath, fileFormat):
        # downloads the YouTube video and saves it at savePath.
        
        if self.busy:
            message = "Another file is downloading. Please try later"
            self.message_box.appendPlainText(message)
            return None
        self.busy = True
        link = self.getLink(searchText)
        if link == None:
            self.busy = False
            return None
        try:
            yt = YouTube(link)
            if fileFormat == "mp3":
                vids = yt.streams.filter(only_audio = True).all()
            else:
                vids = yt.streams.all()
            vids[0].download(savePath)
            defaultName = vids[0].default_filename
            os.chdir(savePath)
            newName = searchText + "." + fileFormat
            os.rename(defaultName, newName)
            self.message_box.appendPlainText("Downloaded successfully at " + savePath)
        except FileExistsError:
            self.message_box.appendPlainText("The specified file already exists.")
        except FileNotFoundError:
            self.message_box.appendPlainText("The specified directory doesn't exist.")
        except:
            self.message_box.appendPlainText("Something unexpected happened. Try again.")
        finally:
            self.busy = False
    
    def initiate(self):
        searchText = self.search_textbox.text().strip()
        savePath = self.dir_textbox.text().strip()
        fileFormat = self.type_box.currentText().strip()
        self.message_box.setPlainText("")
        if len(searchText) == 0 or len(savePath) == 0 or len(fileFormat) == 0:
            self.message_box.appendPlainText("Enter a valid search text.")
        elif len(savePath) == 0:
            self.message_box.appendPlainText("Enter a valid save path.")
        else:
            self.download(searchText, savePath, fileFormat)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 420)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.download_btn = QtWidgets.QPushButton(self.centralwidget)
        self.download_btn.setGeometry(QtCore.QRect(110, 190, 180, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.download_btn.setFont(font)
        self.download_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_btn.setMouseTracking(False)
        self.download_btn.setAutoFillBackground(False)
        self.download_btn.setObjectName("download_btn")
        self.download_btn.clicked.connect(self.initiate)
        self.message_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.message_box.setGeometry(QtCore.QRect(40, 260, 321, 121))
        self.message_box.setObjectName("message_box")
        self.dir_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.dir_textbox.setGeometry(QtCore.QRect(90, 100, 221, 20))
        self.dir_textbox.setObjectName("dir_textbox")
        self.type_box = QtWidgets.QComboBox(self.centralwidget)
        self.type_box.setGeometry(QtCore.QRect(160, 145, 69, 22))
        self.type_box.setObjectName("type_box")
        self.type_box.addItem("mp4")
        self.type_box.addItem("mp3")
        self.search_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.search_textbox.setGeometry(QtCore.QRect(90, 50, 221, 20))
        self.search_textbox.setObjectName("search_textbox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 30, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 145, 47, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.download_btn.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Search Text"))
        self.label_2.setText(_translate("MainWindow", "Download Directory"))
        self.label_3.setText(_translate("MainWindow", "Format"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
