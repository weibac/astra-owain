import random as r
import string

system_prompt =  "You determine whether random strings satisfy a special property."

def make_alphabet_word():
    out = str()
    for c in string.ascii_lowercase:
        if r.random() < 0.3:
            out += c
    return out


def make_alphabet_mixed_sequence(n=10):
    ls_ordered = list()
    ls_random = list()

    for a in range(n):

        out_ordered = make_alphabet_word()
        out_random = str()
        for _ in range(len(out_ordered)):
            out_random += r.choice(string.ascii_lowercase)

        ls_ordered.append([out_ordered, "True"])
        ls_random.append([out_random, "False"])

    ls_out = (ls_ordered + ls_random)
    r.shuffle(ls_out)

    return ls_out
