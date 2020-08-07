msg = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal".encode()
k1 = 73     # corresponds to the letter 'I' in ASCII code
k2 = 67     # 'C'
k3 = 69     # 'E'
cpt = 0
output_bytes = b''
for byte in msg:
    if cpt % 3 == 0:
        output_bytes += bytes([k1 ^ byte])
    if cpt % 3 == 1:
        output_bytes += bytes([k2 ^ byte])
    if cpt % 3 == 2:
        output_bytes += bytes([k3 ^ byte])
    cpt += 1
print(output_bytes.hex())