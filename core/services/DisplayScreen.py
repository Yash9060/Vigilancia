"""Class that generates and handles events on Vigilancia UI."""
import time
import collections

from core.services import SuspicionDetection
from core.platform.opencv import VideoStream
from core.platform.qt import qt4
import vgconf

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
        self.video_window_geometry = (30, 110, 400, 310)
        self.alert_window_stylesheet_red = (
            'background-color: rgba(186, 46, 46, 220)')
        self.alert_window_stylesheet_white = (
            'background-color: white')
        self.alert_window_geometry = (20, 100, 420, 330)

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
        self.firearm_detection_slider_geometry = (700, 210, 31, 20)
        self.event_detection_slider_geometry = (700, 280, 31, 20)
        self.abnormal_activity_slider_geometry = (700, 390, 31, 20)

        self.push_button_stylesheet = ('QPushButton:hover {\n'
            'background-color: rgba(255, 255, 255, 50);\n'
            '}\n'
            'QPushButton {\n'
            'color: white;\n'
            'background-color: rgba(0, 0, 0, 0);\n'
            'border: 1px solid white;\n'
            'border-radius: 5px;\n'
            '}')
        self.push_button_point_size = 11
        self.start_button_text = 'Start'
        self.start_button_geometry = (340, 440, 90, 34)
        self.clear_button_text = 'Clear'
        self.clear_button_geometry = (250, 440, 80, 34)
        self.file_selection_button_text = 'Select file to stream'
        self.file_selection_button_geometry = (30, 440, 210, 34)
        self.file_selection_filter = 'AVI (*.avi);;MP4 (*.mp4);;MKV (*.mkv)'
        self.file_selection_dialog_stylesheet = ('color: lightgrey;')

        self.default_font_family = 'DejaVu Sans Mono'

        self.label_color = 'white'
        self.label_stylesheet = ('color: %s;\n'
            'background-color: rgba(0, 0, 0, 0);' % self.label_color)

        self.fps_bar_label_geometry = (325, 65, 118, 20)
        self.fps_bar_label_text = 'FPS Meter'
        self.detection_label_point_size = 11
        self.object_detection_label_text = 'Object Detection' 
        self.object_detection_label_geometry = (510, 170, 171, 20)
        self.firearm_detection_label_text = 'Firearm Detection' 
        self.firearm_detection_label_geometry = (510, 210, 171, 20)
        self.event_detection_label_text = 'Event Detection'
        self.event_detection_label_geometry = (510, 280, 171, 20)
        self.abnormal_activity_label_text = 'Abnormal Activity'
        self.abnormal_activity_label_geometry = (510, 390, 171, 20)
        self.date_time_label_text = 'Today\'s date and time'
        self.date_time_label_geometry = (20, 80, 271, 20)
        self.datetime_format = '%a %b %d %H:%M:%S %Z %Y'

        self.file_name_label_stylesheet = ('color: %s;\n'
            'background-color: rgba(0, 30, 58, 150);' % self.label_color)
        self.file_name_label_text = 'stream / file name'
        self.file_name_label_geometry = (30, 110, 401, 20)

        self.heading_label_point_size = 13
        self.heading_label_alignment = self.qt.center_alignment
        self.classifier_label_geometry = (490, 100, 221, 18)
        self.classifier_label_text = 'Classifier'
        self.prediction_label_geometry = (770, 100, 221, 18)
        self.prediction_label_text = 'Predictions'

        self.detection_view_stylesheet = ('background-color: '
            'rgba(0, 0, 0, 0);\n'
            'color: white;\n'
            'border: 1px solid white;\n'
            'border-radius: 4px;')
        self.objects_detected_view_text = 'Objects'
        self.objects_detected_view_geometry = (790, 170, 231, 84)
        self.events_detected_view_text = 'Events'
        self.events_detected_view_geometry = (790, 280, 231, 84)
        self.activity_detected_view_text = 'Activity'
        self.activity_detected_view_geometry = (790, 390, 231, 84)

        self.title_label_point_size = 28
        self.vigilancia_title_label_text = 'Vigilancia'
        self.vigilancia_title_label_geometry = (8, 9, 1031, 51)

        # Whether stream / video is playing or not.
        self.streamer = VideoStream.VideoStream()
        self.is_stream_on = False
        self.FPS_rate = 25

        # Timers
        self.stream_timer = self.qt.get_timer()
        self.datetime_timer = self.qt.get_timer()
        self.fps_bar_timer = self.qt.get_timer()
        self.classifier_timer = self.qt.get_timer()
        self.alert_timer = self.qt.get_timer()

        # Set timer timeout time.
        self.video_timer_update_rate = (1000 / self.FPS_rate)
        self.fps_bar_timer_update_rate = 1000
        self.datetime_timer_update_rate = 1000
        self.classifier_timer_update_rate = 1000
        self._flash_alert_update_rate = 250

        # How many time alert should be flashed.
        self.alert_count = 0

        # FPS calculation parameters.
        self.elapsed = 0
        self.stream_start_time = time.time()

        # Name of the selected file to stream. Default None.
        self.selected_stream_name = None

        # Predictions.
        self.objects_detector_prediction = []
        self.event_detector_prediction = []
        self.activity_detector_prediction = None

        # Audio alert file.
        self.alert_beep = self.qt.get_phonon_media_source(
            vgconf.ALERT_BEEP_FILE)
        self.is_beep_playing = False

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
            self, parent, name, geometry, stylesheet,
            font=None, alignment=None):
        obj = self.qt.get_label(parent)
        self.qt.set_obj_name(obj, name)
        self.qt.set_obj_geometry(obj, geometry)
        self.qt.set_obj_stylesheet(obj, stylesheet)
        if font:
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

    def get_timer(self, callback, timer_rate):
        timer = self.qt.get_timer()
        self.qt.connect_obj_event(timer, 'timeout()', callback)
        timer.start(timer_rate)
        return timer

    def get_file_dialog(self, filters):
        file_dialog = self.qt.get_file_dialog(self.central_widget, filters)
        self.qt.set_obj_stylesheet(
            file_dialog, self.file_selection_dialog_stylesheet)
        return file_dialog

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
        self.video_window = self.add_label(
            self.central_widget, 'VideoWindow', self.video_window_geometry,
            self.video_window_stylesheet)
        self.qt.set_label_scaled_content(self.video_window, True)
        self.alert_window = self.add_graphics_view(
            self.central_widget, 'AlertWindow', self.alert_window_geometry,
            self.alert_window_stylesheet_white, False)

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
        self.firearm_detection_slider = self.add_slider(
            self.central_widget, 'FirearmDetectionSlider',
            self.firearm_detection_slider_geometry, self.slider_stylesheet,
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
        self.clear_button = self.add_push_button(
            self.central_widget, 'ClearButton', self.clear_button_geometry,
            self.push_button_stylesheet, self.button_font)
        self.file_selection_button = self.add_push_button(
            self.central_widget, 'FileSelectionButton',
            self.file_selection_button_geometry, self.push_button_stylesheet,
            self.button_font)
        self.file_dialog = self.get_file_dialog(self.file_selection_filter)

        # Add labels.
        self.detection_label_font = self.get_font(
            self.default_font_family, self.detection_label_point_size)
        self.object_detection_label = self.add_label(
            self.central_widget, 'ObjectDetectionLabel',
            self.object_detection_label_geometry, self.label_stylesheet,
            self.detection_label_font)
        self.firearm_detection_label = self.add_label(
            self.central_widget, 'FirearmDetectionLabel',
            self.firearm_detection_label_geometry, self.label_stylesheet,
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
        self.fps_bar_label = self.add_label(
            self.central_widget, 'FPSBarLabel', self.fps_bar_label_geometry,
            self.label_stylesheet, self.detection_label_font)

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

        # Audio player.
        self.alert_beep_player = self.qt.get_phonon_audio_player(
            self.central_widget)
        self.alert_beep_player.setCurrentSource(self.alert_beep)

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
        self.firearm_detection_label.raise_()
        self.event_detection_label.raise_()
        self.abnormal_activity_label.raise_()
        self.fps_bar_label.raise_()
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
            self.main_window, 'MainWindow',
            self.vigilancia_title_label_text, None)
        self.qt.set_obj_text(
            self.start_button, 'MainWindow', self.start_button_text, None)
        self.qt.set_obj_text(
            self.clear_button, 'MainWindow', self.clear_button_text, None)
        self.qt.set_obj_text(
            self.object_detection_label, 'MainWindow',
            self.object_detection_label_text, None)
        self.qt.set_obj_text(
            self.firearm_detection_label, 'MainWindow',
            self.firearm_detection_label_text, None)
        self.qt.set_obj_text(
            self.event_detection_label, 'MainWindow',
            self.event_detection_label_text, None)
        self.qt.set_obj_text(
            self.abnormal_activity_label, 'MainWindow',
            self.abnormal_activity_label_text, None)
        self.qt.set_obj_text(
            self.fps_bar_label, 'MainWindow',
            self.fps_bar_label_text, None)
        self.qt.set_obj_text(
            self.classifier_label, 'MainWindow',
            self.classifier_label_text, None)
        self.qt.set_obj_text(
            self.prediction_label, 'MainWindow',
            self.prediction_label_text, None)
        self.qt.set_obj_text(
            self.vigilancia_title_label, 'MainWindow',
            self.vigilancia_title_label_text, None)
        self.qt.set_obj_text(
            self.file_name_label, 'MainWindow', self.file_name_label_text, None)
        self.qt.set_obj_text(
            self.file_selection_button, 'MainWindow',
            self.file_selection_button_text, None)
        self.qt.set_obj_text(
            self.date_time_label, 'MainWindow', self.date_time_label_text, None)
        self.qt.set_obj_plain_text(
            self.events_detected_view, 'MainWindow',
            self.events_detected_view_text, None)
        self.qt.set_obj_plain_text(
            self.objects_detected_view, 'MainWindow',
            self.objects_detected_view_text, None)
        self.qt.set_obj_plain_text(
            self.activity_detected_view, 'MainWindow',
            self.activity_detected_view_text, None)

    def _start_alert(self):
        self._start_visual_alert()
        self._start_audio_alert()

    def _flash_alert(self):
        self.alert_count -= 1
        if self.alert_count == 0:
            self.alert_timer.stop()
        alert_stylsheet = self.alert_window_stylesheet_white
        if self.alert_count % 2:
            alert_stylsheet = self.alert_window_stylesheet_red
        self.qt.set_obj_stylesheet(self.alert_window, alert_stylsheet)
        self.alert_window.update()

    def _start_visual_alert(self):
        if self.alert_count == 0:
            self.alert_timer = self.get_timer(
                self._flash_alert, self._flash_alert_update_rate)
        self.alert_count = vgconf.DEFAULT_ALERT_FLASH_COUNT

    def _audio_alert_finished(self):
        self.is_beep_playing = False

    def _start_audio_alert(self):
        if self.is_beep_playing:
            return
        self.is_beep_playing = True
        self.alert_beep_player.stop()
        self.alert_beep_player.play()

    def _object_detection_slider_value_changed(self):
        value = self.object_detection_slider.value()
        if value == 1:
            self.detector.enable_yolo_detection()
        else:
            self.detector.disable_yolo_detection()

    def _firearm_detection_slider_value_changed(self):
        value = self.firearm_detection_slider.value()
        if value == 1:
            self.detector.enable_firearm_detection()
        else:
            self.detector.disable_firearm_detection()

    def _event_detection_slider_value_changed(self):
        value = self.event_detection_slider.value()
        if value == 1:
            self.detector.enable_event_detection()
        else:
            self.detector.disable_event_detection()
            self._update_detected_events('Events')

    def _abnormal_activity_slider_value_changed(self):
        value = self.abnormal_activity_slider.value()
        if value == 1:
            self.detector.enable_unusual_activity_detection()
        else:
            self.detector.disable_unusual_activity_detection()
            self._update_detected_activity('Activity')

    def _update_detected_objects(self, objects_prediction):
        if self.detector.is_yolo_on or self.detector.is_firearm_detector_on:
            parsed_objects = [p['label'] for p in objects_prediction]
            parsed_objects_dict = collections.Counter(parsed_objects)
            detected_suspicious_objects = False
            objects = ''

            for (obj, count) in parsed_objects_dict.items():
                objects += '%s (%d)\n' % (obj, count)
                if obj in vgconf.SUSPICIOUS_OBJECTS_LIST:
                    detected_suspicious_objects = True

            self.objects_detected_view_text = objects
            self.qt.set_obj_plain_text(
                self.objects_detected_view, 'MainWindow',
                self.objects_detected_view_text, None)

            # Start alert if suspicious object is detected.
            if detected_suspicious_objects:
                self._start_alert()
        else:
            self.objects_detected_view_text = 'Objects'
            self.qt.set_obj_plain_text(
                self.objects_detected_view, 'MainWindow',
                self.objects_detected_view_text, None)

    def _update_detected_events(self, events_prediction):
        if self.detector.is_event_detector_on:
            events = ', '.join(events_prediction)
            self.events_detected_view_text = events
            self.qt.set_obj_plain_text(
                self.events_detected_view, 'MainWindow',
                self.events_detected_view_text, None)

            detected_suspicious_events = False
            for event in events_prediction:
                if event in vgconf.SUSPICIOUS_EVENTS_LIST:
                    detected_suspicious_events = True

            if detected_suspicious_events:
                self._start_alert()
        else:
            self.events_detected_view_text = events_prediction
            self.qt.set_obj_plain_text(
                self.events_detected_view, 'MainWindow',
                self.events_detected_view_text, None)

    def _update_detected_activity(self, activity_prediction):
        if self.detector.is_activity_detector_on:
            self.activity_detected_view_text = activity_prediction
            self.qt.set_obj_plain_text(
                self.activity_detected_view, 'MainWindow',
                self.activity_detected_view_text, None)

            if activity_prediction == vgconf.ABNORMAL_ACTIVITY:
                self._start_alert()
        else:
            self.activity_detected_view_text = activity_prediction
            self.qt.set_obj_plain_text(
                self.activity_detected_view, 'MainWindow',
                self.activity_detected_view_text, None)

    def _update_stream_name_label(self):
        filename = 'webcam'
        if self.selected_stream_name:
            filename = self.selected_stream_name.split('/')[-1]
        self.qt.set_obj_text(
            self.file_name_label, 'MainWindow', filename, None)

    def _update_fps_rate(self):
        if self.elapsed % 5 == 0:
            self.FPS_rate = (
                self.elapsed / (time.time() - self.stream_start_time))

    def _update_fps_bar(self):
        self.qt.set_obj_property(self.fps_bar, 'value', self.FPS_rate)

    def _update_video_window(self):
        if self.streamer.is_next_frame_available():
            frame = self.streamer.read_next_frame()
            self.detector.detect(frame)
            frame = self.detector.plot_objects(frame)
            frame = self.streamer.qt_preprocess(frame)
            self.qt.set_label_img(self.video_window, frame)
            # Calculate FPS rate.
            self._update_fps_rate()
            self.elapsed += 1

    def _update_predictions(self):
        self.objects_detector_prediction = self.detector.get_yolo_prediction()
        self.firearm_detector_prediction = (
            self.detector.get_firearm_detector_prediction())
        self.activity_detector_prediction = (
            self.detector.get_activity_detector_prediction())
        self.event_detector_prediction = (
            self.detector.get_event_detector_prediction())

        self.detected_objects = []
        if self.objects_detector_prediction:
            self.detected_objects.extend(self.objects_detector_prediction)
        if self.firearm_detector_prediction:
            self.detected_objects.extend(self.firearm_detector_prediction)

        self._update_detected_objects(self.detected_objects)
        if self.activity_detector_prediction:
            self._update_detected_activity(self.activity_detector_prediction)
        if self.event_detector_prediction:
            self._update_detected_events(self.event_detector_prediction)

    def _start_streaming(self):
        if not self.streamer.is_closed:
            self.streamer.close()
        self.streamer = VideoStream.VideoStream(self.selected_stream_name)
        # Get timers.
        self.stream_timer = self.get_timer(
            self._update_video_window, self.video_timer_update_rate)
        self.fps_bar_timer = self.get_timer(
            self._update_fps_bar, self.fps_bar_timer_update_rate)
        self.classifier_timer = self.get_timer(
            self._update_predictions, self.classifier_timer_update_rate)
        # Parameters for updating FPS rate.
        self.stream_start_time = time.time()
        self.elapsed = 0

    def _stop_streaming(self):
        # Stop timers.
        self.stream_timer.stop()
        self.fps_bar_timer.stop()
        self.classifier_timer.stop()
        # Close stream.
        self.streamer.close()
        self.video_window.clear()

    def _start_button_clicked(self):
        if not self.is_stream_on:
            self.is_stream_on = not self.is_stream_on
            self.start_button_text = 'Stop'
            self.qt.set_obj_text(
                self.start_button, 'MainWindow', self.start_button_text, None)
            self._update_stream_name_label()
            self._start_streaming()
        else:
            self.is_stream_on = not self.is_stream_on
            self.start_button_text = 'Start'
            self.qt.set_obj_text(
                self.start_button, 'MainWindow', self.start_button_text, None)
            self._stop_streaming()

    def _open_file_dialog(self):
        if self.file_dialog.exec_():
            filenames = self.file_dialog.selectedFiles()
            self.selected_stream_name = filenames[0]

    def _clear_stream(self):
        self.selected_stream_name = None
        self._update_stream_name_label()

    def _update_date_time(self):
        self.date_time_label_text = time.strftime(self.datetime_format)
        self.qt.set_obj_text(
            self.date_time_label, 'MainWindow', self.date_time_label_text, None)

    def _start_datetime_timer(self):
        self.datetime_timer = self.get_timer(
            self._update_date_time, self.datetime_timer_update_rate)

    def connect_elements_to_callback(self):
        self.qt.connect_obj_event(
            self.object_detection_slider, 'valueChanged(int)', 
            self._object_detection_slider_value_changed)
        self.qt.connect_obj_event(
            self.firearm_detection_slider, 'valueChanged(int)', 
            self._firearm_detection_slider_value_changed)
        self.qt.connect_obj_event(
            self.event_detection_slider, 'valueChanged(int)', 
            self._event_detection_slider_value_changed)
        self.qt.connect_obj_event(
            self.abnormal_activity_slider, 'valueChanged(int)', 
            self._abnormal_activity_slider_value_changed)
        self.qt.connect_obj_event(
            self.start_button, 'clicked()', self._start_button_clicked)
        self.qt.connect_obj_event(
            self.file_selection_button, 'clicked()', self._open_file_dialog)
        self.qt.connect_obj_event(
            self.clear_button, 'clicked()', self._clear_stream)
        self.qt.connect_obj_event(
            self.alert_beep_player, 'finished()', self._audio_alert_finished)

    def create_application(self):
        self.create_ui_components()
        self.raise_ui_components()
        self.setup_main_window_and_status_bar()
        self.retranslate_ui()
        self.connect_elements_to_callback()
        self.qt.connect_slots_by_name(self.main_window)
        self.main_window.show()

    def _close(self):
        self.stream_timer.stop()
        self.fps_bar_timer.stop()
        self.datetime_timer.stop()
        self.classifier_timer.stop()
        self.streamer.close()
        self.detector.close()

    def start_app(self):
        self._start_datetime_timer()
        self.qt.connect_obj_event(self.app, 'aboutToQuit()', self._close)
        return self.app.exec_()
