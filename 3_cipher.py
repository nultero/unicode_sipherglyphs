#this is where I copied chars to keep in the final cipher
#dedupe & package.py are just imported and called instead of keeping them in separate scripts

from dedupe import dedupe
from package import package

cipher_abstract = """⊡⍿⁖∔⊙⊡⋵◬⚆⟇⟐⟓⟔⨀⨃⨥⨰⩀⪽⪾⫃⫄⸬⸭ꄍꜾ𐄁⌽⌾⍉⍜⏀⏁፧⏂⏣◵◶⥁⦲⦵⦺⧂⧲⨭⨮⬰⭗⭘𑗘𝌇🕁𒑢𒑰⊾⦑⦒⦝𐰦𐰬⸁⸖𑨿𑩆𑩃⑂⑃ꉽ᪥᪤᪣𑴈⍻꥟𑅃𑗉𑗌𑱬߹ᚖ""" 

# cipherkeys_nord = """
# 𐲍𐲎𐲖𐲛𐲢𐲤𐲦𐲨𐲫𐲮𐲰𐩢𐪂𐪕𐪘𐪙𐪛𐪞𐪟𐰊𐰌𐰍𐰎𐰚𐰛𐰲𐰳𐰶𐰷
# """

cipherkeys_arrows = """⧊ꥃ⋖⋗❮❯⩿⪀⪗⪘᚛᚜⦤⦥⥈⥉⩑⩒⦡⦢⦣Ⲵ𐌞𐍠"""

cipherkeys_tabular = """
𑩃⑂⑃𑴈〒ᚚᚑ ᚁᚂᚃᚆᚇᚈᚋᚌᚍᚎᚐᚑᚒᚓ
""" #ogham

cipherkeys_jagged = """
ꤰꤱꤲꤳꤴꤸꤹꤺꤻꤼꤽꥀꥁꥂꥄꥅꥆꥇ
""" #rejang

cipherkeys_tif = """ⴱⴲⴳⴴⴵⴶⴷⴸⴹⴺⴼⴽⴾⴿⵀⵁⵃⵄⵅⵆⵇⵈⵉⵊⵋⵌⵍⵎⵐⵒⵓⵖⵗⵘⵙⵚⵛⵜⵝⵞⵟⵠⵡⵢⵣⵤⵥⵦ""" #tifinagh

cipherkeys_hid = """​𐒱""" #this one is for testing the invisible middle cipher mediator

# cipherkeys = """""" + cipher_abstract + cipherkeys_nord + cipherkeys_tif
cipherkeys = """""" + cipher_abstract + cipherkeys_tif + cipherkeys_arrows + cipherkeys_hid
num = 0
for i in cipherkeys:
    print(f"{num} : {i}")
    num += 1
# print(f"CipherKeys len is {len(cipherkeys)}")
# deduped = dedupe(cipherkeys)
# package(deduped, flag="to_cipher")