# GAUSAH KESINI ANJING NGENTOT
# BUATAN VCKYOUUU

import io
import textwrap


from PIL import Image, ImageDraw, ImageFont
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.rgb (.*)")
async def stext(event):
    sticktext = event.pattern_match.group(1)

    if not sticktext:
        await event.edit("`Mohon Maaf, Saya Membutuhkan Text Anda.`")
        return

    await event.delete()

    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 220
    font = ImageFont.truetype(
        "userbot/RobotoMono-Regular.ttf",
        size=fontsize)

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(
            "userbot/RobotoMono-Regular.ttf",
            size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2,
         (512 - height) / 2),
        sticktext,
        font=font,
        fill="white")

    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    await event.client.send_file(event.chat_id, image_stream)


CMD_HELP.update({
    'ramgb':
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.rgb` <text>"
    "\nUsage: Mengubah Teks/Kata-Kata, Menjadi Stiker Anda."
})
