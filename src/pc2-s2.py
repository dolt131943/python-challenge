import string
encode_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


from_chrs = "abcdefghijklmnopqrstuvwxyz"
to_chrs = "cdefghijklmnopqrstuvwxyzab"
tran_tab = string.maketrans(from_chrs, to_chrs)

decode_str = encode_str.translate(tran_tab)

print decode_str
