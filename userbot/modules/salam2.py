# Gausah kesini ngentot!!
# NGEDIT CMD YG BENER KONTOL!!!


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum ngentoott!! ")


@register(outgoing=True, pattern='^.gjm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("GAK, JANGAN MAKSA!!")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumsalam kontolll...")


@register(outgoing=True, pattern='^.gjn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Gajelas Ngentottt")


@register(outgoing=True, pattern='^.yb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Yabenarrrrrrr...**")


@register(outgoing=True, pattern='^.m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MEMEK NYA ANAK INIIIII....**")


@register(outgoing=True, pattern='^.k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Apalo Kontolll....**")


@register(outgoing=True, pattern='^.gjb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJELAS BABI....**")


@register(outgoing=True, pattern='^.gjk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Gajelas Kontolll....**")


@register(outgoing=True, pattern='^.gbgn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ga banget, Ngentott!!!**")


@register(outgoing=True, pattern='^.gls(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK, LO SANGEAN!!!**")


@register(outgoing=True, pattern='^.bsl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BAU SAWI LO..!!**")


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hai, Anak yatim!!**")


@register(outgoing=True, pattern='^.em(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Eh memek..!!!**")


@register(outgoing=True, pattern='^.eh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH NGENTOT...!**")


@register(outgoing=True, pattern='^.ucp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Lu siapa si ngentooootttt!!!!**")


@register(outgoing=True, pattern='^.hey(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hey, Member Alay..😂**")


@register(outgoing=True, pattern='^.loh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC SAMPAH KAYA GINI, BUBARIN AJA PLIS!!🤣**")

CMD_HELP.update({
    "salam3":
    ".p\
\nUsage:\
\n\n.l\
\nUsage:\
\n\n.gjm\
\nUsage:\
\n\n.gjn\
\nUsage:\
\n\n.gjb\
\nUsage:\
\n\n.yb\
\nUsage:\
\n\n.gjk\
\nUsage:"
})

CMD_HELP.update({
    "salam4":
    ".gbgn\
\nUsage:\
\n\n.bsl\
\nUsage:\
\n\n.hai\
\nUsage:\
\n\n.eh\
\nUsage:\
\n\n.em\
\nUsage:\
\n\n.gls\
\nUsage:\
\n\n.hey\
\nUsage:\
\n\n.loh\
\nUsage:\
\n\n.ucp\
\nUsage:\
\n\n.m\
\nUsage:\
\n\n.k\
\nUsage:"
})
