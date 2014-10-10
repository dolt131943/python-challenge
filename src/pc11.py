
# look-and-say sequence(1,11,21,1211,111221,...)

seq_num = "1"

pos = 31

for i in range(1, pos):
    last_ch = seq_num[0]
    ch_cnt = 1
    this_num = ''
    
    for ch in (seq_num[1:]):
        if last_ch != ch:
            this_num += str(ch_cnt) + last_ch
            last_ch = ch
            ch_cnt = 1
        else:
            ch_cnt += 1

    this_num += str(ch_cnt) + last_ch
    seq_num = this_num

    # print "%d -> %s" % (i, seq_num)
            

print len(seq_num)
