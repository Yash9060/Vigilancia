"""Wrappper platform for PyQT4."""
from PyQT4 import  QtCore, QtGui

class Qt(object):
    def __init__(self):
        try:
            self.fromUtf8 = QtCore.QString.fromUtf8
        except AttributeError:
            self.fromUtf8 = self.unicode_string

        try:
            self.encoding = QtGui.QApplication.UnicodeUTF8
        except AttributeError:
            self.encoding = None

    def translate(context, text, disambig):
        if not self.encoding:
            return QtGui.QApplication.translate(context, text, disambig)
        else:
            return QtGui.QApplication.translate(
                context, text, disambig, self.encoding)

    def unicode_string(self, string):
        return s

    def get_main_window(self):
        return QtGui.QMainWindow()

    def set_object_name(self, object, name):
        object.setObjectName(self.fromUtf8(name))
        return object

    def set_object_size(self, object, size):
        object.resize(*size)
        return object

    def set_object_stylesheet(self, object, stylesheet):
        object.setStyleSheet(self.fromUtf8(stylesheet))
        return object

    def set_object_animated(self, object, animated):
        object.setAnimated(animated)
        return object

    def set_uinified_title_and_tool_bar_on_mac(self, object, value):
        object.setUnifiedTitleAndToolBarOnMac(value)
        return object

    def qt_widget_wrapper(self, object):
        return QtGui.QWidget(object)

    def get_graphics_widget(self, parent_widget):
        return QtGui.QGraphicsView(parent_widget)

    def set_geometry(self, object, rect):
        object.setGeometry(QtCore.QRect(*rect))
        return object

    def set_interactive(self, object, value):
        object.setInteractive(value)
        return object

    def get_progress_bar_widget(self, parent_widget):
        return QtGui.QProgressBar(parent_widget)

    def set_object_property(self, object, property_name, property_value):
        object.setProperty(property_name, property_value)
        return object

    def set_text_visible(self, object, value):
        object.setTextVisible(value)
        return object

    def get_slider_widget(self, parent_widget):
        return QtGui.QSlider(parent_widget)

    def set_object_enabled(self, object, value):
        object.setEnabled(value)
        return object

    def get_push_button_widget(self, parent_widget):
        return QtGui.QPushButton(parent_widget)

    def get_font(self, font):
        font = QtGui.QFont()
        font.setFamily(self.fromUtf8(font))
        return font

    def set_font_size(self, font, size):
        font.setPointSize(size)
        return font

    def get_label(self, parent_widget):
        return QtGui.QLabel(parent_widget)

    def set_object_font(self, object, font):
        object.setFont(font)
        return object

    def set_font_bold(self, font, value):
        font.setBold(value)
        return font

    def set_font_underline(self, font, value):
        font.setUnderline(value)
        return font

    def set_font_weights(self, font, value):
        font.setWeight(value)
        return font

    def set_font_strikethrough(self, font, value):
        font.setStrikeOut(value)
        return font

    def set_font_kerning(self, font, value):
        font.setKerning(value)
        return font

    @property
    def rich_text_format(self):
        return QtCore.Qt.RichText

    @property
    def set_center_alignment(self):
        return QtCore.Qt.AlignCenter

    def set_label_text_format(self, label, format):
        label.setTextFormat(format)
        return label

    def set_label_alignment(self, label, alignment):
        label.setAlignment(alignment)
        return label

    def get_plain_text_edit(self, parent_widget, readonly):
        widget = QtGui.QPlainTextEdit(parent_widget)
        widget.setReadOnly(readonly)
        return widget

    def set_central_widget(self, object, widget):
        object.setCentralWidget(widget)
        return object

    def get_statusbar(self, window):
        return QtGui.QtGui.QStatusBar(window)

    def set_window_statusbar(self, window, statusbar):
        window.setStatusBar(statusbar)
        return window

    def connect_slots_by_name(self, window):
        return QtCore.QMetaObject.connectSlotsByName(window)

    def set_window_title(self, window, context, title, disambig):
        window.setWindowTitle(_translate(context, title, disambig))

    def set_object_text(self, object, context, title, disambig):
        object.setText(_translate(context, title, disambig))
        return object

    def set_object_plain_text(self, object, context, title, disambig):
        object.setPlainText(_translate(context, title, disambig))
        return object

    def get_application(self, args):
        return QtGui.QApplication(args)

    def connect_object_event(object, signal_name, listener):
        """Connects an event signal of given object to a listener. A listener
        is a python callable.
        """
        return QtCore.QObject.connect(
            object, QtCore.SIGNAL(signal_name), listener)
