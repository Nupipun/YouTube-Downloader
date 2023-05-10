from DownloadEngine import EasyYTDLEngine
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os

# TODO probably fix DownloadEngine.py code at some point.
if __name__ == '__main__':
    def start_logging(path):
        try:
            sys.stdout = open(path, 'w')
            sys.stderr = open(path, 'a')
        except FileNotFoundError:
            os.makedirs(app_data_folder)
            start_logging(logs_path)

    user_profile = os.getenv('USERPROFILE')
    app_data_folder = os.path.join(user_profile, 'AppData', 'Local', 'Nupi', 'Easy YouTube Downloader', 'logs')
    logs_path = os.path.join(app_data_folder, 'logs.log')

    # Start logging to file DO NOT REMOVE IF LOGGING IS NOT PRESENT PROGRAM DOES NOT WORK
    start_logging(logs_path)

    # Create main application and window object.
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    # Apart from the methods required to run the engine, it also runs the ui. No need to create a UI object.
    eng = EasyYTDLEngine(MainWindow)
    MainWindow.show()

    # Button functions
    eng.ui.enter_link_button.clicked.connect(eng.append_new_links)
    eng.ui.download_links_button.clicked.connect(eng.download_links)
    eng.ui.empty_list.clicked.connect(eng.empty_list)
    eng.ui.clear_latest.clicked.connect(eng.clear_latest)
    eng.ui.actionChange_download_location.triggered.connect(eng.select_download_path)
    eng.ui.get_specific_format_button.clicked.connect(eng.open_format_window)
    eng.ui.mp3_button_func(eng.ydl_opts_mp3)
    eng.ui.mp4_button_func(eng.ydl_opts_mp4)
    eng.ui.webm_button_func(eng.ydl_opts_webm)

    sys.exit(app.exec_())