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
    await typew.edit("**Isal Plerr☑️**")
    await typew.edit("**Isal Plerr✅**")
    sleep(2)
    await typew.edit("**Nola Gilaa☑️**")
    await typew.edit("**Nola Gilaa✅**")
    sleep(2)
    await typew.edit("**Alda Menggosip☑️**")
    await typew.edit("**Alda Menggosip✅**")
    sleep(2)
    await typew.edit("**Repan Depresi☑️**")
    await typew.edit("**Repan Depresi✅**")
    sleep(2)
    await typew.edit("**Dimas Gajelas☑️**")
    await typew.edit("**Dimas Gajelas✅**")
    sleep(2)
    await typew.edit("**Yoll Mengkesel☑️**")
    await typew.edit("**Yoll Mengkesel✅**")
    sleep(2)
    await typew.edit("**Ryan Hulk Versi Beta!☑️**")
    await typew.edit("**Ryan Hulk Versi Beta!✅**")
    sleep(2)
    await typew.edit("**Shallu ,MengRibet☑️**")
    await typew.edit("**Shallu ,MengRibet✅**")
    sleep(2)
    await typew.edit("**Lapus Mengentot☑️**")
    await typew.edit("**Lapus Mengentot✅**")
    sleep(2)
    await typew.edit("**EL, Si Jutek☑️**")
    await typew.edit("**EL, Si Jutek✅**")
    sleep(3)
    await typew.edit("**Anti Riweh☑️**")
    await typew.edit("**Anti Riweh✅**")
    sleep(3)
    await typew.edit("**Mas Ade ,Bandar Bokep☑️**")
    await typew.edit("**Mas Ade ,Bandar Boke✅p**")
    sleep(3)
    await typew.edit("**CUMA DAPA DOANG YANG BENER!**")
    
@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GUA KELUAR AJA LAH NGENTO**")
    sleep(1)
    await typew.edit("**GC NYA JELEK BAT KONTOL**")


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
