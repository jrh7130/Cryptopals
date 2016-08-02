freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}

def xor(a,b):
    if len(a) != len(b):
        raise Exception("Unequal length")
    else:
        a = int(a,16)
        b = int(b,16)
        x = hex(a ^ b)
    return x[2:-1]

def genkey(a,b):
    return b * (len(a) / 2)

def scharxor(a):
    a = a.rstrip()
    best_score = 0
    best_str = ""
    for i in range(256):
        x = genkey(a,hex(i)[2:])
        try:
            curr_str = xor(a,x).decode("hex")
        except:
            continue
        curr_score = score(curr_str)
        if curr_score >= best_score:
            best_score = curr_score
            best_str = curr_str
    return best_str.rstrip()

def score(a):
    score = 0
    for i in a:
        if i.lower() in freqs:
            i = i.lower()
            score += freqs[i]
    return score

def detectscharxor():
    best_str = ""
    best_score = 0
    with open("set1.txt") as f:
        for line in f:
            result = scharxor(line)
            if score(result) > best_score:
                best_score = score(result)
                best_str = result
    return best_str

print(detectscharxor())
