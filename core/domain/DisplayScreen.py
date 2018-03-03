"""Class that generates and handles events on Vigilancia UI."""
from core.domain import SuspicionDetection
from core.platform.qt import qt4

class DisplayScreen(object): 
    def __init__(self, args):
        self.qt = qt4.Qt()
        self.app = self.qt.get_application(args)
        self.detector = SuspicionDetection.SuspicionDetection()

        self.main_window_stylesheet = ('background-color: '
            'qradialgradient(spread:pad, cx:0.461, cy:0.0511364, '
            'radius:1.04, fx:0.461, fy:0.0511818, stop:0 '
            'rgba(7, 14, 15, 255), stop:0.466019 rgba(18, 34, 36, 255), '
            'stop:1 rgba(0, 0, 0, 255))')
        self.main_window_size = (1037, 563)

        self.video_window_stylesheet = ('color: white;\n'
            'background-color: lightgray;\n')
        self.video_window_geometry = (30, 110, 401, 311)
        self.alert_window_stylesheet = (
            'background-color: rgba(186, 46, 46, 220)')
        self.alert_window_geometry = (20, 101, 421, 331)

        self.fps_bar_geometry = (320, 80, 118, 23)
        self.fps_bar_stylesheet = ('color: white;\n '
            'background-color: rgba(0, 0, 0, 0);')
        self.fps_bar_initial_value = 24
        self.fps_bar_maximum_value = 30

        self.slider_stylesheet = ('QSlider::handle:horizontal {\n'
            'background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n'
            '    stop:0 #eee, stop:1 #ccc);\n'
            'border: 1px solid #777;\n'
            'width: 4px;\n'
            'border-radius: 10px;\n'
            '}\n'
            'QSlider::add-page:qlineargradient {\n'
            'background: lightgrey;\n'
            'border-radius: 9px;\n'
            '}\n'
            '\n'
            '\n'
            'QSlider{\n'
            'background-color: rgba(0, 0, 0, 0);\n'
            '}')
        self.slider_maximum = 1
        self.slider_value = 0
        self.slider_page_step = 1
        self.slider_orientation = self.qt.horizontal_orientation
        self.object_detection_slider_geometry = (700, 170, 31, 20)
        self.event_detection_slider_geometry = (700, 280, 31, 20)
        self.abnormal_activity_slider_geometry = (700, 390, 31, 20)

        self.push_button_stylesheet = ('QPushButton:hover {\n'
            'background-color: rgba(255, 255, 255, 111);\n'
            '}\n'
            'QPushButton {\n'
            'color: white;\n'
            'background-color: rgba(0, 0, 0, 0);\n'
            'border: 1px solid white;\n'
            'border-radius: 5px;\n'
            '}')
        self.push_button_point_size = 11
        self.start_button_geometry = (340, 440, 91, 34)
        self.file_selection_button_geometry = (30, 440, 301, 34)

        self.default_font_family = 'DejaVu Sans Mono'

        self.label_color = 'white'
        self.label_stylesheet = ('color: %s;\n'
                'background-color: rgba(0, 0, 0, 0);' % self.label_color)

        self.detection_label_point_size = 11
        self.object_detection_label_geometry = (510, 170, 171, 20)
        self.event_detection_label_geometry = (510, 280, 171, 20)
        self.abnormal_activity_label_geometry = (510, 390, 171, 20)
        self.date_time_label_geometry = (20, 80, 271, 18)

        self.file_name_label_stylesheet = ('color: %s;\n'
                'background-color: rgba(0, 30, 58, 150);' % self.label_color)
        self.file_name_label_geometry = (30, 110, 401, 20)

        self.heading_label_point_size = 13
        self.heading_label_alignment = self.qt.center_alignment
        self.classifier_label_geometry = (490, 100, 221, 18)
        self.prediction_label_geometry = (770, 100, 221, 18)

        self.detection_view_stylesheet = ('background-color: '
            'rgba(0, 0, 0, 0);\n'
            'color: white;\n'
            'border: 1px solid white;\n'
            'border-radius: 4px;')
        self.objects_detected_view_geometry = (790, 170, 231, 84)
        self.events_detected_view_geometry = (790, 280, 231, 84)
        self.activity_detected_view_geometry = (790, 390, 231, 84)

        self.title_label_point_size = 28
        self.vigilancia_title_label_geometry = (8, 9, 1031, 51)

    def add_graphics_view(
            self, parent, name, geometry, stylesheet, interactive):
        obj = self.qt.get_graphics_widget(parent)
        self.qt.set_obj_name(obj, name)
        self.qt.set_obj_stylesheet(obj, stylesheet)
        self.qt.set_obj_geometry(obj, geometry)
        self.qt.set_interactive(obj, interactive)
        return obj

    def add_progress_bar(
            self, parent, name, geometry, stylesheet, value, maximum,
            text_visible):
        obj = self.qt.get_progress_bar_widget(parent)
        self.qt.set_obj_name(obj, name)
        self.qt.set_obj_geometry(obj, geometry)
        self.qt.set_obj_stylesheet(obj, stylesheet)
        self.qt.set_obj_property(obj, 'value', value)
        self.qt.set_obj_property(obj, 'maximum', maximum)
        self.qt.set_text_visible(obj, text_visible)
        return obj

    def add_slider(
            self, parent, name, geometry, stylesheet, value, page_step,
            maximum, enabled, orientation=None):
        obj = self.qt.get_slider_widget(parent)
        self.qt.set_obj_name(obj, name)
        self.qt.set_obj_geometry(obj, geometry)
        self.qt.set_obj_stylesheet(obj, stylesheet)
        self.qt.set_obj_enabled(obj, enabled)
        self.qt.set_obj_property(obj, 'value', value)
        self.qt.set_obj_property(obj, 'pageStep', page_step)
        self.qt.set_obj_property(obj, 'maximum', maximum)
        
        if not orientation:
            orientation = self.qt.horizontal_orientation
        self.qt.set_obj_property(obj, 'orientation', orientation)
        return obj

    def add_push_button(
            self, parent, name, geometry, stylesheet, font):
        obj = self.qt.get_push_button_widget(parent)
        self.qt.set_obj_name(obj, name)
        self.qt.set_obj_geometry(obj, geometry)
        self.qt.set_obj_stylesheet(obj, stylesheet)
        self.qt.set_obj_font(obj, font)
        return obj

    def add_label(
            self, parent, name, geometry, stylesheet, font, alignment=None):
        obj = self.qt.get_label(parent)
        self.qt.set_obj_name(obj, name)
        self.qt.set_obj_geometry(obj, geometry)
        self.qt.set_obj_stylesheet(obj, stylesheet)
        self.qt.set_obj_font(obj, font)
        if alignment:
            self.qt.set_label_alignment(obj, self.qt.center_alignment)
        return obj

    def add_plain_text_widget(
            self, parent, name, geometry, stylesheet, readonly=True):
        obj = self.qt.get_plain_text_edit(parent, readonly)
        self.qt.set_obj_name(obj, name)
        self.qt.set_obj_geometry(obj, geometry)
        self.qt.set_obj_stylesheet(obj, stylesheet)
        return obj

    def add_main_window(self, name, stylesheet, size):
        obj = self.qt.get_main_window()
        self.qt.set_obj_name(obj, name)
        self.qt.set_obj_stylesheet(obj, stylesheet)
        self.qt.set_obj_size(obj, size)
        return obj

    def get_font(
            self, family, point_size, bold=False, underline=False,
            strikethrough=False, weight=None, kerning=None):
        font = self.qt.get_font(family)
        self.qt.set_font_size(font, point_size)

        if bold:
            self.qt.set_font_bold(font, bold)

        if underline:
            self.qt.set_font_underline(font, underline)

        if strikethrough:
            self.qt.set_font_strikethrough(font, strikethrough)

        if weight:
            self.qt.set_font_weight(font, weight)

        if kerning:
            self.qt.set_font_kerning(font, kerning)

        return font

    def create_ui_components(self):
        # Craete main window.
        self.main_window = self.add_main_window(
            'MainWindow', self.main_window_stylesheet, self.main_window_size)

        # Create central widget.
        self.central_widget = self.qt.qt_widget_wrapper(self.main_window)
        self.qt.set_obj_name(self.central_widget, 'CentralWidget')

        # Add video and alert graphic views.
        self.video_window = self.add_graphics_view(
            self.central_widget, 'VideoWindow', self.video_window_geometry,
            self.video_window_stylesheet, False)
        self.alert_window = self.add_graphics_view(
            self.central_widget, 'AlertWindow', self.alert_window_geometry,
            self.alert_window_stylesheet, False)

        # Add FPS progress bar.
        self.fps_bar = self.add_progress_bar(
            self.central_widget, 'FPSBar', self.fps_bar_geometry,
            self.fps_bar_stylesheet, self.fps_bar_initial_value,
            self.fps_bar_maximum_value, True)

        # Add sliders for tuning classifiers ON / OFF.
        self.object_detection_slider = self.add_slider(
            self.central_widget, 'ObjectDetectionSlider',
            self.object_detection_slider_geometry, self.slider_stylesheet,
            self.slider_value, self.slider_page_step, self.slider_maximum,
            True, self.slider_orientation)
        self.event_detection_slider = self.add_slider(
            self.central_widget, 'ObjectDetectionSlider',
            self.event_detection_slider_geometry, self.slider_stylesheet,
            self.slider_value, self.slider_page_step, self.slider_maximum,
            True, self.slider_orientation)
        self.abnormal_activity_slider = self.add_slider(
            self.central_widget, 'ObjectDetectionSlider',
            self.abnormal_activity_slider_geometry, self.slider_stylesheet,
            self.slider_value, self.slider_page_step, self.slider_maximum,
            True, self.slider_orientation)

        # Add buttons for starting video and opening files.
        self.button_font = self.get_font(
            self.default_font_family, self.push_button_point_size)
        self.start_button = self.add_push_button(
            self.central_widget, 'StartButton', self.start_button_geometry,
            self.push_button_stylesheet, self.button_font)
        self.file_selection_button = self.add_push_button(
            self.central_widget, 'FileSelectionButton',
            self.file_selection_button_geometry, self.push_button_stylesheet,
            self.button_font)

        # Add labels.
        self.detection_label_font = self.get_font(
            self.default_font_family, self.detection_label_point_size)
        self.object_detection_label = self.add_label(
            self.central_widget, 'ObjectDetectionLabel',
            self.object_detection_label_geometry, self.label_stylesheet,
            self.detection_label_font)
        self.event_detection_label = self.add_label(
            self.central_widget, 'EventDetectionLabel',
            self.event_detection_label_geometry, self.label_stylesheet,
            self.detection_label_font)
        self.abnormal_activity_label = self.add_label(
            self.central_widget, 'AbnormalActivityLabel',
            self.abnormal_activity_label_geometry, self.label_stylesheet,
            self.detection_label_font)
        self.date_time_label = self.add_label(
            self.central_widget, 'PredictionLabel',
            self.date_time_label_geometry, self.label_stylesheet,
            self.detection_label_font)

        self.heading_label_font = self.get_font(
            self.default_font_family, self.heading_label_point_size,
            bold=True, weight=75)
        self.classifier_label = self.add_label(
            self.central_widget, 'ClassifierLabel',
            self.classifier_label_geometry, self.label_stylesheet,
            self.heading_label_font, alignment=self.heading_label_alignment)
        self.prediction_label = self.add_label(
            self.central_widget, 'PredictionLabel',
            self.prediction_label_geometry, self.label_stylesheet,
            self.heading_label_font, alignment=self.heading_label_alignment)

        self.file_name_label = self.add_label(
            self.central_widget, 'FileNameLabel',
            self.file_name_label_geometry, self.file_name_label_stylesheet,
            self.detection_label_font, alignment=self.heading_label_alignment)

        # Add title label.
        self.title_label_font = self.get_font(
            self.default_font_family, self.title_label_point_size,
            bold=True, weight=75)
        self.vigilancia_title_label = self.add_label(
            self.central_widget, 'VigilanciaTitleLabel',
            self.vigilancia_title_label_geometry, self.label_stylesheet,
            self.title_label_font, alignment=self.heading_label_alignment)

        # Add plain text boxes for showing detection results.
        self.objects_detected_view = self.add_plain_text_widget(
            self.central_widget, 'ObjectesDetectedView',
            self.objects_detected_view_geometry,
            self.detection_view_stylesheet)
        self.events_detected_view = self.add_plain_text_widget(
            self.central_widget, 'EventsDetectedView',
            self.events_detected_view_geometry,
            self.detection_view_stylesheet)
        self.activity_detected_view = self.add_plain_text_widget(
            self.central_widget, 'ActivityDetectedView',
            self.activity_detected_view_geometry,
            self.detection_view_stylesheet)

    def raise_ui_components(self):
        # Raise all components on main UI.
        self.alert_window.raise_()
        self.video_window.raise_()
        self.fps_bar.raise_()
        self.object_detection_slider.raise_()
        self.event_detection_slider.raise_()
        self.abnormal_activity_slider.raise_()
        self.start_button.raise_()
        self.file_selection_button.raise_()
        self.classifier_label.raise_()
        self.prediction_label.raise_()
        self.object_detection_label.raise_()
        self.event_detection_label.raise_()
        self.abnormal_activity_label.raise_()
        self.file_name_label.raise_()
        self.date_time_label.raise_()
        self.objects_detected_view.raise_()
        self.events_detected_view.raise_()
        self.activity_detected_view.raise_()
        self.vigilancia_title_label.raise_()

    def setup_main_window_and_status_bar(self):
        self.main_window.setCentralWidget(self.central_widget)
        self.statusbar = self.qt.get_statusbar(self.main_window)
        self.qt.set_obj_name(self.statusbar, 'StatusBar')
        self.main_window.setStatusBar(self.statusbar)

    def retranslate_ui(self):
        # Set content of various UI components.
        self.qt.set_window_title(
            self.main_window, "MainWindow", "Vigilancia", None)
        self.qt.set_obj_text(self.start_button, "MainWindow", "Start", None)
        self.qt.set_obj_text(
            self.object_detection_label, "MainWindow", "Object Detection",
            None)
        self.qt.set_obj_text(
            self.event_detection_label, "MainWindow", "Event Detecion", None)
        self.qt.set_obj_text(
            self.abnormal_activity_label, "MainWindow", "Abnormal Activity",
            None)
        self.qt.set_obj_text(
            self.classifier_label, "MainWindow", "Classifiers", None)
        self.qt.set_obj_text(
            self.prediction_label, "MainWindow", "Predictions", None)
        self.qt.set_obj_text(
            self.vigilancia_title_label, "MainWindow", "Vigilancia", None)
        self.qt.set_obj_text(
            self.file_name_label, "MainWindow", "stream / file name", None)
        self.qt.set_obj_text(
            self.file_selection_button, "MainWindow", "Select file to stream",
            None)
        self.qt.set_obj_text(
            self.date_time_label, "MainWindow", "Today\'s date and time",
            None)
        self.qt.set_obj_plain_text(
            self.events_detected_view, "MainWindow", "Event", None)
        self.qt.set_obj_plain_text(
            self.objects_detected_view, "MainWindow", "Objects", None)
        self.qt.set_obj_plain_text(
            self.activity_detected_view, "MainWindow", "Activity", None)

    def object_detection_slider_value_changed(self):
        value = self.object_detection_slider.value()
        if value == 1:
            self.detector.enable_yolo_detection()
        else:
            self.detector.disable_yolo_detection()

    def event_detection_slider_value_changed(self):
        value = self.event_detection_slider.value()
        if value == 1:
            self.detector.enable_event_detection()
        else:
            self.detector.disable_event_detection()

    def abnormal_activity_slider_value_changed(self):
        value = self.abnormal_activity_slider.value()
        if value == 1:
            self.detector.enable_unusual_activity_detection()
        else:
            self.detector.disable_unusual_activity_detection()

    def connect_elements_to_callback(self):
        self.qt.connect_obj_event(
            self.object_detection_slider, 'valueChanged(int)', 
            self.object_detection_slider_value_changed)
        self.qt.connect_obj_event(
            self.event_detection_slider, 'valueChanged(int)', 
            self.event_detection_slider_value_changed)
        self.qt.connect_obj_event(
            self.abnormal_activity_slider, 'valueChanged(int)', 
            self.abnormal_activity_slider_value_changed)

    def create_application(self):
        self.create_ui_components()
        self.raise_ui_components()
        self.setup_main_window_and_status_bar()
        self.retranslate_ui()
        self.connect_elements_to_callback()
        self.qt.connect_slots_by_name(self.main_window)
        self.main_window.show()

    def start_app(self):
        return self.app.exec_()
