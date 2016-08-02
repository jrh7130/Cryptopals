def hextob64(a):
    return a.decode("hex").encode("base64")

hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

print(hextob64(hex_str))

for i in range(256):
    l = len(hex_str)
    b = int(("%02x" % i)*l,16)
    c = "%02x" % i
    print(c)
