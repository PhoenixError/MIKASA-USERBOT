import asyncio
from collections import deque

from . import *

@bot.on(deadly_cmd(pattern=r"boxs$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"boxs$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "`boxs...`")
    deq = deque(list("ð¥ð§ð¨ð©ð¦ðªð«â¬â¬"))
    for _ in range(999):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(deadly_cmd(pattern=r"rain$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"rain$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "`Raining.......`")
    deq = deque(list("ð¬âï¸ð©ð¨ð§ð¦ð¥âð¤"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(deadly_cmd(pattern=r"deploy$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"deploy$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(12)
    event = await eor(event, "`Deploying...`")
    animation_chars = [
        "**Heroku Connecting To Latest [Github Build](The-Deadlybot/Deadlybot)**",
        f"**Build started by user** {deadly_mention}",
        f"**Deploy** `535a74f0` **by user** **{deadly_mention}**",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m stdborg`",
        "**State changed from starting to up**",
        "__INFO:DÑÎ±âly BÏÑ:Logged in as 557667062__",
        "__INFO:DÑÎ±âly BÏÑ:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(deadly_cmd(pattern=r"dump$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"dump$", allow_sudo=True))
async def _(message):
    if event.fwd_from:
        return
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "ð¥ ð ð«"
    event = await eor(message, "`droping....`")
    u, t, g, o, s, n = inp.split(), "ð", "<(^_^ <)", "(> ^_^)>", "â  ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await event.edit(something_else)
            except errors.MessageIdInvalidError:
                return


@bot.on(deadly_cmd(pattern=r"fleaveme$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"fleaveme$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(10)
    animation_chars = [
        "â¬â¬â¬\nâ¬â¬â¬\nâ¬â¬â¬",
        "â¬â¬â¬\nâ¬ðâ¬\nâ¬â¬â¬",
        "â¬â¬ï¸â¬\nâ¬ðâ¬\nâ¬â¬â¬",
        "â¬â¬ï¸âï¸\nâ¬ðâ¬\nâ¬â¬â¬",
        "â¬â¬ï¸âï¸\nâ¬ðâ¡ï¸\nâ¬â¬â¬",
        "â¬â¬ï¸âï¸\nâ¬ðâ¡ï¸\nâ¬â¬âï¸",
        "â¬â¬ï¸âï¸\nâ¬ðâ¡ï¸\nâ¬â¬ï¸âï¸",
        "â¬â¬ï¸âï¸\nâ¬ðâ¡ï¸\nâï¸â¬ï¸âï¸",
        "â¬â¬ï¸âï¸\nâ¬ï¸ðâ¡ï¸\nâï¸â¬ï¸âï¸",
        "âï¸â¬ï¸âï¸\nâ¬ï¸ðâ¡ï¸\nâï¸â¬ï¸âï¸",
    ]
    event = await eor(event, "fleaveme....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@bot.on(deadly_cmd(pattern=r"loveu$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"loveu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await eor(event, "loveu")
    animation_chars = [
        "ð",
        "ð©âð¨",
        "ð",
        "ð",
        "ð¤£",
        "ð",
        "ð",
        "ð",
        "ð",
        "âº",
        "ð",
        "ð¤",
        "ð¤¨",
        "ð",
        "ð",
        "ð¶",
        "ð£",
        "ð¥",
        "ð®",
        "ð¤",
        "ð¯",
        "ð´",
        "ð",
        "ð",
        "â¹",
        "ð",
        "ð",
        "ð",
        "ð",
        "ð¢",
        "ð­",
        "ð¤¯",
        "ð",
        "â¤",
        "I Love Youâ¤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@bot.on(deadly_cmd(pattern=r"plane$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"plane$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "Wait for plane...")
    await event.edit("â-------------")
    await event.edit("-â------------")
    await event.edit("--â-----------")
    await event.edit("---â----------")
    await event.edit("----â---------")
    await event.edit("-----â--------")
    await event.edit("------â-------")
    await event.edit("-------â------")
    await event.edit("--------â-----")
    await event.edit("---------â----")
    await event.edit("----------â---")
    await event.edit("-----------â--")
    await event.edit("------------â-")
    await event.edit("-------------â")
    await asyncio.sleep(3)


@bot.on(deadly_cmd(pattern=r"police$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"police$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(12)
    event = await eor(event, "Police")
    animation_chars = [
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
        "ðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´\nðµðµðµâ¬â¬â¬ð´ð´ð´",
        "ð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ\nð´ð´ð´â¬â¬â¬ðµðµðµ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])
        
@bot.on(deadly_cmd(pattern=f"hack$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(15)
    event = await eor(event, "`Hacking this kid....`")
    animation_chars = [
            "Looking for WhatsApp databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 0%\n[ââââââââââââââââââââ]\n`Looking for WhatsApp...`\nETA: 0m, 20s",
            "Hacking... 11.07%\n[ââââââââââââââââââââ]\n`Looking for WhatsApp...`\nETA: 0m, 18s",
            "Hacking... 20.63%\n[ââââââââââââââââââââ]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s",
            "Hacking... 34.42%\n[ââââââââââââââââââââ]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s",
            "Hacking... 42.17%\n[ââââââââââââââââââââ]\n`Searching for databases`\nETA: 0m, 12s",
            "Hacking... 55.30%\n[ââââââââââââââââââââ]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",
            "Hacking... 64.86%\n[ââââââââââââââââââââ]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",
            "Hacking... 74.02%\n[ââââââââââââââââââââ]\n`Trying to Decrypt...`\nETA: 0m, 06s",
            "Hacking... 86.21%\n[ââââââââââââââââââââ]\n`Trying to Decrypt...`\nETA: 0m, 04s",
            "Hacking... 93.50%\n[ââââââââââââââââââââ]\n`Decryption successful!`\nETA: 0m, 02s",
            "Hacking... 100%\n[ââââââââââââââââââââ]\n`Scanning file...`\nETA: 0m, 00s",
            "Hacking complete!\nUploading file...",
            "Targeted Account Hacked...!\n\n â File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 15])

@bot.on(deadly_cmd(pattern=r"jio$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"jio$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(19)
    event = await eor(event, "jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "*Optimising JIO NETWORK...*",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "`â â â â â â â`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


@bot.on(deadly_cmd(pattern=r"solarsystem$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"solarsystem$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(80)
    event = await eor(event, "solarsystem")
    animation_chars = [
        "`â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nðâ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nðâ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸ðâ¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸ââ¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸ðâ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ââ¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸ð\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nââ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nââ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸ð\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸`",
        "`â¼ï¸ââ¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸ðâ¼ï¸`",
        "`â¼ï¸â¼ï¸â¼ï¸ââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ðâ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ðâ¼ï¸â¼ï¸â¼ï¸`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
        
        
@bot.on(deadly_cmd(pattern="degi$"))
@bot.on(sudo_cmd(pattern="degi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "degi")
    await event.edit("WO")
    await asyncio.sleep(1.5)
    await event.edit("DegI")
    await asyncio.sleep(1.5)
    await event.edit("TuM")
    await asyncio.sleep(1.5)
    await event.edit("EkbaR")
    await asyncio.sleep(1.5)
    await event.edit("ManG")
    await asyncio.sleep(1.5)
    await event.edit("KaR")
    await asyncio.sleep(1.5)
    await event.edit("ToH")
    await asyncio.sleep(1.5)
    await event.edit("DekhO")
    await asyncio.sleep(1.5)
    await event.edit("Wo DeGi TuM eKbAr MaNg KaR tOh DeKhOð")


@bot.on(deadly_cmd(pattern=f"nehi$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"nehi$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "nehi")
    await event.edit(
        "`Wo PaKkA DeGi Tu ManG KaR ToH DekH\n AuR NaA De To UskI BheN Ko PakaDðð`"
    )
    await asyncio.sleep(999)


@bot.on(deadly_cmd(pattern="hnd (.*)"))
@bot.on(sudo_cmd(pattern="hnd (.*)", allow_sudo=True))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    event = await eor(event, "âï¸")
    animation_chars = [
        "ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿                                          ðð¿\nðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿",
        "ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾                                  ðð¾\nðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾",
        "ðð½ðð½ðð½ðð½ðð½ðð½ðð½\nðð½                        ðð½\nðð½                        ðð½\nðð½                        ðð½\nðð½                        ðð½\nðð½                        ðð½\nðð½ðð½ðð½ðð½ðð½ðð½ðð½",
        "ðð¼ðð¼ðð¼ðð¼ðð¼\nðð¼              ðð¼\nðð¼              ðð¼\nðð¼              ðð¼\nðð¼ðð¼ðð¼ðð¼ðð¼",
        f"ðð»ðð»ðð»\n{name}\nðð»ðð»ðð»",
        f"ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿\nðð¿ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¿\nðð¿ðð¾ðð½ðð½ðð½ðð½ðð½ðð½ðð½ðð¾ðð¿\nðð¿ðð¾ðð½ðð¼ðð¼ðð¼ðð¼ðð¼ðð½ðð¾ðð¿\nðð¿ðð¾ðð½ðð¼ðð»ðð»ðð»ðð¼ðð½ðð¾ðð¿\nðð¿  {name}  ðð¿\nðð¿ðð¾ðð½ðð¼ðð»ðð»ðð»ðð¼ðð½ðð¾ðð¿\nðð¿ðð¾ðð½ðð¼ðð¼ðð¼ðð¼ðð¼ðð½ðð¾ðð¿\nðð¿ðð¾ðð½ðð½ðð½ðð½ðð½ðð½ðð½ðð¾ðð¿\nðð¿ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¾ðð¿\nðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿ðð¿",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(deadly_cmd(pattern="phub$", outgoing=True))
@bot.on(sudo_cmd(pattern="phub$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await eor(event, "phub")

    animation_chars = [
        "P_",
        "PO_",
        "POR_",
        "PORN_",
        "PORNH_",
        "PORNHU_",
        "PORNHUB_",
        "PORNHUB",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])


@bot.on(deadly_cmd(pattern=r"amore$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"amore$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await eor(event, "amore")

    animation_chars = [
        "A_",
        "AM_",
        "AMO_",
        "AMOR_",
        "AMORE_",
        "AMOREâ¤_",
        ".-.",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])


@bot.on(deadly_cmd(pattern=r"sexy$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sexy$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await eor(event, "Sexy")

    animation_chars = [
        "S_",
        "SE_",
        "SEX_",
        "SEXY_",
        "SEXYð_",
        "SEXYð",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])
        
@bot.on(deadly_cmd(pattern="istar$", outgoing=True))
@bot.on(sudo_cmd(pattern="istar$", allow_sudo=True))
async def ammastar(deadlystar):
  
    if deadlystar.fwd_from:
      
        return
      
    animation_interval = 2
    
    animation_ttl = range(0, 11)
    
    await eor(deadlystar, "I am A Star")
    
    animation_chars = [
        "I Party like a rockstar",
        "I Look like a movie star",
        "I Play like an all star",
        "I Fuck like a pornstar",
        "Baby I'm a superstar",
    ]
    
    for i in animation_ttl:
      
        await asyncio.sleep(animation_interval)
        
        await deadlystar.edit(animation_chars[i % 11])
    
        
@bot.on(deadly_cmd(pattern=r"lmoon", outgoing=True))
@bot.on(sudo_cmd(pattern=r"lmoon", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return
    await eor(event, 
        "ðððððððð\nðððððððð\nðððððððð\nðððððððð\nðððððððð\nðððððððð\nðððððððð\nðððððððð\nðððððððð\nðððððððð\nðððððððð\nðððððððð\nðð¤ð»ððððð¤ð»ð\nðððððððð\nðððððððð\nðððððððð"
    )


@bot.on(deadly_cmd(pattern=r"city", outgoing=True))
@bot.on(sudo_cmd(pattern=r"city", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return
    await eor(event, 
        """ââð      â           â
       â  â         â    ð    â    â        â          â     â   â

ð¬ð¨ð«ð¢ð¤ð¥ð¦ðªð«
              ð²/     lð\ð³ð­
           ð³/  ð l  ð \ð´ ð¬                       ð¬  ð´/            l  ð    \ð²
      ð²/   ð     l               \
   ð³/ð¶           |   ð         \ ð´ð´ð´
ð´/                    |                     \ð²"""
    )


@bot.on(deadly_cmd(pattern=r"hii", outgoing=True))
@bot.on(sudo_cmd(pattern=r"hii", allow_sudo=True))
async def hi(event):
    if event.fwd_from:
        return
    await eor(event, "ðºâ¨â¨ðºâ¨ðºðºðº\nðºâ¨â¨ðºâ¨â¨ðºâ¨\nðºðºðºðºâ¨â¨ðºâ¨\nðºâ¨â¨ðºâ¨â¨ðºâ¨\nðºâ¨â¨ðºâ¨ðºðºðº\nââââââââ")


@bot.on(deadly_cmd(pattern=r"cheer", outgoing=True))
@bot.on(sudo_cmd(pattern=r"cheer", allow_sudo=True))
async def cheer(event):
    if event.fwd_from:
        return
    await eor(event, 
        "ðððððð\nâ Cheer Up  ðµ\nð â¨ )) â¨  ð\nðâ (( * â£â ð\nðâ*ð â£â ð \nðââââ  ðð For YOU  ð°\nðððððð"
    )


@bot.on(deadly_cmd(pattern=r"getwell", outgoing=True))
@bot.on(sudo_cmd(pattern=r"getwell", allow_sudo=True))
async def getwell(event):
    if event.fwd_from:
        return
    await eor(event, "ð¹ð¹ð¹ð¹ð¹ð¹ð¹ð¹ \nð¹ð·ð¢ðð·ð¢ð¨ð¹\nð¹ðððµðððð¹\nð¹ GetBetter Soon! ð¹\nð¹ð¹ð¹ð¹ð¹ð¹ð¹ð¹")

@bot.on(deadly_cmd(pattern="switch$", outgoing=True))
@bot.on(sudo_cmd(pattern="switch$", allow_sudo=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 11)

  #  input_str = event.pattern_match.group(1)

  #  if input_str == "switch":

    await eor(event, "Switch")

    animation_chars = [
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬[ð²](https://github.com/TEAM-MISAKA/MISAKA-BOT)\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬[ð²](https://github.com/TEAM-MISAKA/MISAKA-BOT)\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\n[ð](https://t.me/official_sameer)â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬[ð²](https://github.com/TEAM-MISAKA/MISAKA-BOT)\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬[ð](https://t.me/official_sameer)â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬[ð²](https://github.com/TEAM-MISAKA/MISAKA-BOT)\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬[ð](https://t.me/official_sameer)â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬[ð²](https://github.com/TEAM-MISAKA/MISAKA-BOT)\nâ¬[ð](https://t.me/official_sameer)â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬[ð²](https://github.com/TEAM-MISAKA/MISAKA-BOT)\nâ¬â¬[ð](https://t.me/official_sameer)â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬[ð²](https://github.com/TEAM-MISAKA/MISAKA-BOT)\nâ¬â¬â¬[ð](https://t.me/official_sameer)â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬ð²\nâ¬â¬â¬â¬[ð](https://t.me/official_sameer)â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬[ð](https://t.me/official_sameer)â¬ð²\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬[ð](https://t.me/official_sameer)ð²\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
         "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬ð³\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


@bot.on(deadly_cmd(pattern=r"sprinkle", outgoing=True))
@bot.on(sudo_cmd(pattern=r"sprinkle", allow_sudo=True))
async def sprinkle(event):
    if event.fwd_from:
        return
    await eor(event, 
        "â¨.â¢*Â¨*.Â¸.â¢*Â¨*.Â¸Â¸.â¢*Â¨*â¢ Æ¸ÓÆ·\nð¸ðºð¸ðºð¸ðºð¸ðº\n Sprinkled with loveâ¤\nð·ð»ð·ð»ð·ð»ð·ð»\n Â¨*.Â¸.â¢*Â¨*. Â¸.â¢*Â¨*.Â¸Â¸.â¢*Â¨`*â¢.â¨\nð¹ðð¹ðð¹ðð¹ð"
    )
    

@bot.on(deadly_cmd(pattern=r"f", outgoing=True))
@bot.on(sudo_cmd(pattern=r"f", allow_sudo=True))
async def payf(event):
    if event.fwd_from:
        return
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await eor(event, pay)


@bot.on(deadly_cmd(outgoing=True, pattern="kiler( (.*)|$)"))
@bot.on(sudo_cmd(pattern="kiler( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(1)
    if not name:
        name = "die"
    animation_interval = 0.7
    animation_ttl = range(8)
    event = await eor(event, f"**Ready Commando **__{deadly_mention}....")
    animation_chars = [
        "ï¼¦ï½ï½ï½ï½ï½ï½ï½",
        f"__**Commando **__{deadly_mention}          \n\n_/ï¹\_\n (Ò`_Â´)\n <,ï¸»â¦â¤â Ò - \n _/ï¹\_\n",
        f"__**Commando **__{deadly_mention}          \n\n_/ï¹\_\n (Ò`_Â´)\n  <,ï¸»â¦â¤â Ò - -\n _/ï¹\_\n",
        f"__**Commando **__{deadly_mention}          \n\n_/ï¹\_\n (Ò`_Â´)\n <,ï¸»â¦â¤â Ò - - -\n _/ï¹\_\n",
        f"__**Commando **__{deadly_mention}          \n\n_/ï¹\_\n (Ò`_Â´)\n<,ï¸»â¦â¤â Ò - -\n _/ï¹\_\n",
        f"__**Commando **__{deadly_mention}          \n\n_/ï¹\_\n (Ò`_Â´)\n <,ï¸»â¦â¤â Ò - \n _/ï¹\_\n",
        f"__**Commando **__{deadly_mention}         \n\n_/ï¹\_\n (Ò`_Â´)\n  <,ï¸»â¦â¤â Ò - -\n _/ï¹\_\n",
        f"__**Commando **__{deadly_mention}          \n\n_/ï¹\_\n (Ò`_Â´)\n <,ï¸»â¦â¤â Ò - - - {name}\n _/ï¹\_\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@bot.on(deadly_cmd(pattern="eye$"))
@bot.on(sudo_cmd(pattern="eye$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(10)
    event = await eor(event, "ðð")
    animation_chars = [
        "ðð\n  ð  =====> Kya dekh rha hai lawde",
        "ðð\n  ð  =====> Chal gandu nikal",
        "ðð\n  ð  =====> Teri maa nach rhi h idhar?",
        "ðð\n  ð  =====> Bhag madarchod",
        "ðð\n  ð  =====> Abee ja naa gandu",
        "ðð\n  ð  =====> Abee jaa naa suar",
        "ðð\n  ð  =====> Abe jaa naa chakke",
        "ðð\n  ð  =====> Aae madarchod apna kaam kar",
        "ðð\n  ð  =====> Chal abb gand mra bsdk",
        "ðð\n  ð  =====> Bhag lode",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])
    await asyncio.sleep(animation_interval)
    await event.delete()


@bot.on(deadly_cmd(pattern="thinking$"))
@bot.on(sudo_cmd(pattern="thinking$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(288)
    event = await eor(event, "thinking..")
    animation_chars = [
        "THINKING",
        "THI&K#Nâ¹",
        "T+IN@I?G",
        "Â¿H$NKâNG",
        "Â¶HÃNK&N*",
        "NGITHKIN",
        "T+I#K@â¹G",
        "THINKING",
        "THI&K#Nâ¹",
        "T+IN@I?G",
        "Â¿H$NKâNG",
        "Â¶HÃNK&N*",
        "NGITHKIN",
        "T+I#K@â¹G",
        "THINKING",
        "THI&K#Nâ¹",
        "T+IN@I?G",
        "Â¿H$NKâNG",
        "Â¶HÃNK&N*",
        "NGITHKIN",
        "T+I#K@â¹G",
        "THINKING",
        "THI&K#Nâ¹",
        "T+IN@I?G",
        "Â¿H$NKâNG",
        "Â¶HÃNK&N*",
        "NGITHKIN",
        "T+I#K@â¹G",
        "THINKING",
        "THI&K#Nâ¹",
        "T+IN@I?G",
        "Â¿H$NKâNG",
        "Â¶HÃNK&N*",
        "NGITHKIN",
        "T+I#K@â¹G",
        "THINKING... ð¤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 36])


@bot.on(deadly_cmd(pattern=f"snake$", outgoing=True))
@bot.on(sudo_cmd(pattern="snake$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(27)
    event = await eor(event, "snake..")
    animation_chars = [
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â»ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â»ï¸â»ï¸ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "ââ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â¼ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
        "â»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â»ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ»ï¸â»ï¸â»ï¸â»ï¸â»ï¸",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 27])


@bot.on(deadly_cmd(pattern=f"human$", outgoing=True))
@bot.on(sudo_cmd(pattern="human$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(16)
    event = await eor(event, "human...")
    animation_chars = [
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬ð\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬ðâ¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬ðâ¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬ðâ¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬ðâ¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬ðâ¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nðâ¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬ðâ¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬ðâ¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬ðâ¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬ðâ¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬ðâ¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬ðâ¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
        "â¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nâ¬â¬â¬ðâ¬â¬â¬\nâ¬â¬â¬â¬â¬â¬â¬\nð²ð²ð²ð²ð²ð²ð²",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 16])


@bot.on(deadly_cmd(pattern=f"mc$", outgoing=True))
@bot.on(sudo_cmd(pattern="mc$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(28)
    event = await eor(event, "mc..")
    animation_chars = [
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â»ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â»ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â»ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â»ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â»ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â»ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â»ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â»ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â»ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â»ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â»ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â»ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â»ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ»ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â»ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â»ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â»ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â»ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â»ï¸â¼ï¸â»ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â»ï¸â»ï¸â»ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 28])


@bot.on(deadly_cmd(pattern="virus$"))
@bot.on(sudo_cmd(pattern="virus$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(30)
    event = await eor(event, "Injecting virus....")
    animation_chars = [
        "ð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "â¼ï¸ð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "â¼ï¸â¼ï¸ð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "â¼ï¸â¼ï¸â¼ï¸ï¸ð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸ð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "ââ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðâââ",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðââââ¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðââââ¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nð´ðµðâââð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸ð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðââââ¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðâââð´ðµðââââ¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðââââ¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðââââ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðââââ¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðââââ¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸ð´ðµðâââð´ðµðââââ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸ð´ðµðââââ¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸â¼ï¸",
        "â¼ï¸â¼ï¸\nâ¼ï¸â¼ï¸",
        "â¼ï¸",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 30])


@bot.on(deadly_cmd(pattern=r"repe$", outgoing=True))
@bot.on(sudo_cmd(pattern="repe$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(30)
    event = await eor(event, "repe")
    animation_chars = [
        "**r**",
        "**ra**",
        "**rap**",
        "**rape**",
        "**rape_**",
        "**rape_t**",
        "**rape_tr**",
        "**rape_tra**",
        "**rape_trai**",
        "**rape_train**",
        "**ape_trainð**",
        "**pe_trainððð**",
        "**e_trainðððð**",
        "**_trainððððð**",
        "**trainðððððð**",
        "**rainððððððð**",
        "**ainðððððððð**",
        "**inððððððððð**",
        "**nðððððððððð**",
        "ðððððððððð",
        "ððððððððð",
        "ðððððððð",
        "ððððððð",
        "ðððððð",
        "ððððð",
        "ðððð",
        "ððð",
        "ðð",
        "ð",
        "**rApEd**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 30])


@bot.on(deadly_cmd(pattern=f"nikal$", outgoing=True))
@bot.on(sudo_cmd(pattern="nikal$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(6)
    event = await eor(event, "nakal")
    animation_chars = [
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â   â    â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Nikal   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â       â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Lavde   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__|â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Pehli   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â          â¡\n  â â¢¿â£¯â â â (P)â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â    â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Fursat  â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __ â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â  â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Meeee   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__| â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
        "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â   â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Nikal   â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â loduâ â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(deadly_cmd(pattern=f"music$", outgoing=True))
@bot.on(sudo_cmd(pattern="music$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.5
    animation_ttl = range(11)
    event = await eor(event, "starting player...")
    animation_chars = [
        "â¬¤â¬¤â¬¤ 81% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:00** â±â±â±â±â±â±â±â±â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¶ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: I Fone XXX**",
        "â¬¤â¬¤â¬¤ 81% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:01** â°â±â±â±â±â±â±â±â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¬¤ 81% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:02** â°â°â±â±â±â±â±â±â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¬¤ 81% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:03** â°â°â°â±â±â±â±â±â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¯ 80% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:04** â°â°â°â°â±â±â±â±â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¯ 80% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:05** â°â°â°â°â±â±â±â±â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¯ 80% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:06** â°â°â°â°â°â°â±â±â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¯ 80% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:07** â°â°â°â°â°â°â°â±â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¯ 80% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:08** â°â°â°â°â°â°â°â°â±â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¯ 80% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:09** â°â°â°â°â°â°â°â°â°â± **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `â¸ï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
        "â¬¤â¬¤â¯ 80% â â â â â â â â â â â â â â â â â â â `âï¸`\n\nâ â â â â [Music Player](t.me/deadly_techy)\n\nâ â â â **Now Playing:shape of u**\n\n**00:10** â°â°â°â°â°â°â°â°â°â° **00:10**\n\nâ â â â â `ð` `â®ï¸` `âªï¸` `âºï¸` `â©ï¸` `â­ï¸`\n\n**â Next Song:** __Alan Walker - Alone.__\n\nâ â â â **â Device: Ifone XXX**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(deadly_cmd(pattern=f"squ$", outgoing=True))
@bot.on(sudo_cmd(pattern="squ$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(
        event, "âââââââââââââââââââââ \n  \nâââââââââââââââââââââ"
    )
    await asyncio.sleep(1)
    await event.edit("âââââââââââââââââââââ \n \tâ \nâââââââââââââââââââââ")
    await asyncio.sleep(1)
    await event.edit("âââââââââââââââââââââ \n â \tâ \nâââââââââââââââââââââ")
    await asyncio.sleep(1)
    await event.edit("âââââââââââââââââââââ \n â â â \nâââââââââââââââââââââ")
    await asyncio.sleep(1)
    await event.edit("âââââââââââââââââââââ \n â â â â \nâââââââââââââââââââââ")
    await asyncio.sleep(1)
    await event.edit("âââââââââââââââââââââ \n â â â â â \nâââââââââââââââââââââ")
    await asyncio.sleep(1)
    await event.edit("âââââââââââââââââââââ \n â â â â â â \nâââââââââââââââââââââ")
    await asyncio.sleep(1)
    await event.edit("âââââââââââââââââââââ \n â â â â â â â \nâââââââââââââââââââââ")
    await asyncio.sleep(1)
    await event.edit("âââââââââââââââââââââ \n â â â â â â â â \nâââââââââââââââââââââ")
    await asyncio.sleep(1)
    await event.edit(
        "âââââââââââââââââââââ \n â â â â â â â â â \nâââââââââââââââââââââ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "âââââââââââââââââââââ \n â â â â â â â â â â \nâââââââââââââââââââââ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "âââââââââââââââââââââ \n â â â â â â â â â â â \nâââââââââââââââââââââ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "âââââââââââââââââââââ \n â â â â â â â â â â â â \nâââââââââââââââââââââ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "âââââââââââââââââââââ \n â â â â â â â â â â â â â \nâââââââââââââââââââââ"
    )
    await asyncio.sleep(1)
    await event.edit(
        "âââââââââââââââââââââ \n â â â â â â â â â â â â â â \nâââââââââââââââââââââ"
    )
    await asyncio.sleep(6)


CmdHelp("animations").add_command(
  'boxs', None, 'Use and see'
).add_command(
  'kiler', '<text>', 'Cool killing animation with name'
).add_command(
  'eye', None, 'Use and see'
).add_command(
  'thinking', None, 'Use and see'
).add_command(
  'snake', None, 'Use and see'
).add_command(
  'human', None, 'Use and see'
).add_command(
  'mc', None, 'Use and see'
).add_command(
  'virus', None, 'Use and see'
).add_command(
  'repe', None, 'Use and see'
).add_command(
  'nikal', None, 'Use and see'
).add_command(
  'music', None, 'Use and see'
).add_command(
  'squ', None, 'Use and see'
).add_command(
  'rain', None, 'Use and see'
).add_command(
  'deploy', None, 'Use and see'
).add_command(
  'dump', None, 'Use and see'
).add_command(
  'fleaveme', None, 'Use and see'
).add_command(
  'loveu', None, 'Use and see'
).add_command(
  'plane', None, 'Use and see'
).add_command(
  'police', None, 'Use and see'
).add_command(
  'jio', None, 'Use and see'
).add_command(
  'solarsystem', None, 'Use and see'
).add_command(
  'degi', None, 'Use and see'
).add_command(
  'nehi', None, 'Use and see'
).add_command(
  'hack', None, 'Im a hacker bitch'
).add_command(
  'hnd', '<your text>', 'A handy animation with the text,'
).add_command(
  'owner', None, 'Use and see'
).add_command(
  'padmin', None, 'Prank promote a user'
).add_command(
  "phub", None, "Animated PORNHUB Typing"
).add_command(
  "amore", None, "Animated AMORE Typing"
).add_command(
  "sexy", None, "Animated SEXY Typing"
).add_command(
  "unoob", None, "Animated text calling them noobð¶"
).add_command(
  "menoob", None, "Animated text claiming you noob"
).add_command(
  "uproo", None, "Animated text claiming you to be proooo"
).add_command(
  "mepro", None, "Animated text calling them proo Af!!"
).add_command(
  "sprinkle", None, "Use and see"
).add_command(
  "getwell", None, "Use and see"
).add_command(
  "cheer", None, "Use and see"
).add_command(
  "hii", None, "Use and see"
).add_command(
  "city", None, "Use and see"
).add_command(
  "lmoon", None, "Use and see"
).add_command(
  "istar", None, "I am a Superstarâ¡â¨"
).add_command(
  "switch", None, "Click on the switch to reveal the priceâ¨"
).add_command(
  "thanos", None, "A poem on Thanos... Maybeð¤"
).add_command(
  "tp", None, "Use and see"
).add_command(
  "f", "<text>", "Prints the given text in 'F' format"
).add_command(
  "wahack", None, "Whatsapp Hack animation"
).add_info(
  "Fun Animations."
).add_warning(
  "â ï¸ Some commands may cause flood error."
).add()
