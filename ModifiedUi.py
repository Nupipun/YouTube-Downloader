from ui import Ui_MainWindow
from formatWindow import Ui_formatWindow
from video_or_playlist_window import Ui_playlist_or_video_window
from PyQt5 import QtCore, QtWidgets
import sys


class ModifiedUi(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.dialog = QtWidgets.QFileDialog()
        self.msg = QtWidgets.QMessageBox()
        self.format_window = QtWidgets.QMainWindow()
        self.format_ui = Ui_formatWindow()
        self.format_ui.setupUi(self.format_window)
        self.playlist_window = QtWidgets.QMainWindow()
        self.playlist_ui = Ui_playlist_or_video_window()
        self.playlist_ui.setupUi(self.playlist_window)

    def __str__(self):
        return f'ModifiedUi({Ui_MainWindow})'

    def mp3_button_func(self, func):
        self.format_ui.mp3Button.clicked.connect(func)

    def mp4_button_func(self, func):
        self.format_ui.mp4Button.clicked.connect(func)

    def webm_button_func(self, func):
        self.format_ui.webmButton.clicked.connect(func)

    def open_ui_format_window(self):
        self.format_window.show()

    def shrink_progress_bar(self):
        self.progress_bar.setGeometry(QtCore.QRect(110, 200, 0, 21))

    def enlarge_progress_bar(self):
        self.progress_bar.setGeometry(QtCore.QRect(110, 200, 411, 21))

    def get_entry_text(self):
        output_text = self.link_entry.text()
        return output_text

    def clear_entry_text(self):
        self.link_entry.setText("")

    def set_progressbar_value(self, value):
        if value >= 100:
            self.progress_bar.setValue(100)
        else:
            self.progress_bar.setValue(value)

    def set_no_active_downloads_label(self):
        self.remaining_download_links_label.setText(
            "Descargas: no active downloads"
            )

    def set_active_downloads_label(self, completed, total):
        self.remaining_download_links_label.setText(
            f"Descargas: {completed}/{total}"
            )

    def ask_for_directory(self):
        path = self.dialog.getExistingDirectory()
        return path

    def download_not_found_msg(self, MainWindow):
        self.msg.about(
            MainWindow,
            "Info",
            "Download path was not found. Please select a new one."
            )

    def too_many_tries_msg(self, MainWindow):
        self.msg.about(
            MainWindow,
            "Info",
            "Too many tries reached. Exiting program."
            )

    def set_selected_format_label(self, format):
        self.active_format_label.setText(
            f"Active download format: {format}"
        )

    def open_ui_playlist_window(self, MainWindow):
        self.msg.about(
            MainWindow,
            "Info",
            ("Playlist detected. "
             "Choose whether you want a single video or the whole playlist.")
        )
        self.playlist_window.show()

    def video_button_func(self, func):
        self.playlist_ui.individual_video_button.clicked.connect(func)

    def playlist_button_func(self, func):
        self.playlist_ui.playlist_button.clicked.connect(func)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = ModifiedUi(main_window)
    main_window.show()
    ui.open_ui_playlist_window(main_window)
    sys.exit(app.exec_())
