import os

API_ID = API_ID =  28590119

API_HASH = os.environ.get("API_HASH", "2494557bf21e6c5152f26070aa1a97c7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", ""))

OWNER = int(os.environ.get("OWNER", "6556141430"))

LOG = -1002494437539,

# UPDATE_GRP = -1002494437539, # bot sat group

# auth_chats = [2494437539]

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6556141430").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


