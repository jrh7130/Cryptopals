def xor(a,b):
    if len(a) != len(b):
        raise Exception("Unequal length")
    else:
        a = int(a,16)
        b = int(b,16)
        x = hex(a ^ b)
    return x[2:-1]

a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"

print(xor(a,b))
