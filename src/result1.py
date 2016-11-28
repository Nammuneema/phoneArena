# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result1.ui'
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
        self.name0 = QtGui.QLabel(Form)
        self.name0.setGeometry(QtCore.QRect(10, 240, 111, 16))
        self.name0.setObjectName(_fromUtf8("name0"))
        
        self.phone0 = QtGui.QPushButton(Form)
        self.phone0.setGeometry(QtCore.QRect(10, 90, 111, 141))
        self.phone0.setAutoFillBackground(False)
        self.phone0.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../Data/online/images/0.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.phone0.setIcon(icon1)
        self.phone0.setIconSize(QtCore.QSize(131, 131))
        self.phone0.setObjectName(_fromUtf8("phone0"))
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
        #self.Logo.raise_()
        self.line_3.raise_()
        self.name0.raise_()
        self.phone0.raise_()

        QtCore.QObject.connect(self.phone0, QtCore.SIGNAL(_fromUtf8("clicked()")), self.press0)
        QtCore.QObject.connect(self.phone0, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.hide)
        

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.phone0, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        import readJson as rj
        names = rj.getName()
        Form.setWindowTitle(_translate("Form", "Result", None))
        self.name0.setText(_translate("Form", names[0], None))
        #self.name10.setText(_translate("Form", names[10], None))
        self.name10.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[10]), None))
        self.name0.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[0]), None))
        self.phone0.setToolTip(_translate("Form", "<html><head/><body><p>{}</p></body></html>".format(names[0]), None))
        
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

