from environs import Env

# init environs
env = Env()
env.read_env()

# get data from .env file
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("IP")