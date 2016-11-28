# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phonearena.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import getCompany as gc
import json
import getSpecs as gso
import getPhones as gpo


def readJson(name):
        with open('../Data/{}.json'.format(name)) as f:
            details = json.loads(f.read())
            return details
            
TopDevices = readJson("top10")
TopBrands = readJson("topBrand")
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_phoneArena(object):
    def setupUi(self, phoneArena):
        phoneArena.setObjectName(_fromUtf8("phoneArena"))
        phoneArena.resize(547, 525)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/UI_Icon/PhoneSearch.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        phoneArena.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(phoneArena)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 541, 501))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(208, 208, 208);"))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        #self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.home = QtGui.QWidget()
        self.home.setObjectName(_fromUtf8("home"))
        self.scrollArea = QtGui.QScrollArea(self.home)
        self.scrollArea.setGeometry(QtCore.QRect(10, 160, 301, 171))
        self.scrollArea.setStyleSheet(_fromUtf8("background-color: rgb(190,190,190);"))
        self.scrollArea.setFrameShape(QtGui.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.scrollArea.setSizeAdjustPolicy(QtGui.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 282, 329))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.phnHeading = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.phnHeading.setGeometry(QtCore.QRect(50, 0, 47, 13))
        self.phnHeading.setObjectName(_fromUtf8("phnHeading"))
        self.likeHeading = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.likeHeading.setGeometry(QtCore.QRect(200, 0, 47, 13))
        self.likeHeading.setObjectName(_fromUtf8("likeHeading"))
        self.pos0 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos0.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.pos0.setObjectName(_fromUtf8("pos0"))
        self.like0 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like0.setGeometry(QtCore.QRect(166, 30, 111, 16))
        self.like0.setObjectName(_fromUtf8("like0"))
        self.pos1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos1.setGeometry(QtCore.QRect(6, 60, 131, 16))
        self.pos1.setObjectName(_fromUtf8("pos1"))
        self.like1 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like1.setGeometry(QtCore.QRect(166, 60, 111, 16))
        self.like1.setObjectName(_fromUtf8("like1"))
        self.pos2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos2.setGeometry(QtCore.QRect(6, 90, 121, 16))
        self.pos2.setObjectName(_fromUtf8("pos2"))
        self.like2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like2.setGeometry(QtCore.QRect(166, 90, 101, 16))
        self.like2.setObjectName(_fromUtf8("like2"))
        self.pos3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos3.setGeometry(QtCore.QRect(6, 120, 131, 20))
        self.pos3.setObjectName(_fromUtf8("pos3"))
        self.like3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like3.setGeometry(QtCore.QRect(166, 120, 101, 16))
        self.like3.setObjectName(_fromUtf8("like3"))
        self.pos4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos4.setGeometry(QtCore.QRect(6, 150, 121, 20))
        self.pos4.setObjectName(_fromUtf8("pos4"))
        self.like4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like4.setGeometry(QtCore.QRect(166, 150, 101, 16))
        self.like4.setObjectName(_fromUtf8("like4"))
        self.pos5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos5.setGeometry(QtCore.QRect(6, 180, 111, 16))
        self.pos5.setObjectName(_fromUtf8("pos5"))
        self.like5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like5.setGeometry(QtCore.QRect(166, 180, 111, 16))
        self.like5.setObjectName(_fromUtf8("like5"))
        self.pos6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos6.setGeometry(QtCore.QRect(6, 210, 121, 16))
        self.pos6.setObjectName(_fromUtf8("pos6"))
        self.like6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like6.setGeometry(QtCore.QRect(166, 210, 111, 16))
        self.like6.setObjectName(_fromUtf8("like6"))
        self.pos7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos7.setGeometry(QtCore.QRect(6, 240, 121, 20))
        self.pos7.setObjectName(_fromUtf8("pos7"))
        self.like7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like7.setGeometry(QtCore.QRect(166, 240, 101, 16))
        self.like7.setObjectName(_fromUtf8("like7"))
        self.pos8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos8.setGeometry(QtCore.QRect(6, 270, 121, 16))
        self.pos8.setObjectName(_fromUtf8("pos8"))
        self.like8 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like8.setGeometry(QtCore.QRect(166, 270, 101, 16))
        self.like8.setObjectName(_fromUtf8("like8"))
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(10, 10, 261, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setGeometry(QtCore.QRect(140, 0, 20, 321))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pos9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.pos9.setGeometry(QtCore.QRect(10, 300, 121, 16))
        self.pos9.setObjectName(_fromUtf8("pos9"))
        self.like9 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.like9.setGeometry(QtCore.QRect(170, 300, 101, 20))
        self.like9.setObjectName(_fromUtf8("like9"))
        self.line.raise_()
        self.phnHeading.raise_()
        self.likeHeading.raise_()
        self.pos0.raise_()
        self.like0.raise_()
        self.pos1.raise_()
        self.like1.raise_()
        self.pos2.raise_()
        self.like2.raise_()
        self.pos3.raise_()
        self.like3.raise_()
        self.pos4.raise_()
        self.like4.raise_()
        self.pos5.raise_()
        self.like5.raise_()
        self.pos6.raise_()
        self.like6.raise_()
        self.pos7.raise_()
        self.like7.raise_()
        self.pos8.raise_()
        self.like8.raise_()
        self.line_2.raise_()
        self.pos9.raise_()
        self.like9.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.phoneArenaLogo = QtGui.QLabel(self.home)
        self.phoneArenaLogo.setGeometry(QtCore.QRect(10, 10, 331, 101))
        self.phoneArenaLogo.setText(_fromUtf8(""))
        self.phoneArenaLogo.setPixmap(QtGui.QPixmap(_fromUtf8("../Data/UI_Icon/Logomakr_6YHD7m.png")))
        self.phoneArenaLogo.setScaledContents(True)
        self.phoneArenaLogo.setObjectName(_fromUtf8("phoneArenaLogo"))
        self.topBrandHeading = QtGui.QLabel(self.home)
        self.topBrandHeading.setGeometry(QtCore.QRect(330, 160, 71, 16))
        self.topBrandHeading.setObjectName(_fromUtf8("topBrandHeading"))
        self.frame = QtGui.QFrame(self.home)
        self.frame.setGeometry(QtCore.QRect(330, 180, 181, 151))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(190, 190, 190);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.brand0 = QtGui.QLabel(self.frame)
        self.brand0.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.brand0.setObjectName(_fromUtf8("brand0"))
        self.brand1 = QtGui.QLabel(self.frame)
        self.brand1.setGeometry(QtCore.QRect(10, 40, 151, 16))
        self.brand1.setObjectName(_fromUtf8("brand1"))
        self.brand2 = QtGui.QLabel(self.frame)
        self.brand2.setGeometry(QtCore.QRect(10, 70, 151, 16))
        self.brand2.setObjectName(_fromUtf8("brand2"))
        self.brand3 = QtGui.QLabel(self.frame)
        self.brand3.setGeometry(QtCore.QRect(10, 100, 151, 16))
        self.brand3.setStyleSheet(_fromUtf8("background-color: rgb(190, 190, 190);"))
        self.brand3.setObjectName(_fromUtf8("brand3"))
        self.brand4 = QtGui.QLabel(self.frame)
        self.brand4.setGeometry(QtCore.QRect(10, 130, 151, 16))
        self.brand4.setObjectName(_fromUtf8("brand4"))
        self.refresh = QtGui.QPushButton(self.home)
        self.refresh.setGeometry(QtCore.QRect(230, 400, 75, 23))
        self.refresh.setObjectName(_fromUtf8("refresh"))
        self.phoneArenaLogo.raise_()
        self.scrollArea.raise_()
        self.topBrandHeading.raise_()
        self.frame.raise_()
        self.refresh.raise_()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/UI_Icon/home-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.home, icon1, _fromUtf8(""))
        self.finder = QtGui.QWidget()
        self.finder.setObjectName(_fromUtf8("finder"))
        self.searchBar = QtGui.QLineEdit(self.finder)
        self.searchBar.setGeometry(QtCore.QRect(80, 210, 351, 20))
        self.searchBar.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);"))
        self.searchBar.setObjectName(_fromUtf8("searchBar"))
        self.searchButton = QtGui.QPushButton(self.finder)
        self.searchButton.setGeometry(QtCore.QRect(200, 270, 111, 31))
        self.searchButton.setIcon(icon)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.logo = QtGui.QLabel(self.finder)
        self.logo.setGeometry(QtCore.QRect(100, 40, 311, 141))
        self.logo.setText(_fromUtf8(""))
        self.logo.setPixmap(QtGui.QPixmap(_fromUtf8("../Data/UI_Icon/Logomakr_1qkjc5.png")))
        self.logo.setScaledContents(True)
        self.logo.setObjectName(_fromUtf8("logo"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/UI_Icon/search-icon-png-21.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.finder, icon2, _fromUtf8(""))
        
        self.about = QtGui.QWidget()
        self.about.setObjectName(_fromUtf8("about"))
        self.ver = QtGui.QLabel(self.about)
        self.ver.setGeometry(QtCore.QRect(210, 190, 111, 21))
        self.ver.setObjectName(_fromUtf8("ver"))
        self.builddate = QtGui.QLabel(self.about)
        self.builddate.setGeometry(QtCore.QRect(210, 240, 121, 21))
        self.builddate.setObjectName(_fromUtf8("builddate"))
        self.openSource = QtGui.QTextBrowser(self.about)
        self.openSource.setGeometry(QtCore.QRect(140, 270, 281, 51))
        self.openSource.setFrameShape(QtGui.QFrame.NoFrame)
        self.openSource.setObjectName(_fromUtf8("openSource"))
        self.GSMArena = QtGui.QTextBrowser(self.about)
        self.GSMArena.setGeometry(QtCore.QRect(90, 340, 381, 31))
        self.GSMArena.setObjectName(_fromUtf8("GSMArena"))
        self.logo_2 = QtGui.QLabel(self.about)
        self.logo_2.setGeometry(QtCore.QRect(170, 100, 191, 71))
        self.logo_2.setText(_fromUtf8(""))
        self.logo_2.setPixmap(QtGui.QPixmap(_fromUtf8("../Data/UI_Icon/Logomakr_6YHD7m.png")))
        self.logo_2.setScaledContents(True)
        self.logo_2.setObjectName(_fromUtf8("logo_2"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/UI_Icon/About-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.about, icon4, _fromUtf8(""))
        phoneArena.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(phoneArena)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        phoneArena.setStatusBar(self.statusBar)

        self.retranslateUi(phoneArena)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.searchPhoneOnline)
        QtCore.QObject.connect(self.refresh, QtCore.SIGNAL(_fromUtf8("clicked()")),gc.getTopBrand)
        QtCore.QObject.connect(self.refresh, QtCore.SIGNAL(_fromUtf8("clicked()")),self.topDeviceList)
        QtCore.QMetaObject.connectSlotsByName(phoneArena)

    def retranslateUi(self, phoneArena):
        global TopDevices 
        global TopBrands
        topBrands = TopBrands
        
        local = TopDevices
        phoneArena.setWindowTitle(_translate("phoneArena", "phoneArena", None))
        self.phnHeading.setText(_translate("phoneArena", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Phone</span></p></body></html>", None))
        self.likeHeading.setText(_translate("phoneArena", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Likes</span></p></body></html>", None))
        self.pos0.setText(_translate("phoneArena", local[0][0], None))
        self.like0.setText(_translate("phoneArena",local[0][1], None))
        self.pos1.setText(_translate("phoneArena", local[1][0], None))
        self.like1.setText(_translate("phoneArena", local[1][1], None))
        self.pos2.setText(_translate("phoneArena", local[2][0], None))
        self.like2.setText(_translate("phoneArena", local[2][1], None))
        self.pos3.setText(_translate("phoneArena", local[3][0], None))
        self.like3.setText(_translate("phoneArena", local[3][1], None))
        self.pos4.setText(_translate("phoneArena", local[4][0], None))
        self.like4.setText(_translate("phoneArena", local[4][1], None))
        self.pos5.setText(_translate("phoneArena", local[5][0], None))
        self.like5.setText(_translate("phoneArena", local[5][1], None))
        self.pos6.setText(_translate("phoneArena", local[6][0], None))
        self.like6.setText(_translate("phoneArena", local[6][1], None))
        self.pos7.setText(_translate("phoneArena", local[7][0], None))
        self.like7.setText(_translate("phoneArena", local[7][1], None))
        self.pos8.setText(_translate("phoneArena", local[8][0], None))
        self.like8.setText(_translate("phoneArena", local[8][1], None))
        self.pos9.setText(_translate("phoneArena", local[9][0], None))
        self.like9.setText(_translate("phoneArena", local[9][1], None))        
        self.topBrandHeading.setText(_translate("phoneArena", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Brands</span></p></body></html>", None))
        self.brand0.setText(_translate("phoneArena", topBrands[0], None))
        self.brand1.setText(_translate("phoneArena", topBrands[1], None))
        self.brand2.setText(_translate("phoneArena", topBrands[2], None))
        self.brand3.setText(_translate("phoneArena", topBrands[3], None))
        self.brand4.setText(_translate("phoneArena", topBrands[4], None))
        self.refresh.setText(_translate("phoneArena", "Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("phoneArena", "Home", None))
        self.searchButton.setText(_translate("phoneArena", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.finder), _translate("phoneArena", "Finder", None))
        self.ver.setText(_translate("phoneArena", "<html><head/><body><p align=\"center\">ver 0.0.1</p></body></html>", None))
        self.builddate.setText(_translate("phoneArena", "<html><head/><body><p align=\"center\">Built on Nov 20 2016</p></body></html>", None))
        self.openSource.setHtml(_translate("phoneArena", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Phone Arena Is open source phone detail finding offline Application developed by students for educational purpose</p></body></html>", None))
        self.GSMArena.setHtml(_translate("phoneArena", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Phone Arena uses GSMarena.com to fech data</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("phoneArena", "About", None))
        self.tabWidget.setCurrentIndex(0)
    
    def topDeviceList(self):
        global TopDevices

        local = TopDevices

        self.pos0.setText(_translate("phoneArena", local[0][0], None))
        self.like0.setText(_translate("phoneArena",local[0][1], None))
        self.pos1.setText(_translate("phoneArena", local[1][0], None))
        self.like1.setText(_translate("phoneArena", local[1][1], None))
        self.pos2.setText(_translate("phoneArena", local[2][0], None))
        self.like2.setText(_translate("phoneArena", local[2][1], None))
        self.pos3.setText(_translate("phoneArena", local[3][0], None))
        self.like3.setText(_translate("phoneArena", local[3][1], None))
        self.pos4.setText(_translate("phoneArena", local[4][0], None))
        self.like4.setText(_translate("phoneArena", local[4][1], None))
        self.pos5.setText(_translate("phoneArena", local[5][0], None))
        self.like5.setText(_translate("phoneArena", local[5][1], None))
        self.pos6.setText(_translate("phoneArena", local[6][0], None))
        self.like6.setText(_translate("phoneArena", local[6][1], None))
        self.pos7.setText(_translate("phoneArena", local[7][0], None))
        self.like7.setText(_translate("phoneArena", local[7][1], None))
        self.pos8.setText(_translate("phoneArena", local[8][0], None))
        self.like8.setText(_translate("phoneArena", local[8][1], None))
        self.pos9.setText(_translate("phoneArena", local[9][0], None))
        self.like9.setText(_translate("phoneArena", local[9][1], None)) 
        
        global TopBrands
        topBrands = TopBrands
        self.brand0.setText(_translate("phoneArena", topBrands[0], None))
        self.brand1.setText(_translate("phoneArena", topBrands[1], None))
        self.brand2.setText(_translate("phoneArena", topBrands[2], None))
        self.brand3.setText(_translate("phoneArena", topBrands[3], None))
        self.brand4.setText(_translate("phoneArena", topBrands[4], None))
        
       
    def searchPhoneOnline(self):
        gpo.getName(gpo.createSoup(gpo.input2url(self.searchBar.text())))
        
        details = gso.getURL()
        if len(details) is 0 :
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowIcon(QtGui.QMessageBox.warning)
            msgBox.setWindowTitle("Not found")
            msgBox.setText('Please try again phone not found')
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            
            msgBox.exec_()
        else:
            if len(details) is 1:
                from result1 import Ui_Form as uf
            elif len(details) is 2:
                from result2 import Ui_Form as uf
            elif len(details) is 3:
                from result3 import Ui_Form as uf
            elif len(details) is 4:
                from result4 import Ui_Form as uf
            elif len(details) is 5:
                from result5 import Ui_Form as uf
            elif len(details) is 6:
                from result6 import Ui_Form as uf
            elif len(details) is 7:
                from result7 import Ui_Form as uf
            elif len(details) is 8:
                from result8 import Ui_Form as uf
            elif len(details) is 9:
                from result9 import Ui_Form as uf
            elif len(details) is 10:
                from result10 import Ui_Form as uf
            else:
                from result11 import Ui_Form as uf
            

            self.win = QtGui.QDialog()
            self.ui = uf()
            self.ui.setupUi(self.win)
            self.win.show()
    
def main():
    import sys
    app = QtGui.QApplication( sys.argv)
    find = QtGui.QMainWindow()
    findUi = Ui_phoneArena()
    findUi.setupUi(find)

    find.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()

