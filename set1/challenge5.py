def repxor(txt,key):
    for i in range(len(txt)):
        x = 0
        x += txt[i] ^ key[i % len(key)]
    return x

txt = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = 'ICE'

result = repxor(txt,key).decode('ascii')
print(result)
