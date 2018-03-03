"""Wrappper platform for PyQT4."""
from PyQt4 import  QtCore, QtGui

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

    def translate(self, context, text, disambig):
        if not self.encoding:
            return QtGui.QApplication.translate(context, text, disambig)
        else:
            return QtGui.QApplication.translate(
                context, text, disambig, self.encoding)

    def unicode_string(self, string):
        return string

    def get_main_window(self):
        return QtGui.QMainWindow()

    def set_obj_name(self, obj, name):
        obj.setObjectName(self.fromUtf8(name))
        return obj

    def set_obj_size(self, obj, size):
        obj.resize(*size)
        return obj

    def set_obj_stylesheet(self, obj, stylesheet):
        obj.setStyleSheet(self.fromUtf8(stylesheet))
        return obj

    def set_obj_animated(self, obj, animated):
        obj.setAnimated(animated)
        return obj

    def set_uinified_title_and_tool_bar_on_mac(self, obj, value):
        obj.setUnifiedTitleAndToolBarOnMac(value)
        return obj

    def qt_widget_wrapper(self, obj):
        return QtGui.QWidget(obj)

    def get_graphics_widget(self, parent_widget):
        return QtGui.QGraphicsView(parent_widget)

    def set_obj_geometry(self, obj, rect):
        obj.setGeometry(QtCore.QRect(*rect))
        return obj

    def set_interactive(self, obj, value):
        obj.setInteractive(value)
        return obj

    def get_progress_bar_widget(self, parent_widget):
        return QtGui.QProgressBar(parent_widget)

    def set_obj_property(self, obj, property_name, property_value):
        obj.setProperty(property_name, property_value)
        return obj

    def set_text_visible(self, obj, value):
        obj.setTextVisible(value)
        return obj

    def get_slider_widget(self, parent_widget):
        return QtGui.QSlider(parent_widget)

    def set_obj_enabled(self, obj, value):
        obj.setEnabled(value)
        return obj

    @property
    def horizontal_orientation(self):
        return QtCore.Qt.Horizontal

    @property
    def vertical_orientation(self):
        return QtCore.Qt.Vertical

    def get_push_button_widget(self, parent_widget):
        return QtGui.QPushButton(parent_widget)

    def get_font(self, family):
        font = QtGui.QFont()
        font.setFamily(self.fromUtf8(family))
        return font

    def set_font_size(self, font, size):
        font.setPointSize(size)
        return font

    def get_label(self, parent_widget):
        return QtGui.QLabel(parent_widget)

    def set_obj_font(self, obj, font):
        obj.setFont(font)
        return obj

    def set_font_bold(self, font, value):
        font.setBold(value)
        return font

    def set_font_underline(self, font, value):
        font.setUnderline(value)
        return font

    def set_font_weight(self, font, value):
        font.setWeight(value)
        return font

    def set_font_strikethrough(self, font, value):
        font.setStrikeOut(value)
        return font

    def set_font_kerning(self, font, value):
        font.setKerning(value)
        return font

    @property
    def center_alignment(self):
        return QtCore.Qt.AlignCenter

    def set_label_alignment(self, label, alignment):
        label.setAlignment(alignment)
        return label

    def get_plain_text_edit(self, parent_widget, readonly):
        widget = QtGui.QPlainTextEdit(parent_widget)
        widget.setReadOnly(readonly)
        return widget

    def set_central_widget(self, obj, widget):
        obj.setCentralWidget(widget)
        return obj

    def get_statusbar(self, window):
        return QtGui.QStatusBar(window)

    def set_window_statusbar(self, window, statusbar):
        window.setStatusBar(statusbar)
        return window

    def connect_slots_by_name(self, window):
        return QtCore.QMetaObject.connectSlotsByName(window)

    def set_window_title(self, window, context, title, disambig):
        window.setWindowTitle(self.translate(context, title, disambig))

    def set_obj_text(self, obj, context, title, disambig):
        obj.setText(self.translate(context, title, disambig))
        return obj

    def set_obj_plain_text(self, obj, context, title, disambig):
        obj.setPlainText(self.translate(context, title, disambig))
        return obj

    def get_application(self, args):
        return QtGui.QApplication(args)

    def connect_obj_event(self, obj, signal_name, listener):
        """Connects an event signal of given obj to a listener. A listener
        is a python callable.
        """
        return QtCore.QObject.connect(
            obj, QtCore.SIGNAL(signal_name), listener)
