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


@register(outgoing=True, pattern='^.404(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Axel Peler☑️**")
    await typew.edit("**Axel Peler✅**")
    sleep(1)
    await typew.edit("**Nola Gilaa☑️**")
    await typew.edit("**Nola Gilaa✅**")
    sleep(2)
    await typew.edit("**Repan Depresi☑️**")
    await typew.edit("**Repan Depresi✅**")
    sleep(2)
    await typew.edit("**Dimas Gajelas☑️**")
    await typew.edit("**Dimas Gajelas✅**")
    sleep(2)
    await typew.edit("**Yoll GJM!☑️**")
    await typew.edit("**Yoll GJM!✅**")
    sleep(2)
    await typew.edit("**Ryan Hulk Versi Beta!☑️**")
    await typew.edit("**Ryan Hulk Versi Beta!✅**")
    sleep(2)
    await typew.edit("**Shallu ,MengRibet☑️**")
    await typew.edit("**Shallu ,MengRibet✅**")
    sleep(2)
    await typew.edit("**Mas Ade,Mengintol☑️**")
    await typew.edit("**Mas Ade,Mengintol✅**")
    sleep(3)
    await typew.edit("**CUMA DAPA DOANG YANG BENER!**")

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
