from challenge3 import get_english_score
import base64


def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value.
    """
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes


def test(ciphertext):
    potential_messages = []
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        score = get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
        }
        potential_messages.append(data)
    best_score = sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]
    return best_score['message'], best_score['key']


def hamming_distance(ch1, ch2):
    dist = 0
    # zip('ABCD', 'xy') --> Ax By
    for b1, b2 in zip(ch1, ch2):
        difference = b1 ^ b2
        dist += sum([1 for bit in bin(difference) if bit == "1"])
    return dist


print(hamming_distance("this is a test".encode(), "wokka wokka!!!".encode()))


def repeating_key_xor(message_bytes, key):
    """Returns message XOR'd with a key. If the message, is longer
    than the key, the key will repeat.
    """
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes


def break_repeating_key_xor(ciphertext):
    average_distances = []
    # I try to discover the length of the key with the 1st method
    # The KEYSIZE with the smallest normalized edit distance is probably the key.
    for key_size in range(2, 41):
        distances = []
        chunks = [ciphertext[i:i + key_size] for i in range(0, len(ciphertext), key_size)]
        while True:
            try:
                chunk_1, chunk_2 = chunks[0], chunks[1]
                distance = hamming_distance(chunk_1, chunk_2)
                distances.append(distance / key_size)
                del chunks[0]
                del chunks[1]
            except Exception as e:
                break
        result = {
            'key': key_size,
            'avg distance': sum(distances) / len(distances)
        }
        average_distances.append(result)
    possible_key_lengths = sorted(average_distances, key=lambda x: x['avg distance'])[0]
    possible_plaintext = []
    key = b''
    possible_key_length = possible_key_lengths['key']

    for i in range(possible_key_length):
        block = b''
        for j in range(i, len(ciphertext), possible_key_length):
            block += bytes([ciphertext[j]])
        key += bytes([test(block)[1]])

    possible_plaintext.append((repeating_key_xor(ciphertext, key), key))
    return max(possible_plaintext, key=lambda x: get_english_score(x[0]))


my_file = open("6", "r")
ciphertext = base64.b64decode(my_file.read())
plaintext, key = break_repeating_key_xor(ciphertext)
print("Key: {}\nMessage: {}".format(key, plaintext))
my_file.close()