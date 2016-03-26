import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
 
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
 
class BrowserDialog(object):
    def setupUi(self, Dialog):
        #Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(100, 100)
        self.qwebview = QWebView(Dialog)
        self.qwebview.setGeometry(QtCore.QRect(1, 1, 1340, 430))
        self.qwebview.setObjectName(_fromUtf8("kwebview"))
       
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
 
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Browser", "Browser", None))
