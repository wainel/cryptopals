from binascii import unhexlify

my_file = open("8", "r")
ciphertext = [unhexlify(line.strip()) for line in open("8").readlines()]
my_file.close()


def count_repetitions(ciphertext, block_size):
    chunks = [ciphertext[i:i + block_size] for i in range(0, len(ciphertext), block_size)]
    number_of_repetitions = len(chunks) - len(set(chunks))
    result = {
        'ciphertext': ciphertext,
        'repetitions': number_of_repetitions
    }
    return result


# The most significant characteristic of ECB is that if the same b-bit block of plaintext appears more than once in
# the message, it always produces the same ciphertext.
block_size = 16
repetitions = [count_repetitions(cipher, block_size) for cipher in ciphertext]
most_repetitions = sorted(repetitions, key = lambda x: x['repetitions'], reverse= True)[0]
print('Ciphertext: {}'.format(most_repetitions['ciphertext']))
print('Repeating blocks: {}'.format(most_repetitions['repetitions']))