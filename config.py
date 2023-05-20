#!/usr/bin/env python3
# Copyright (C) @armoviechat
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'auto-filter-bot-v3')
API_ID = int(environ['API_ID'15056052])
API_HASH = environ['API_HASH'87f3fa0ad63a2b9dc87f2fd6def04970]
BOT_TOKEN = environ['BOT_TOKEN'5787728341:AAG2eBIQZfLw6rQH0eDuy7wytbUHwQsVsmY]

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", "1001607950761"))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "5009480460").split())
DB_URL = os.environ.get("DATABASE_URI", "mongodb+srv://Olammovie:LfbR3H731Q8pbtSl@cluster0.tipaq8j.mongodb.net/?retryWrites=true&w=majority")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('FORCES_SUB')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
DEV_CHANNEL = "https://t.me/armoviechat"

# MongoDB information
DATABASE_URI = environ['DATABASE_URI'mongodb+srv://Olammovie:LfbR3H731Q8pbtSl@cluster0.tipaq8j.mongodb.net/?retryWrites=true&w=majority]
DATABASE_NAME = environ['DATABASE_NAME'olammovie]
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Dora_files')

# Messages
default_start_msg = "𝖸𝗈...𝖸𝗈... Hey I'm DORA FILMS 💖

𝖨'𝗆 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖠𝗎𝗍𝗈-𝖥𝗂𝗅𝗍𝖾𝗋 𝖡𝗈𝗍 𝖸𝗈𝗎 𝖢𝖺𝗇 𝖴𝗌𝖾 𝖬𝖾 𝖠𝗌 𝖠 𝖠𝗎𝗍𝗈-𝖿𝗂𝗅𝗍𝖾𝗋 𝗂𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉

𝖨𝗍𝗌 𝖤𝖺𝗌𝗒 𝖳𝗈 𝖴𝗌𝖾 𝖬𝖾; 𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇, 

𝖳𝗁𝖺𝗍𝗌 𝖠𝗅𝗅, 𝗂 𝗐𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖳𝗁𝖾𝗋𝖾...🤓🤪

⚠️𝖬𝗈𝗋𝖾 𝖧𝖾𝗅𝗉 𝖧𝗂𝗍 /help

😎 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖻𝗒 @armoviechat"


Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "Dorafilms")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
