import os

user_profile = os.getenv('USERPROFILE')

PROGRAM_FOLDER = os.path.join(
    user_profile, 'AppData', 'Local', 'Nupi', 'Easy YouTube Downloader'
    )

LOCATION_JSON_PATH = os.path.join(
    PROGRAM_FOLDER, 'data', 'location.json'
)

LOGS_LOG_PATH = os.path.join(
    PROGRAM_FOLDER, 'logs', 'logs.log'
)
