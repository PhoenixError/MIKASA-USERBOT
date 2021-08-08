import datetime
from DeadlyBot import *
from DeadlyBot.config import Config
from DeadlyBot.helpers import *
from DeadlyBot.utils import *
from DeadlyBot.random_strings import *
from DeadlyBot.version import __mikasa__
from telethon import version


MIKASA_USER = bot.me.first_name
official_sameer = bot.uid
mikasa_mention = f"[{MIKASA_USER}](tg://user?id={official_sameer})"
mikasa_logo = "./DeadlyBot/resources/pics/DeadlyBot_logo.jpg"
cjb = "./DeadlyBot/resources/pics/cjb.jpg"
restlo = "./DeadlyBot/resources/pics/rest.jpeg"
shuru = "./DeadlyBot/resources/pics/shuru.jpg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
mikasa_ver = __mikasa__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.MY_CHANNEL or "deadly_techy"
my_group = Config.MY_GROUP or "Deadly_bot_support"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/deadly_techy"
mikasa_channel = f"[†hê ʍɨӄǟֆǟ ẞø†]({chnl_link})"
grp_link = "https://t.me/Deadly_bot_support"
mikasa_grp = f"[ʍɨӄǟֆǟ ẞø† Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# DeadlyBot
