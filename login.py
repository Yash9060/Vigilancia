# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from mongoDbtest import mongoDbtest1
from pymongo import MongoClient

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

class Ui_Dialog(object):
	def showMessageBox(self,title,message):
		msgBox = QtGui.QMessageBox()
		msgBox.setIcon(QtGui.QMessageBox.Warning)
		msgBox.setWindowTitle(title)
		msgBox.setText(message)
		msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
		msgBox.exec_()

	def loginCheck(self):
		username = unicode(self.uname_lineEdit.text())
		password = unicode(self.pass_lineEdit.text())
		mongo = mongoDbtest1()
		mongo.test(username,password)


	def setupUi(self, Dialog):
		Dialog.setObjectName(_fromUtf8("Dialog"))
		Dialog.resize(496, 265)
		self.u_name_label = QtGui.QLabel(Dialog)
		self.u_name_label.setGeometry(QtCore.QRect(150, 110, 71, 20))
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(False)
		font.setWeight(50)
		self.u_name_label.setFont(font)
		self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
		self.u_name_label.setObjectName(_fromUtf8("u_name_label"))
		self.pass_label = QtGui.QLabel(Dialog)
		self.pass_label.setGeometry(QtCore.QRect(150, 150, 71, 21))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.pass_label.setFont(font)
		self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
		self.pass_label.setObjectName(_fromUtf8("pass_label"))
		self.uname_lineEdit = QtGui.QLineEdit(Dialog)
		self.uname_lineEdit.setGeometry(QtCore.QRect(230, 110, 113, 20))
		self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
		self.pass_lineEdit = QtGui.QLineEdit(Dialog)
		self.pass_lineEdit.setGeometry(QtCore.QRect(230, 150, 113, 20))
		self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
		self.login_btn = QtGui.QPushButton(Dialog)
		self.login_btn.setGeometry(QtCore.QRect(230, 200, 51, 23))
		self.login_btn.setObjectName(_fromUtf8("login_btn"))
		######################### Button Event ##############################3
		self.login_btn.clicked.connect(self.loginCheck)
		#####################################################################
		self.label = QtGui.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(190, 10, 211, 51))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.label.setFont(font)
		self.label.setObjectName(_fromUtf8("label"))

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(_translate("Dialog", "Login Form", None))
		self.u_name_label.setText(_translate("Dialog", "USERNAME ", None))
		self.pass_label.setText(_translate("Dialog", "PASSWORD", None))
		self.login_btn.setText(_translate("Dialog", "Login", None))
		self.label.setText(_translate("Dialog", "Login Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

