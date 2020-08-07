from challenge3 import get_english_score
from challenge3 import single_char_xor


def test(hexstring):
    ciphertext = bytes.fromhex(hexstring)
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


def position_maximum(l):
    # we suppose every element in l is a positive integer
    # we suppose every element in l is distinct
    m = 0
    j = 0
    for i in range(len(l)):
        if l[i] > m:
            m = l[i]
            j = i
    return j


my_file = open("4", "r")
content = my_file.read()
# we create a list with an element = a line in the file
L = content.split('\n')
# type(L) = list ; type(content) = str
L2 = []     # list of the potential encrypted message
L3 = []     # list of the associated keys
L4 = []     # list of the associated scores, to see which one has the best one
for line in L:
    L2.append(test(line)[0])
    L3.append(test(line)[1])
for ele in L2:
    L4.append(get_english_score(ele))
position = position_maximum(L4)
print("The following string: ", L[position], "of the file has been encrypted by key: ", L3[position], ". \nThe "
                                                                                                      "original "
                                                                                                      "message was: "
                                                                                                      "", L2[position])
my_file.close()