# credit goes to @D3_krish and @official_sameer

from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *


#-------------------------------------------------------------------------------

DEADLY_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
DEADLY_CAPTION = "π₯ βΡgΡΠΈβΡΡ Ξ±f DΡΞ±βly BΟΡ π₯\n\n"
DEADLY_CAPTION += (
    f"                __βΌπΌπ°πππ΄πβ__\n  **γ {Config.YOUR_NAME} γ**\n\n"
)
DEADLY_CAPTION += f"ββββββββββββββββββββ\n"
DEADLY_CAPTION += f"β β’β³β  `ππ΄π»π΄ππ·πΎπ½:` `{tel_ver}` \n"
DEADLY_CAPTION += f"β β’β³β  `ππ΄πππΈπΎπ½:` `{deadly_ver}`\n"
DEADLY_CAPTION += f"β β’β³β  `πΆππΎππΏ:`  [πΉπΎπΈπ½](t.me/DEADLY_USERBOT)\n"
DEADLY_CAPTION += f"β β’β³β  `π²π·π°π½π½π΄π»:` [πΉπΎπΈπ½](t.me/deadly_techy)\n"
DEADLY_CAPTION += f"β β’β³β  `π²ππ΄π°ππΎπ:` [β‘ππ°πΌπ΄π΄πβ‘](https://t.me/official_sameer)\n"
DEADLY_CAPTION += f"β β’β³β  `πΎππ½π΄π:` [β‘π³π°π½πΈππ· πΎπΏβ‘](https://t.me/idanishbaba)\n"
DEADLY_CAPTION += f"ββββββββββββββββββββ\n\n"
DEADLY_CAPTION += " [β¨ππ΄πΏπΎβ¨](https://github.com/DEADLY-FIGHTERS/DEADLY-BOT) πΉ [ππ»πΈπ²π΄π½ππ΄π](https://github.com/DEADLY-FIGHTERS/DEADLY-BOT/blob/main/LICENSE)"
                            
                                      
#-------------------------------------------------------------------------------

# for Deadlybot
# ONLY for Deadlybot
# EDITED BY - @SAMEER_795 (SAMEER )
# KANGERS STAY AWAY
# JISNE KANG KIYA USKI MA CHOD DI JAYEGI
# BHADWE KANG MT KR LENA ...
# TERI MA KI CHUT KANGER
# CHL AGAR KANG HI KRNA HE TO CREDIT KE SATH KR


import time

from userbot import StartTime
from Deadlybot.utils import admin_cmd, edit_or_reply, sudo_cmd

ludosudo = Config.SUDO

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = Config.YOUR_NAME or "Deadly User"
DEADLY_PIC = Config.ALIVE_PIC

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
                         

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="deadly$"))
@bot.on(sudo_cmd(pattern="deadly$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if DEADLY_PIC:
        deadly_caption = f"**{Config.ALIVE_MSG}**\n\n"
        deadly_caption += f"ββββββββββββββββββββββββββββ\n"                
        deadly_caption += f"ββββββββββββββββββββ\n"
        deadly_caption += f"β£β’β³β  `Tα΄Κα΄α΄Κα΄Ι΄:` `{tel_ver}` \n"
        deadly_caption += f"β£β’β³β  `Vα΄ΚsΙͺα΄Ι΄:` `{deadly_ver}`\n"
        deadly_caption += f"β£β’β³β  `π°π±πππ΄:` `{abuse_m}`\n"
        deadly_caption += f"β£β’β³β  `Sα΄α΄α΄:` `{is_sudo}`\n"
        deadly_caption += f"β£β’β³β  `CΚα΄Ι΄Ι΄α΄Κ:` [Jα΄ΙͺΙ΄](Config.YOUR_CHANNEL)\n"
        deadly_caption += f"β£β’β³β  `GΚα΄α΄α΄:` [Jα΄ΙͺΙ΄](Config.YOUR_GROUP)\n"
        deadly_caption += f"β£β’β³β  `Uα΄α΄Ιͺα΄α΄:`{uptime}`\n"
        deadly_caption += f"ββββββββββββββββββββ\n"
        await alive.client.send_file(
            alive.chat_id, DEADLY_IMG, caption=deadly_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"ββββββββββββββββββββ\n"
            f"β£β’β³β  `ππ΄π»π΄ππ·πΎπ½:` `1.23.0` \n"
            f"β£β’β³β  `ππ΄πππΈπΎπ½:` `0.2`\n"
            f"β£β’β³β  `π°π±πππ΄:` `Config.ABUSE`\n"
            f"β£β’β³β  `Sα΄α΄α΄:` `{is_sudo}`\n"
            f"β£β’β³β  `π²π·π°π½π½π΄π»:` [α΄α΄ΙͺΙ΄](Config.YOUR_CHANNEL)\n"
            f"β£β’β³β  `πΆππΎππΏ:` [α΄α΄ΙͺΙ΄](Config.YOUR_GROUP)\n"
            f"β£β’β³β  `ππΏππΈπΌπ΄:`{uptime}\n`"
            f"ββββββββββββββββββββ\n"
        )
                
CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "deadly", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "β Harmless Module"
).add()
