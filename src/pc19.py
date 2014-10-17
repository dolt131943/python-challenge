import base64,utils,re

'''
str = utils.getUrlToStr('http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html')

encode_str = re.search('base64\n\n(.*)\n\n--============', str, re.S).group(1)

f = open('pc19.wav', 'wb')
f.write(base64.decodestring(encode_str))
f.close()
'''

import wave

w1 = wave.open('pc19.wav')
w1frames = w1.readframes(w1.getnframes())
w1.close()

w2 = wave.open('pc19-2.wav','w')
w2.setnchannels(1)
w2.setsampwidth(w1.getsampwidth())
w2.setframerate(w1.getframerate()//2)
w2.writeframes(w1frames[0::2])

w2.close()



