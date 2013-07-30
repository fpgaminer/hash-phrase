# Released into the Public Domain by fpgaminer@bitcoin-mining.com


import hashlib
import math
import sys
from pbkdf2 import pbkdf2_hex


def load_dictionary (dictionary_file=None):
	if dictionary_file is None:
		dictionary_file = "words.txt"

	with open (dictionary_file, 'rb') as f:
		dictionary = f.read ().splitlines ()
	
	return dictionary


def default_hasher (data):
	return pbkdf2_hex (data, '', iterations=50000, keylen=32, hashfunc=hashlib.sha256)


def hash_phrase (data, minimum_entropy=64, dictionary=None, hashfunc=default_hasher):
	# Dictionary
	if dictionary is None:
		dictionary = load_dictionary ()
	
	dict_len = len (dictionary)
	entropy_per_word = math.log (dict_len, 2)
	num_words = int (math.ceil (minimum_entropy / entropy_per_word))

	# Hash the data and convert to a big integer (converts as Big Endian)
	hash = hashfunc (data)
	available_entropy = len (hash) * 4
	hash = int (hash, 16)

	# Check entropy
	if num_words * entropy_per_word > available_entropy:
		raise Exception ("The output entropy of the specified hashfunc (%d) is too small." % available_entropy)

	# Generate phrase
	phrase = []

	for i in range (num_words):
		remainder = hash % dict_len
		hash = hash / dict_len

		phrase.append (dictionary[remainder])
	
	return " ".join (phrase).lower().capitalize()


if __name__ == "__main__":
	if len (sys.argv) != 2:
		print "USAGE: hash-phrase.py DATA"
		sys.exit (-1)
	
	print hash_phrase (sys.argv[1])
