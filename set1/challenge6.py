from binascii import hexlify

def goHAM(txt1,txt2):
    dist = 0
    txt1 = bin(int(hexlify(txt1),16))
    txt2 = bin(int(hexlify(txt2),16))
    for i in range(len(txt1)):
        if txt1[i] != txt2[i]:
            dist += 1
    return dist

txt1 = "this is a test"
txt2 = "wokka wokka!!!"

print(goHAM(txt1,txt2))
