import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("1223411843:AAFa7MaLKX43TD6uTm8IIydI3a8Qlv8zxwc", )
    # The Telegram API things
    API_ID = int(os.environ.get("1242353", ))
    API_HASH = os.environ.get("b3a18ad8cab67c73ee21881c5b76a7e1",)
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    VIDEO_FORMATS = ["mp4", "mkv", "mov", "m4v", "avi", "unknown_video"]
    AUDIO_FORMATS = ["mp3", "flac", "m4a", "wav"]
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("391342978",))
    ADMINS = int(os.environ.get("391342978", ))
    SESSION_NAME = "URLUPLOADERBOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("mongodb+srv://shahanu7034:shahanu7034@cluster0.tg83ar4.mongodb.net/?retryWrites=true&w=majority",)
    DATABASE_NAME = os.environ.get("cluster0",)
    MAX_RESULTS = "50"
    #update channel
    UPDATE_CHANNEL = os.environ.get("-1001678913761",)
    UPDATES_CHANNEL = os.environ.get("-1001678913761",)
    #log channel
    LOG_CHANNEL = os.environ.get("-1001870858774")
    
