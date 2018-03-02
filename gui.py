# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vigilancia.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1037, 563)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.897561 rgba(0, 30, 58, 255), stop:1 rgba(0, 181, 174, 255))"))
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Video_Window = QtGui.QGraphicsView(self.centralwidget)
        self.Video_Window.setGeometry(QtCore.QRect(30, 110, 401, 311))
        self.Video_Window.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: lightgray;\n"
""))
        self.Video_Window.setInteractive(True)
        self.Video_Window.setObjectName(_fromUtf8("Video_Window"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(320, 80, 118, 23))
        self.progressBar.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.sld_Object_detection = QtGui.QSlider(self.centralwidget)
        self.sld_Object_detection.setEnabled(True)
        self.sld_Object_detection.setGeometry(QtCore.QRect(700, 170, 31, 20))
        self.sld_Object_detection.setStyleSheet(_fromUtf8("QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 4px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-radius: 9px;\n"
"}\n"
"\n"
"\n"
"QSlider{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}"))
        self.sld_Object_detection.setMaximum(1)
        self.sld_Object_detection.setPageStep(1)
        self.sld_Object_detection.setProperty("value", 1)
        self.sld_Object_detection.setTracking(True)
        self.sld_Object_detection.setOrientation(QtCore.Qt.Horizontal)
        self.sld_Object_detection.setInvertedAppearance(False)
        self.sld_Object_detection.setInvertedControls(False)
        self.sld_Object_detection.setTickPosition(QtGui.QSlider.NoTicks)
        self.sld_Object_detection.setTickInterval(1)
        self.sld_Object_detection.setObjectName(_fromUtf8("sld_Object_detection"))
        self.Start = QtGui.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(340, 440, 91, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(11)
        self.Start.setFont(font)
        self.Start.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.2);\n"
"}\n"
"QPushButton {color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid white;\n"
"}\n"
""))
        self.Start.setObjectName(_fromUtf8("Start"))
        self.label_ObjectDetection = QtGui.QLabel(self.centralwidget)
        self.label_ObjectDetection.setGeometry(QtCore.QRect(510, 170, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(11)
        self.label_ObjectDetection.setFont(font)
        self.label_ObjectDetection.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.label_ObjectDetection.setObjectName(_fromUtf8("label_ObjectDetection"))
        self.label_Event_Detection = QtGui.QLabel(self.centralwidget)
        self.label_Event_Detection.setGeometry(QtCore.QRect(510, 280, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(11)
        self.label_Event_Detection.setFont(font)
        self.label_Event_Detection.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.label_Event_Detection.setObjectName(_fromUtf8("label_Event_Detection"))
        self.label_Abnormal_Activity = QtGui.QLabel(self.centralwidget)
        self.label_Abnormal_Activity.setGeometry(QtCore.QRect(510, 390, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(11)
        self.label_Abnormal_Activity.setFont(font)
        self.label_Abnormal_Activity.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.label_Abnormal_Activity.setObjectName(_fromUtf8("label_Abnormal_Activity"))
        self.label_Classifier = QtGui.QLabel(self.centralwidget)
        self.label_Classifier.setGeometry(QtCore.QRect(490, 100, 221, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_Classifier.setFont(font)
        self.label_Classifier.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.label_Classifier.setTextFormat(QtCore.Qt.RichText)
        self.label_Classifier.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Classifier.setObjectName(_fromUtf8("label_Classifier"))
        self.label_Predictions = QtGui.QLabel(self.centralwidget)
        self.label_Predictions.setGeometry(QtCore.QRect(770, 100, 221, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_Predictions.setFont(font)
        self.label_Predictions.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 0);"))
        self.label_Predictions.setTextFormat(QtCore.Qt.RichText)
        self.label_Predictions.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Predictions.setObjectName(_fromUtf8("label_Predictions"))
        self.Label_Vigilanci_Title = QtGui.QLabel(self.centralwidget)
        self.Label_Vigilanci_Title.setGeometry(QtCore.QRect(8, 9, 781, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Vigilanci_Title.setFont(font)
        self.Label_Vigilanci_Title.setAutoFillBackground(False)
        self.Label_Vigilanci_Title.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(255, 255, 255, 0)"))
        self.Label_Vigilanci_Title.setTextFormat(QtCore.Qt.RichText)
        self.Label_Vigilanci_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Vigilanci_Title.setObjectName(_fromUtf8("Label_Vigilanci_Title"))
        self.label_FileName = QtGui.QLabel(self.centralwidget)
        self.label_FileName.setGeometry(QtCore.QRect(30, 110, 401, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        self.label_FileName.setFont(font)
        self.label_FileName.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 30, 58, 150);"))
        self.label_FileName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FileName.setObjectName(_fromUtf8("label_FileName"))
        self.sld_Event_detection = QtGui.QSlider(self.centralwidget)
        self.sld_Event_detection.setGeometry(QtCore.QRect(700, 280, 31, 20))
        self.sld_Event_detection.setStyleSheet(_fromUtf8("QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 4px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 10px;\n"
"}\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QSlider{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}"))
        self.sld_Event_detection.setMaximum(1)
        self.sld_Event_detection.setPageStep(1)
        self.sld_Event_detection.setProperty("value", 0)
        self.sld_Event_detection.setTracking(True)
        self.sld_Event_detection.setOrientation(QtCore.Qt.Horizontal)
        self.sld_Event_detection.setInvertedAppearance(False)
        self.sld_Event_detection.setInvertedControls(False)
        self.sld_Event_detection.setTickPosition(QtGui.QSlider.NoTicks)
        self.sld_Event_detection.setTickInterval(1)
        self.sld_Event_detection.setObjectName(_fromUtf8("sld_Event_detection"))
        self.sld_Abnormal_Activity = QtGui.QSlider(self.centralwidget)
        self.sld_Abnormal_Activity.setGeometry(QtCore.QRect(700, 390, 31, 20))
        self.sld_Abnormal_Activity.setStyleSheet(_fromUtf8("QSlider{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 4px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::add-page:qlineargradient {\n"
"background: lightgrey;\n"
"border-top-right-radius: 9px;\n"
"border-bottom-right-radius: 9px;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"}"))
        self.sld_Abnormal_Activity.setMaximum(1)
        self.sld_Abnormal_Activity.setPageStep(1)
        self.sld_Abnormal_Activity.setProperty("value", 0)
        self.sld_Abnormal_Activity.setTracking(True)
        self.sld_Abnormal_Activity.setOrientation(QtCore.Qt.Horizontal)
        self.sld_Abnormal_Activity.setInvertedAppearance(False)
        self.sld_Abnormal_Activity.setInvertedControls(False)
        self.sld_Abnormal_Activity.setTickPosition(QtGui.QSlider.NoTicks)
        self.sld_Abnormal_Activity.setTickInterval(1)
        self.sld_Abnormal_Activity.setObjectName(_fromUtf8("sld_Abnormal_Activity"))
        self.File_Seletcion = QtGui.QPushButton(self.centralwidget)
        self.File_Seletcion.setGeometry(QtCore.QRect(30, 440, 301, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(11)
        self.File_Seletcion.setFont(font)
        self.File_Seletcion.setStyleSheet(_fromUtf8("QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.2);\n"
"}\n"
"QPushButton {color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid white;\n"
"}\n"
""))
        self.File_Seletcion.setObjectName(_fromUtf8("File_Seletcion"))
        self.label_DateTime = QtGui.QLabel(self.centralwidget)
        self.label_DateTime.setGeometry(QtCore.QRect(20, 80, 271, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        self.label_DateTime.setFont(font)
        self.label_DateTime.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid white;"))
        self.label_DateTime.setObjectName(_fromUtf8("label_DateTime"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 101, 421, 331))
        self.graphicsView_2.setAutoFillBackground(False)
        self.graphicsView_2.setStyleSheet(_fromUtf8("background-color: rgba(186, 46, 46, 1)"))
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView_2.setBackgroundBrush(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView_2.setForegroundBrush(brush)
        self.graphicsView_2.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(790, 270, 231, 84))
        self.plainTextEdit_2.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 4px;"))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(790, 160, 231, 84))
        self.plainTextEdit_3.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 4px;"))
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(790, 380, 231, 84))
        self.plainTextEdit_4.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"border: 1px solid white;\n"
"border-radius: 4px;"))
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.graphicsView_2.raise_()
        self.Video_Window.raise_()
        self.progressBar.raise_()
        self.sld_Object_detection.raise_()
        self.Start.raise_()
        self.label_ObjectDetection.raise_()
        self.label_Event_Detection.raise_()
        self.label_Abnormal_Activity.raise_()
        self.label_Classifier.raise_()
        self.label_Predictions.raise_()
        self.Label_Vigilanci_Title.raise_()
        self.label_FileName.raise_()
        self.sld_Event_detection.raise_()
        self.sld_Abnormal_Activity.raise_()
        self.File_Seletcion.raise_()
        self.label_DateTime.raise_()
        self.plainTextEdit_2.raise_()
        self.plainTextEdit_3.raise_()
        self.plainTextEdit_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vigilancia", None))
        self.Start.setText(_translate("MainWindow", "Start", None))
        self.label_ObjectDetection.setText(_translate("MainWindow", "Object Detection", None))
        self.label_Event_Detection.setText(_translate("MainWindow", "Event Detecion", None))
        self.label_Abnormal_Activity.setText(_translate("MainWindow", "Abnormal Activity", None))
        self.label_Classifier.setText(_translate("MainWindow", "Classifiers", None))
        self.label_Predictions.setText(_translate("MainWindow", "Predictions", None))
        self.Label_Vigilanci_Title.setText(_translate("MainWindow", "Vigilancia", None))
        self.label_FileName.setText(_translate("MainWindow", "stream / file name", None))
        self.File_Seletcion.setText(_translate("MainWindow", "Select file to stream", None))
        self.label_DateTime.setText(_translate("MainWindow", "Today\'s date and time", None))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "Event\n"
"", None))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", "Objects", None))
        self.plainTextEdit_4.setPlainText(_translate("MainWindow", "Activity", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

