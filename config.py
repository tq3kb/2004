from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "6224624072:AAHMkg0GgP5XJO0o1bWxd_8o8F0tsBg_DRI")
SESSION_NAME = getenv("SESSION_NAME", "BACxexkoqBPt5JW4kmH1A89RlAtgoolmxyAk9KZbe366ADUTiBMKIJa1f3Id1cTa6HTmMnrSSH2DG5XIeQbpbRKyDmCWMIoa26O69aVQ8FZgGHx6Swyr9Chi2lnkwk3VAPqfTrgOY1EG-dz4XXVdKxEZGzYp778d8U9DJIElk8jE4UC8_25PzYtAEThQncQ3tvJ3gpGxS1QxTIyN7gYNF5XlG3T2KdDFkAGyC5sTybgsOreHTxVDNL_flPljrnfEuwlfy5JyzV1j_pT_VBR4mHDeOKCoQon6AQdDr3vT07F6uQcmlC_AFtw-MAvQDII_uQfodxU3FfSil9307X6wfaR4AAAAAW5CyFkA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "AL_mtim")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "myozkmtimbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AL_mtim")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "tqq_kb")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
