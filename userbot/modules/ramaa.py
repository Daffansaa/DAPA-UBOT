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


@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Vicky Peler☑️**")
    await typew.edit("**Vicky Peler✅**")
    sleep(1)
    await typew.edit("**Toni Gilaa☑️**")
    await typew.edit("**Toni Gilaa✅**")
    sleep(2)
    await typew.edit("**Karina Depresi☑️**")
    await typew.edit("**Karina Depresi✅**")
    sleep(2)
    await typew.edit("**Yunus Gajelas☑️**")
    await typew.edit("**Yunus Gajelas✅**")
    sleep(2)
    await typew.edit("**Adel GJM!☑️**")
    await typew.edit("**Adel GJM!✅**")
    sleep(2)
    await typew.edit("**Jia GJB!☑️**")
    await typew.edit("**Jia GJB!✅**")
    sleep(2)
    await typew.edit("**Imeh,MengRibet☑️**")
    await typew.edit("**Imeh,MengRibet✅**")
    sleep(2)
    await typew.edit("**Jeje,Mengintil☑️**")
    await typew.edit("**Jeje,Mengintil✅**")
    sleep(3)
    await typew.edit("**CUMA RAMA YANG BENER!**")

# Create by myself @localheart

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})
