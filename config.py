import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "8125761940:AAEnznDYk7eoDXYXz_7PG2mzrliPKXkQv78"
    # Telegram API ki ID
    API_ID = 29940750
    # Telegram API ki hash key
    API_HASH = "33412ad3b366ca991309d1bcbb472c32"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '7618270428'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://mcacourse01:nEDXm37rW8u1VKUe@cluster0.dt5hh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002252455050
    # Authentication log channel ki ID
    AUTH_LOG = -1002252455050
    # Hit log channel ki ID
    HIT_LOG = -1002252455050
    # DRM dump channel ki ID
    DRM_DUMP = -1002252455050
    # Main channel ki ID
    CHANNEL = -1002252455050
    # Channel ka link
    CH_URL = "https://t.me/skillwithoreo"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/Deepa4455"
    # Thumbnail image ka URL
    THUMB_URL = "https://te.legra.ph/file/11366447de3410810a383-d29ae883f7add39f2a.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

