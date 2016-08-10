from binascii import hexlify

def genkey(txt,key):
    while len(key) != len(txt):
        for i in range(len(key)):
            if len(key) == len(txt):
                break
            key = key + key[i]
    return key

def repxor(txt,key):
    txt = hexlify(txt)
    key = hexlify(key)
    key = genkey(txt,key)
    txt = int(txt,16)
    key = int(key,16)
    result = hex(txt ^ key)
    return result[2:-1]

txt = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = 'ICE'

result = repxor(txt,key)
print(result)
