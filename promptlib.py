import random as r
import string
import constants as c

system_prompt =  "You determine whether the strings given to you satisfy a special property. You output True if the property is satisfied, and False if it is not." 
correct_prompt = "Yes, that's correct. Now please describe the special property in your own words."

###
# Alphabet task: 
# Over the space of random strings of lowercase letters, 
# Some have their letters in alphabetical order. Those have the True label.
###

def make_alphabet_word(p=c.ALPHABET_P):
    out = str()
    for c in string.ascii_lowercase:
        if r.random() < p:
            out += c
    return out

def make_alphabet_mixed_sequence(n=c.ALPHABET_N):
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


###
# Digits task: 
# Over the space of random strings of number characters, 
# Some have them sorted by numerical order. Those have the True label.
###

def make_digits_word(p=c.DIGITS_P):
    out = str()
    for c in string.digits:
        if r.random() < p:
            out += c
    return out

def make_digits_mixed_sequence(n=c.DIGITS_N):
    ls_ordered = list()
    ls_random = list()

    for a in range(n):

        out_ordered = make_digits_word()
        out_random = str()
        for _ in range(len(out_ordered)):
            out_random += string.digits.pop(r.choice(range(len(string.digits)))) + " "

        ls_ordered.append([out_ordered, "True"])
        ls_random.append([out_random, "False"])

    ls_out = (ls_ordered + ls_random)
    r.shuffle(ls_out)

    return ls_out


###
# DEPRECATED
# Alphabet-words task:
# Over the space of random sequences of lowercase english words,
# Some of them are ordered alphabetically. Those have the True label.
# words taken from https://www.mit.edu/~ecprice/wordlist.10000 credit: Eric Price
# curated manually to remove porn terms, stray letters, abbreviations and even some spanish words.
# about 1000 words removed.
###

def make_alphabet_words_sentence(word_list, p=c.ALPHABET_WORDS_P):
    out = str()
    n_words = 0
    for w in word_list:
        if r.random() < p:
            out += w + " "
            n_words += 1
    out = out[:-1]
    return out, n_words

def make_alphabet_words_mixed_sequence(n=c.ALPHABET_WORDS_N):
    with open("data/words_10000.txt") as f:
        word_list = [word.strip("\n") for word in f.readlines()]
    ls_ordered = list()
    ls_random = list()

    for a in range(n):

        out_ordered, n_words = make_alphabet_words_sentence(word_list)
        out_random = str()
        for _ in range(n_words):
            out_random += word_list.pop(r.choice(range(len(word_list)))) + " "
        out_random = out_random[:-1]

        ls_ordered.append([out_ordered, "True"])
        ls_random.append([out_random, "False"])

    ls_out = (ls_ordered + ls_random)
    r.shuffle(ls_out)

    return ls_out


###
# Variable-length word sequence task:
# Over the space of random sequences of lowercase english words,
# Some of them are a lot longer than others. Those have the True label.
###

###
# TODO
# Spanish-gender task:
# Nouns in Spanish are grammatically either masculine or feminine.
# Over the space of random sequences of spanish words nouns,
# Some of them have more than 80% of their nouns being feminine. Those have the True label.
###