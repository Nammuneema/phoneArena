# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result10.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import json
from phoneSpecs import Ui_MainWindow as ps
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(633, 651)
        Form.setMinimumSize(QtCore.QSize(615, 520))
        Form.setMouseTracking(True)
        Form.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/PhoneSearch.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(208, 208, 208);"))
        self.name0 = QtGui.QLabel(Form)
        self.name0.setGeometry(QtCore.QRect(10, 240, 111, 16))
        self.name0.setObjectName(_fromUtf8("name0"))
        self.name1 = QtGui.QLabel(Form)
        self.name1.setGeometry(QtCore.QRect(170, 240, 111, 16))
        self.name1.setObjectName(_fromUtf8("name1"))
        self.name2 = QtGui.QLabel(Form)
        self.name2.setGeometry(QtCore.QRect(330, 240, 111, 16))
        self.name2.setObjectName(_fromUtf8("name2"))
        self.name3 = QtGui.QLabel(Form)
        self.name3.setGeometry(QtCore.QRect(480, 240, 111, 16))
        self.name3.setObjectName(_fromUtf8("name3"))
        self.name4 = QtGui.QLabel(Form)
        self.name4.setGeometry(QtCore.QRect(10, 420, 111, 16))
        self.name4.setObjectName(_fromUtf8("name4"))
        self.name5 = QtGui.QLabel(Form)
        self.name5.setGeometry(QtCore.QRect(170, 420, 111, 16))
        self.name5.setObjectName(_fromUtf8("name5"))
        self.name6 = QtGui.QLabel(Form)
        self.name6.setGeometry(QtCore.QRect(330, 420, 111, 16))
        self.name6.setObjectName(_fromUtf8("name6"))
        self.name7 = QtGui.QLabel(Form)
        self.name7.setGeometry(QtCore.QRect(480, 420, 111, 16))
        self.name7.setObjectName(_fromUtf8("name7"))
        self.name8 = QtGui.QLabel(Form)
        self.name8.setGeometry(QtCore.QRect(10, 610, 111, 16))
        self.name8.setObjectName(_fromUtf8("name8"))
        self.name9 = QtGui.QLabel(Form)
        self.name9.setGeometry(QtCore.QRect(170, 610, 111, 16))
        self.name9.setObjectName(_fromUtf8("name9"))
        self.phone0 = QtGui.QPushButton(Form)
        self.phone0.setGeometry(QtCore.QRect(10, 90, 111, 141))
        self.phone0.setAutoFillBackground(False)
        self.phone0.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/0.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone0.setIcon(icon1)
        self.phone0.setIconSize(QtCore.QSize(131, 131))
        self.phone0.setObjectName(_fromUtf8("phone0"))
        self.phone2 = QtGui.QPushButton(Form)
        self.phone2.setGeometry(QtCore.QRect(330, 90, 111, 141))
        self.phone2.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/2.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone2.setIcon(icon2)
        self.phone2.setIconSize(QtCore.QSize(131, 131))
        self.phone2.setObjectName(_fromUtf8("phone2"))
        self.phone1 = QtGui.QPushButton(Form)
        self.phone1.setGeometry(QtCore.QRect(170, 90, 111, 141))
        self.phone1.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/1.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone1.setIcon(icon3)
        self.phone1.setIconSize(QtCore.QSize(131, 131))
        self.phone1.setObjectName(_fromUtf8("phone1"))
        self.phone3 = QtGui.QPushButton(Form)
        self.phone3.setGeometry(QtCore.QRect(480, 90, 111, 141))
        self.phone3.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/3.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone3.setIcon(icon4)
        self.phone3.setIconSize(QtCore.QSize(131, 131))
        self.phone3.setObjectName(_fromUtf8("phone3"))
        self.phone4 = QtGui.QPushButton(Form)
        self.phone4.setGeometry(QtCore.QRect(10, 270, 111, 141))
        self.phone4.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/4.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone4.setIcon(icon5)
        self.phone4.setIconSize(QtCore.QSize(131, 131))
        self.phone4.setObjectName(_fromUtf8("phone4"))
        self.phone5 = QtGui.QPushButton(Form)
        self.phone5.setGeometry(QtCore.QRect(170, 270, 111, 141))
        self.phone5.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/5.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone5.setIcon(icon6)
        self.phone5.setIconSize(QtCore.QSize(131, 131))
        self.phone5.setObjectName(_fromUtf8("phone5"))
        self.phone6 = QtGui.QPushButton(Form)
        self.phone6.setGeometry(QtCore.QRect(330, 270, 111, 141))
        self.phone6.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/6.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone6.setIcon(icon7)
        self.phone6.setIconSize(QtCore.QSize(131, 131))
        self.phone6.setObjectName(_fromUtf8("phone6"))
        self.phone7 = QtGui.QPushButton(Form)
        self.phone7.setGeometry(QtCore.QRect(480, 270, 111, 141))
        self.phone7.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/7.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone7.setIcon(icon8)
        self.phone7.setIconSize(QtCore.QSize(131, 131))
        self.phone7.setObjectName(_fromUtf8("phone7"))
        self.phone8 = QtGui.QPushButton(Form)
        self.phone8.setGeometry(QtCore.QRect(10, 460, 111, 141))
        self.phone8.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/8.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone8.setIcon(icon9)
        self.phone8.setIconSize(QtCore.QSize(131, 131))
        self.phone8.setObjectName(_fromUtf8("phone8"))
        self.phone9 = QtGui.QPushButton(Form)
        self.phone9.setGeometry(QtCore.QRect(170, 460, 111, 141))
        self.phone9.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/9.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone9.setIcon(icon10)
        self.phone9.setIconSize(QtCore.QSize(131, 131))
        self.phone9.setObjectName(_fromUtf8("phone9"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 245, 611, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 430, 611, 31))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 620, 611, 31))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 10, 221, 71))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../Data/UI_Icon/Logomakr_6YHD7m.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.raise_()

        self.line_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.name0.raise_()
        self.name1.raise_()
        self.name2.raise_()
        self.name3.raise_()
        self.name4.raise_()
        self.name5.raise_()
        self.name6.raise_()
        self.name7.raise_()
        self.name8.raise_()
        self.name9.raise_()
        self.phone0.raise_()
        self.phone2.raise_()
        self.phone1.raise_()
        self.phone3.raise_()
        self.phone4.raise_()
        self.phone5.raise_()
        self.phone6.raise_()
        self.phone7.raise_()
        self.phone8.raise_()
        self.phone9.raise_()

        QtCore.QObject.connect(self.phone0, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press0)
        QtCore.QObject.connect(self.phone0, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press1)
        QtCore.QObject.connect(self.phone1, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press2)
        QtCore.QObject.connect(self.phone2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press3)
        QtCore.QObject.connect(self.phone3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press4)
        QtCore.QObject.connect(self.phone4, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press5)
        QtCore.QObject.connect(self.phone5, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press6)
        QtCore.QObject.connect(self.phone6, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press7)
        QtCore.QObject.connect(self.phone7, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press8)
        QtCore.QObject.connect(self.phone8, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        QtCore.QObject.connect(self.phone9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press9)
        QtCore.QObject.connect(self.phone9, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.phone0, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        import readJson as rj
        names = rj.getName()
        Form.setWindowTitle(_translate("Form", "Result", None))
        self.name0.setText(_translate("Form", names[0], None))
        self.name1.setText(_translate("Form", names[1], None))
        self.name2.setText(_translate("Form", names[2], None))
        self.name3.setText(_translate("Form", names[3], None))
        self.name4.setText(_translate("Form", names[4], None))
        self.name5.setText(_translate("Form", names[5], None))
        self.name6.setText(_translate("Form", names[6], None))
        self.name7.setText(_translate("Form", names[7], None))
        self.name8.setText(_translate("Form", names[8], None))
        self.name9.setText(_translate("Form", names[9], None))
        
        self.name1.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[1]), None))
        self.name2.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[2]), None))
        self.name3.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[3]), None))
        self.name4.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[4]), None))
        self.name5.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[5]), None))
        self.name6.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[6]), None))
        self.name7.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[7]), None))
        self.name8.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[8]), None))
        self.name9.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[9]), None))
        #self.name10.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[10]), None))
        self.name0.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[0]), None))
        self.phone0.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[0]), None))
        self.phone1.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[1]), None))
        self.phone2.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[2]), None))
        self.phone3.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[3]), None))
        self.phone4.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[4]), None))
        self.phone5.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[5]), None))
        self.phone6.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[6]), None))
        self.phone7.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[7]), None))
        self.phone8.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[8]), None))
        self.phone9.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[9]), None))
        
        def createData(self,name):
         ofl = open('../data/online/name.json','w')
         json.dump(name,ofl)
    def press0(self) :
        name = [self.name0.text(),0]
        self.createData(name)
        self.openSpecs()
        
    def press1(self) :
        name = [self.name1.text(),1]
        self.createData(name)
        self.openSpecs()
        
    def press2(self) :
        name = [self.name2.text(),2]
        self.createData(name)
        self.openSpecs()
        
    def press3(self) :
        name = [self.name3.text(),3]
        self.createData(name)
        self.openSpecs()
        
    def press4(self) :
        name = [self.name4.text(),4]
        self.createData(name)
        self.openSpecs()
        
    def press5(self) :
        name = [self.name5.text(),5]
        self.createData(name)
        self.openSpecs()
        
    def press6(self) :
        name = [self.name6.text(),6]
        self.createData(name)
        self.openSpecs()
        
    def press7(self) :
        name = [self.name7.text(),7]
        self.createData(name)
        self.openSpecs()
        
    def press8(self) :
        name = [self.name8.text(),8]
        self.createData(name)
        
    def press9(self) :
        name = [self.name9.text(),9]
        self.createData(name)
        self.openSpecs()
    
        
    def press10(self) :
        name = [self.name10.text(),10]
        self.createData(name)
        self.openSpecs()
        #self.hide()
        
    def openSpecs(self) :
        self.win = QtGui.QMainWindow()
        self.ui = ps()
        self.ui.setupUi(self.win)
            #QtCore.QCoreApplication.instance().quit()
            #self.close()
        self.win.show()
