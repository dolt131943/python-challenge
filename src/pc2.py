encode_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.";

begin_pos = ord('a')
end_pos = ord('z')

decode_str = '';

for ch in encode_str:
    if (ch >= 'a'  and ch <= 'z'):
        decode_str += chr((ord(ch) + 2) % end_pos)
    else:
        decode_str += ch

print decode_str
