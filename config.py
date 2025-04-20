import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("7129963475:AAH3Ak4FgNsmC01gwSeDfjfrq_yqKvkJPBA", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("26745242", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("e9b17e0b329fa1876b8d92922bf0c00b", "")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("@nooneisperfect5", "7010115105"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "sansavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
