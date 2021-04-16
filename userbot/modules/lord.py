from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.rama(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Rama ganteng☑️**")
    await typew.edit("**Rama Ganteng✅**")
    sleep(1)
    await typew.edit("**Rama baik☑️**")
    await typew.edit("**Rama baik✅**")
    sleep(2)
    await typew.edit("**Rama setia☑️**")
    await typew.edit("**Rama setia✅**")
    sleep(3)
    await typew.edit("**Rama Ga galak☑️**")
    await typew.edit("**Rama Ga galak✅**")
    sleep(3)
    await typew.edit("**Kalian Semua stress,Kecuali rama😋**")


@register(outgoing=True, pattern='^.as(?: |$(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam dulu biar sopan...`")
    sleep(1)
    await typew.edit("`A`")
    await typew.edit("`As`")
    await typew.edit("`Ass`")
    await typew.edit("`Assa`")
    await typew.edit("`Assal`")
    await typew.edit("`Assala`")
    await typew.edit("`Assalam`")
    await typew.edit("`Assalamu`")
    await typew.edit("`Assalamu'`")
    await typew.edit("`Assalamu'a`")
    await typew.edit("`Assalamu'al`")
    await typew.edit("`Assalamu'ala`")
    await typew.edit("`Assalamu'alai`")
    await typew.edit("`Assalamu'alaik`")
    await typew.edit("`Assalamu'alaiku`")
    await typew.edit("`Assalamu'alaikum`")
    sleep(2)
    await typew.edit("`YANG GAK JAWAB,FIX ATHEIS!!`")


# Create by myself @localheart

CMD_HELP.update({
    "stres":
    "`.stres`\
    \nUsage: alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.rama` ; `.as`\
    \nUsage: coba aja & salam."
})
