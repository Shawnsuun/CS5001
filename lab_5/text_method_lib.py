import string

#converts everything in in_file to upper case and saves it in out_file
def all_upper_case(in_file, out_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		upper_contents = contents.upper()
	with open(out_file, 'w') as file_object:
		file_object.write(upper_contents)


#gets as input a word, removes it from the input file, and writes in out_file
def remove_a_word(in_file, out_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		removed_word = input('Please input the word that you want to remove:\n')
		contents_removed = contents.replace(removed_word, '')
	with open(out_file, 'w') as file_object:
		file_object.write(contents_removed)


#reverses the content of in_file by word not letter, writes it out as out_file 
def reverse_file(in_file, out_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		rev_words = contents.split(' ')
		rev_words.reverse()
		contents_reversed = ' '.join(rev_words)
	with open(out_file, 'w') as file_object:
		file_object.write(contents_reversed)


#gets as input a word and prints how many time that pattern occurs
def pattern_count(in_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		word = input('Please input the word you want to count:\n')
		counts = contents.count(word)
		print(f"{word} appearing time(s): {counts}")


#count word number of the in_file
def count_all_words(in_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		words = contents.split(' ')
		counts = len(words)
		print(f"File {in_file} have {counts} word(s)\n")


#Encode the in_file by shifting letters backward 1, saves it in out_file 
def encode_file(in_file, out_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		contents_encode = caesar_clipher(contents, 1)
	with open(out_file, 'w') as file_object:
		file_object.write(contents_encode)


#Decode the in_file by shifting letters backward 1, saves it in out_file
def decode_file(in_file, out_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		contents_decode = caesar_clipher(contents, -1)
	with open(out_file, 'w') as file_object:
		file_object.write(contents_decode)


#A more complex way to encode in_file
#Shift letters forward in each word according word's length
#reverse the whole content by word and saves it in out_file
def complex_encode_file(in_file, out_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		words = contents.split(' ')
		new_words = []
		for word in words:
			new_word = caesar_clipher(word, len(word) % 26)
			new_words.append(new_word)
		new_words.reverse()
		contents_complex_encode = ' '.join(new_words)
	with open(out_file, 'w') as file_object:
		file_object.write(contents_complex_encode)


#A more complex way to decode in_file
#Shift letters backward in each word according word's length
#reverse the whole content by word and saves it in out_file
def complex_decode_file(in_file, out_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		words = contents.split(' ')
		new_words = []
		i = 0
		for word in words:
			new_word = caesar_clipher(word, -len(word) % 26)
			new_words.append(new_word)
		new_words.reverse()
		contents_complex_decode = ' '.join(new_words)
	with open(out_file, 'w') as file_object:
		file_object.write(contents_complex_decode)


#helper method to shift letters according to a given pace
def caesar_clipher(contents, pace):
	contents_clipher = ''
	for ch in contents:
		ascii_num = ord(ch)
		if ch in string.ascii_uppercase or ch in string.ascii_lowercase:
			if ch in string.ascii_uppercase:
				ascii_start = 65
			elif ch in string.ascii_lowercase:		
				ascii_start = 97
			num = (ascii_num - ascii_start + 26 + pace) % 26
			ch = chr(num + ascii_start)
		contents_clipher += ch;
	return contents_clipher

#converts contents in in_file to diagonal text and saves it in out_file
def diagonal_text(in_file, out_file):
	with open(in_file) as file_object:
		contents = file_object.read()
		wave_contents = ''
		words = contents.split(' ')
		n = 1
		for word in words:
			wave_contents += ' ' * n
			wave_contents += word
			wave_contents += '\n'
			n += 1
			n %= 30
	with open(out_file, 'w') as file_object:
		file_object.write(wave_contents)