from threading import Thread
from yt_dlp import YoutubeDL
from appdirs import user_data_dir
from ModifiedUi import ModifiedUi
import json
import os


class EasyYTDLEngine(YoutubeDL, Thread):
    def __init__(self, MainWindow):
        super().__init__()

        self.ui = ModifiedUi(MainWindow)
        self.MainWindow = MainWindow
        self.download_path = ''
        self.ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'progress_hooks': [self.update_progress],
        }

        self.URL = []
        self.old_video_id = None
        self.format_type = 'mp4'
        self._finished_downloads = 0
        self.read_download_path()

    def check_if_empty_download_path(self, max_attempts=5):
        if self.download_path == '':
            attempt = 1
            while attempt <= max_attempts:
                self.download_not_found_msg_box(self.MainWindow)
                if self.download_path != '':
                    break
                attempt += 1
                if attempt > max_attempts:
                    self.ui.too_many_tries_msg(self.MainWindow)

    def read_download_path(self):
        user_profile_env = os.environ.get('USERPROFILE')
        json_file = os.path.join(
            user_profile_env, 'AppData', 'Local', 'Nupi', 'Easy YouTube Downloader', 'data', 'location.json'
        )
        try:
            with open(json_file, "r") as json_data:
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
        self.ui.enlarge_progress_bar()
        with YoutubeDL(self.ydl_opts) as ydl:
            ydl.download(self.URL)
        self.URL = []
        self.ui.shrink_progress_bar()
        self.update_downloads_label()

    def download_links(self):
        t = Thread(target=self.threaded_download)
        t.start()

    def append_new_links(self):
        self.URL.append(self.ui.get_entry_text())
        self.ui.clear_entry_text()
        self.update_downloads_label()

    def ydl_opts_mp3(self):
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
        if self.format_type != 'mp4':
            self.format_type = 'mp4'
        self.ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
            'progress_hooks': [self.update_progress],
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s'
        }

    def ydl_opts_webm(self):
        # TODO add progress_hooks to webm
        if self.format_type != 'webm':
            self.format_type = 'webm'
        self.ydl_opts = {
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s'
        }

    def empty_list(self):
        try:
            self.URL.clear()
            self.update_downloads_label()
        except IndexError:
            pass

    def clear_latest(self):
        try:
            self.URL.pop()
            self.update_downloads_label()
        except IndexError:
            pass

    def update_progress(self, video):
        try:
            descargado, total = video.get('downloaded_bytes', 0), video.get('total_bytes_estimate', 1)
            porcentaje = int((descargado / total) * 100)

            if porcentaje >= 101:
                self.ui.set_progressbar_value(porcentaje - 1)
            else:
                self.ui.set_progressbar_value(porcentaje)

            self.video_id_checker(video)
            self.update_downloads_label()
        except KeyError:
            pass

    def update_downloads_label(self):
        if len(self.URL) <= 0:
            self._finished_downloads = 0
            self.ui.set_no_active_downloads_label()
        else:
            self.ui.set_active_downloads_label(self._finished_downloads, len(self.URL))

    def select_download_path(self):
        path = self.ui.ask_for_directory()
        data = {'path': path}
        data_dir = user_data_dir("Easy YouTube Downloader", "Nupi")
        data_folder = os.path.join(data_dir, "data")
        os.makedirs(data_folder, exist_ok=True)
        location_file_path = os.path.join(data_folder, "location.json")
        with open(location_file_path, "w") as file:
            json.dump(data, file, indent=4)
        self.read_download_path()

    def video_id_checker(self, video):
        if 'info_dict' in video and 'id' in video['info_dict']:
            video_id = video['info_dict']['id']
            if video_id != self.old_video_id:
                self.old_video_id = video_id
                self._finished_downloads += 1

    def download_not_found_msg_box(self, MainWindow):
        if self.download_path == '':
            self.ui.download_not_found_msg(MainWindow)
            self.select_download_path()

    def open_format_window(self):
        self.ui.open_ui_format_window()
