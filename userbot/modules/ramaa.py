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

@register(outgoingg=True, pattern='^.NF(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASSALAMUALAIKUM**")
    sleep(1)
     await typew.edit("**Gua Mau Pantun Nih Gesss**")
    sleep(2)
    await typew.edit("**Ikan Sepat**")
    sleep(2)
    await typew.edit("**Makan Saos**")
    sleep(3)
    await typew.edit("**KENALIN 404 NIH BOS!**")


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
