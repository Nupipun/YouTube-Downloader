"""Modulo para leer y guardar archivos json"""
import json
import os
from threading import Thread
from yt_dlp import YoutubeDL
from appdirs import user_data_dir
from ModifiedUi import ModifiedUi


# TODO change download label when changing format
class EasyYTDLEngine(YoutubeDL, Thread):
    """Class that runs the download engine."""
    def __init__(self, MainWindow):
        super().__init__()

        self.ui_object = ModifiedUi(MainWindow)
        self.format_type = 'mp4'
        self.main_window = MainWindow
        self.download_path = ''
        self.ydl_opts = None
        self.ydl_opts_mp4()
        self.input_url = []
        self.old_video_id = None
        self._finished_downloads = 0
        self.read_download_path()

    def check_if_empty_download_path(self, max_attempts=5):
        """Method that checks if path stored in location.json is empty"""
        if self.download_path == '':
            attempt = 1
            while attempt <= max_attempts:
                self.download_not_found_msg_box(self.main_window)
                if self.download_path != '':
                    break
                attempt += 1
                if attempt > max_attempts:
                    self.ui_object.too_many_tries_msg(self.main_window)

    def read_download_path(self):
        """Method that reads the path from location.json"""
        user_profile_env = os.environ.get('USERPROFILE')
        json_file = os.path.join(
            user_profile_env, 'AppData', 'Local', 'Nupi',
            'Easy YouTube Downloader', 'data', 'location.json'
        )
        try:
            with open(json_file, "r", encoding='UTF-8') as json_data:
                data = json.load(json_data)
                self.download_path = data['path']
                self.check_if_empty_download_path()
                self.download_path = data['path']
        except FileNotFoundError:
            self.check_if_empty_download_path()
        finally:
            if self.format_type == 'mp3':
                self.ydl_opts_mp3()
            elif self.format_type == 'mp4':
                self.ydl_opts_mp4()
            elif self.format_type == 'webm':
                self.ydl_opts_webm()

    def threaded_download(self):
        """Method that downloads the inputted urls"""
        self.ui_object.enlarge_progress_bar()
        with YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(self.input_url)
        self.input_url = []
        self.ui_object.shrink_progress_bar()
        self.update_downloads_label()

    def download_links(self):
        """Method that initializes threaded_download method in a new thread"""
        t_1 = Thread(target=self.threaded_download)
        t_1.start()

    def append_new_links(self):
        """Method that inputs the current link in the entry."""
        self.input_url.append(self.ui_object.get_entry_text())
        self.ui_object.clear_entry_text()
        self.update_downloads_label()

    def ydl_opts_mp3(self):
        """
        Method that sets the self.ydl_opts attribute into the mp3 format
        """
        if self.format_type != 'mp3':
            self.format_type = 'mp3'
        self.ydl_opts = {
            'format': 'mp3/bestaudio/best',
            'progress_hooks': [self.update_progress],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s'
        }

    def ydl_opts_mp4(self):
        """
        Method that sets the self.ydl_opts attribute into the mp4 format
        """
        if self.format_type != 'mp4':
            self.format_type = 'mp4'
        self.ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'progress_hooks': [self.update_progress],
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s'
        }

    def ydl_opts_webm(self):
        """
        Method that sets the self.ydl_opts attribute into the webm format
        """
        if self.format_type != 'webm':
            self.format_type = 'webm'
        self.ydl_opts = {
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s',
            'progress_hooks': [self.update_progress],
        }

    def empty_list(self):
        """Method that clears the input_url attribute"""
        try:
            self.input_url.clear()
            self.update_downloads_label()
        except IndexError:
            pass

    def clear_latest(self):
        """Method that pops the latest url in the input_url attribute"""
        try:
            self.input_url.pop()
            self.update_downloads_label()
        except IndexError:
            pass

    def update_progress(self, video):
        """Method that updates the progressbar"""
        try:
            descargado, total = video.get(
                'downloaded_bytes', 0), video.get('total_bytes_estimate', 1)
            porcentaje = int((descargado / total) * 100)

            if porcentaje >= 101:
                self.ui_object.set_progressbar_value(porcentaje - 1)
            else:
                self.ui_object.set_progressbar_value(porcentaje)

            self.video_id_checker(video)
            self.update_downloads_label()
        except KeyError:
            pass

    def update_downloads_label(self):
        """Method that updates the active downloads label"""
        if len(self.input_url) <= 0:
            self._finished_downloads = 0
            self.ui_object.set_no_active_downloads_label()
        else:
            self.ui_object.set_active_downloads_label(
                self._finished_downloads, len(self.input_url))

    def select_download_path(self):
        """Method to choose a new download path"""
        path = self.ui_object.ask_for_directory()
        data = {'path': path}
        data_dir = user_data_dir("Easy YouTube Downloader", "Nupi")
        data_folder = os.path.join(data_dir, "data")
        os.makedirs(data_folder, exist_ok=True)
        location_file_path = os.path.join(data_folder, "location.json")
        with open(location_file_path, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4)
        self.read_download_path()

    def video_id_checker(self, video):
        """Method that checks if the new video id is different the old one"""
        if 'info_dict' in video and 'id' in video['info_dict']:
            video_id = video['info_dict']['id']
            if video_id != self.old_video_id:
                self.old_video_id = video_id
                self._finished_downloads += 1

    def download_not_found_msg_box(self, main_window):
        """Method that calls a download not found msg box"""
        if self.download_path == '':
            self.ui_object.download_not_found_msg(main_window)
            self.select_download_path()

    def open_format_window(self):
        """Method that opens the format window"""
        self.ui_object.open_ui_format_window()
