import codecs


def convert_hex_to_b64(hex_string):
    b64 = codecs.encode(codecs.decode(hex_string, 'hex'), 'base64').decode()
    return b64


print(convert_hex_to_b64(
    "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
