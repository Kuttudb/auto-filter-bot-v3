#!/usr/bin/env python3
# Copyright (C) @ZauteKm
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
# Bot information
SESSION = 'betterAutoFilterBot'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:BetterAutoFilterBot-zyx57W2v1u123ew11'
USERBOT_STRING_SESSION = 'BetterAutoFilterBot'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 987654321]
CHANNELS = [-10012345678, -100987654321, 'tgbotsproject']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb://[BetterAutoFilterBot:BetterAutoFilterBot@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'LuciferMoringstar_Robot'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Messages
START_MSG = """
**Hi, I'm [auto-filter-bot-v3](https://github.com/ZauteKm/auto-filter-bot-v3)** or you can call me as **Media Inline Search Bot**\n\nHere you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = 'Please join @.... to use this bot'
