# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
📚 Commands Available -

• `{i}carbon <text/balas ke pesan/balas ke dokumen>`
   karbonisasi teks dengan pengaturan default.

• `{i}rcarbon <text/reply to msg/reply to document>`
   karbonisasi teks dengan warna background random.
"""

import random

import requests
from carbonnow import Carbon

from . import *

all_col = [
    "Black",
    "Navy",
    "DarkBlue",
    "MediumBlue",
    "Blue",
    "DarkGreen",
    "Green",
    "Teal",
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "MediumSpringGreen",
    "Lime",
    "SpringGreen",
    "Aqua",
    "Cyan",
    "MidnightBlue",
    "DodgerBlue",
    "LightSeaGreen",
    "ForestGreen",
    "SeaGreen",
    "DarkSlateGray",
    "DarkSlateGrey",
    "LimeGreen",
    "MediumSeaGreen",
    "Turquoise",
    "RoyalBlue",
    "SteelBlue",
    "DarkSlateBlue",
    "MediumTurquoise",
    "Indigo  ",
    "DarkOliveGreen",
    "CadetBlue",
    "CornflowerBlue",
    "RebeccaPurple",
    "MediumAquaMarine",
    "DimGray",
    "DimGrey",
    "SlateBlue",
    "OliveDrab",
    "SlateGray",
    "SlateGrey",
    "LightSlateGray",
    "LightSlateGrey",
    "MediumSlateBlue",
    "LawnGreen",
    "Chartreuse",
    "Aquamarine",
    "Maroon",
    "Purple",
    "Olive",
    "Gray",
    "Grey",
    "SkyBlue",
    "LightSkyBlue",
    "BlueViolet",
    "DarkRed",
    "DarkMagenta",
    "SaddleBrown",
    "DarkSeaGreen",
    "LightGreen",
    "MediumPurple",
    "DarkViolet",
    "PaleGreen",
    "DarkOrchid",
    "YellowGreen",
    "Sienna",
    "Brown",
    "DarkGray",
    "DarkGrey",
    "LightBlue",
    "GreenYellow",
    "PaleTurquoise",
    "LightSteelBlue",
    "PowderBlue",
    "FireBrick",
    "DarkGoldenRod",
    "MediumOrchid",
    "RosyBrown",
    "DarkKhaki",
    "Silver",
    "MediumVioletRed",
    "IndianRed ",
    "Peru",
    "Chocolate",
    "Tan",
    "LightGray",
    "LightGrey",
    "Thistle",
    "Orchid",
    "GoldenRod",
    "PaleVioletRed",
    "Crimson",
    "Gainsboro",
    "Plum",
    "BurlyWood",
    "LightCyan",
    "Lavender",
    "DarkSalmon",
    "Violet",
    "PaleGoldenRod",
    "LightCoral",
    "Khaki",
    "AliceBlue",
    "HoneyDew",
    "Azure",
    "SandyBrown",
    "Wheat",
    "Beige",
    "WhiteSmoke",
    "MintCream",
    "GhostWhite",
    "Salmon",
    "AntiqueWhite",
    "Linen",
    "LightGoldenRodYellow",
    "OldLace",
    "Red",
    "Fuchsia",
    "Magenta",
    "DeepPink",
    "OrangeRed",
    "Tomato",
    "HotPink",
    "Coral",
    "DarkOrange",
    "LightSalmon",
    "Orange",
    "LightPink",
    "Pink",
    "Gold",
    "PeachPuff",
    "NavajoWhite",
    "Moccasin",
    "Bisque",
    "MistyRose",
    "BlanchedAlmond",
    "PapayaWhip",
    "LavenderBlush",
    "SeaShell",
    "Cornsilk",
    "LemonChiffon",
    "FloralWhite",
    "Snow",
    "Yellow",
    "LightYellow",
    "Ivory",
    "White",
]


@ultroid_cmd(
    pattern="carbon",
)
async def crbn(event):
    xxxx = await eor(event, get_string("com_1"))
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await ultroid_bot.download_media(temp)
            a = open(b)
            code = a.read()
            a.close()
            os.remove(b)
        else:
            code = temp.message
    else:
        code = event.text.split(" ", maxsplit=1)[1]
    webs = requests.get("https://carbonara.vercel.app/api/cook")
    if webs.status_code == 502:
        return await eor(
            event, "`terjadi kesalahan server sementara !!\nsilahkan coba lagi nanti.`"
        )
    carbon = Carbon(base_url="https://carbonara.vercel.app/api/cook", code=code)
    xx = await carbon.memorize("ultroid_carbon")
    await xxxx.delete()
    await ultroid_bot.send_file(
        event.chat_id,
        xx,
        caption=f"karbon oleh [{OWNER_NAME}](tg://user?id={OWNER_ID})",
    )


@ultroid_cmd(
    pattern="rcarbon",
)
async def crbn(event):
    xxxx = await eor(event, "`memproses...`")
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await ultroid_bot.download_media(temp)
            a = open(b)
            code = a.read()
            a.close()
            os.remove(b)
        else:
            code = temp.message
    else:
        code = event.text.split(" ", maxsplit=1)[1]
    col = random.choice(all_col)
    webs = requests.get("https://carbonara.vercel.app/api/cook")
    if webs.status_code == 502:
        return await eor(
            event, "`terjadi kesalahan server sementara !!\nsilahkan coba lagi nanti.`"
        )
    carbon = Carbon(
        base_url="https://carbonara.vercel.app/api/cook", code=code, background=col
    )
    xx = await carbon.memorize("ultroid_carbon")
    await xxxx.delete()
    await ultroid_bot.send_file(
        event.chat_id,
        xx,
        caption=f"karbon oleh [{OWNER_NAME}](tg://user?id={OWNER_ID})",
    )
