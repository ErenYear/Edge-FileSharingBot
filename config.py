#(©)@EdgeBots

import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6020240248:AAG35b4X1-43zPmkOIgB7p6DzSX85sqIl9o")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7414019"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d463ed3d695f5cd4164029405ad8388e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001987257151"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1350488685"))
MAIN_CHANNEL = (os.environ.get("OWNER_ID", "Anime_Edge"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://owais:owais2006@cluster0.xykjk8j.mongodb.net/?")
DB_NAME = os.environ.get("DATABASE_NAME", "Edgefilebot")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI'm here to help! I keep private files in a special channel and share links so others can access them effortlessly.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5910975386").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", """<b>Hold on, {mention}!\n
You're missing out on some serious action.\n
To unleash my full power and access all the files, you've got to join both of our electrifying channels below:</b>""")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please avoid direct messages. I'm here solely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)