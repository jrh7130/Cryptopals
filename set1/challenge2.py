def xor(txt,key):
    if len(txt) != len(key):
        raise Exception("Unequal length")
    else:
        txt = int(txt,16)
        key = int(key,16)
        result = hex(txt ^ key)
    return result[2:-1]

txt = "1c0111001f010100061a024b53535009181c"
key = "686974207468652062756c6c277320657965"

print(xor(txt,key))
