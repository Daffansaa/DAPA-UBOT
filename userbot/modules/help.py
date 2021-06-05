# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpme(?: |$)(.*)")
async def help(event):
    """ For .helpme command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**`NGETIK YANG BENER NGENTOT!`**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t 💫  "
        await event.edit("**⭐𝗥𝗔𝗠-𝗨𝗕𝗢𝗧⭐**\n\n"
                         f"**💫 Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**💀 Mᴏᴅᴜʟᴇꜱ : {len(modules)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"💫 {string}\nNGETIK YANG BENER YA NGENTOOOOT!!\n\n")
        await event.reply(f"\n**Contoh** : Ketik <`.help ping`> Untuk Informasi Pengunaan.\nJangan Lupa Berdoa Sebelum Mencoba wahahaha..")
        await asyncio.sleep(50)
        await event.delete()
