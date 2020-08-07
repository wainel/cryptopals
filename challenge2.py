def XORHex(hex1, hex2):
    if len(hex1) != len(hex2):
        print("Les deux chaînes de caractères ne sont pas de même longueur")
        return
    b1 = bytes.fromhex(hex1)
    b2 = bytes.fromhex(hex2)
    b3 = bytes([e1 ^ e2 for e1,e2 in zip(b1, b2)])
    print(b3.decode())
    hex3 = b3.hex()
    return hex3


print(XORHex("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965"))