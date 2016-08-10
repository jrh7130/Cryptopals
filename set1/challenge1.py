def hextob64(txt):
    return txt.decode("hex").encode("base64").rstrip()

hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

print(hextob64(hex_str))
