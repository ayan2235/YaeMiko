# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 13161347  # Get this value from my.telegram.org/apps
    API_HASH = "80157e31b41407507c6a7849113cc1d4"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgresql://Bot_followwho:6d1a6eb3e414d737afda6a214c5df43c48356bac@pw8.h.filess.io:5432/Bot_followwho"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002088557628
    MESSAGE_DUMP = -1002088557628

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Ayan:TnOx4mKnolqnOf5ZipysFsVg2FfyvvLRyI3srAn6qQjBUb8TjDJUTVfQ4CZM6fCR@cluster0.otxzq7c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Support chat and support ID
    SUPPORT_CHAT = "Noob_xd03"
    SUPPORT_ID = -1002082219534

    # Database name
    DB_NAME = "SupportDB"

    # Bot token
    TOKEN = "7168125411:AAHR-nRUc5C1k_xDDQ5bBPeCd3ftAo13h8M"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6515961910
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
