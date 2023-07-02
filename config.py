from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQHD6LgAcHjegD4bXUxM6Vqw5tzsat8ML2Ih7bUcuzo33Fkz5R5PEIvqBYXFUc5VABluFHdgF2CAPsz3ZvE8MMNeLbVhmBVWvqIC0f9FXE3ud56Lmttk7WHdNpztIshZrkz44Cjb3oSlvxhYduA439d1iwHwbPJFohTT5NrqzGmgNvMLIy_lwGSNhesOPRDYmAGj8ALTlAgpzD-wz3TzRrFYLByAm11hXdspMDckwuCMNzlHWHYrNrOMNlu9SbTLa3Cbp2ATYhwNiLDGO2eXOhC5EnzvZi3YGDY0iFnL87RGh3hRBI-Ja05SLIFTotsbxoUfJY83w8mcsbu3ExdxC-O0UP0IlwAAAAF1QO7LAA")
BOT_TOKEN = getenv("BOT_TOKEN", "6356388726:AAGNT3VwYvMQ55KGndcUfQ9uQ-Cz-Dw7Yvg")
BOT_USERNAME = getenv("BOT_USERNAME", "musicXplayerBot")
admins = {6262157003}
API_ID = int(getenv("API_ID" , 29616312))
API_HASH = getenv("API_HASH", "dd1a05ab4c47a5a037cc067cf4bded27")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
