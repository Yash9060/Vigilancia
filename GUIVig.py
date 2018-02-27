import sys, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui

def window():
	app = QApplication(sys.argv)
	box = QMainWindow()
	box.setGeometry(200,200,300,500)
	create_checkbox(box)
	sys.exit(app.exec_())

'''def button_clicked():
	os.system('python core/classifiers/YOLOClassifier.py')''' 

def create_checkbox(self):
	btn = QtGui.QPushButton("Import_file", self)
	btn.clicked.connect(import_file)
	btn.move(0,250)
	btn1 = QtGui.QPushButton("Play_Video", self)
	btn1.clicked.connect(Play_Video)
	btn1.move(0,400)

	global checkBox
	checkBox = QCheckBox('All',self)
	checkBox.setGeometry(0, 10, 300, 60)
	global checkBox1
	checkBox1 = QCheckBox('YOLO',self)
	checkBox1.setGeometry(0, 50, 300, 60)
	global checkBox2
	checkBox2 = QCheckBox('Scene_detection',self)
	checkBox2.setGeometry(0, 100, 300, 60)
	global checkBox3
	checkBox3= QCheckBox('Anomaly',self)
	checkBox3.setGeometry(0, 150, 300, 60)
	
	checkBox.stateChanged.connect(classifier_selection)
	checkBox1.stateChanged.connect(classifier_selection)
	checkBox2.stateChanged.connect(classifier_selection)
	checkBox3.stateChanged.connect(classifier_selection)
	self.show()

def import_file(self):
	w = QWidget()
	filename = QFileDialog.getOpenFileName(w, 'Open File', '/')
	fileName = filename
	print(os.getcwd())
	print(fileName)
	#this fileName(path) can be passed as parameter 
def Play_Video(self):
	print("INside video play")
	os.system('python Video2.py')

def classifier_selection():
	if(checkBox.isChecked() or (checkBox1.isChecked() and checkBox2.isChecked() and checkBox3.isChecked())):
		print("CheckBox 1 is ticked")#os.sytem(path/to/script)
	else:

		if (checkBox1.isChecked()):
			pass # path to some script using system.os()
		if (checkBox2.isChecked()):
			pass
		if (checkBox3.isChecked()):
			pass
		if (checkBox1.isChecked() and checkBox2.isChecked()):
			pass
		if (checkBox1.isChecked() and checkBox3.isChecked()):
			pass
		if (checkBox2.isChecked() and checkBox3.isChecked()):
			pass	
		else:
			print("Please select")


if __name__ == '__main__':
   window()