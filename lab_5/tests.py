from text_method_lib import *

filename = 'alice.txt'
filename_upper = 'alice_upper.txt'
filename_remove = 'alice_remove.txt'
filename_reverse = 'alice_reverse.txt'
filename_encode = 'alice_encode.txt'
filename_decode = 'alice_decode.txt'
filename_complex_encode = 'alice_complex_encode.txt'
filename_complex_decode = 'alice_complex_decode.txt'
filename_diag = 'alice_diag.txt'

#test all_upper_case method
all_upper_case(filename, filename_upper)

#test remove_a_word method
remove_a_word(filename, filename_remove)

#test reverse_file method
reverse_file(filename, filename_reverse)

#test pattern_count method
pattern_count(filename)

#test encode_file method
encode_file(filename, filename_encode)

#test decode_file method
decode_file(filename_encode, filename_decode)

#test complex_encode_file method
complex_encode_file(filename, filename_complex_encode)

#test complex_decode_file method
complex_decode_file(filename_complex_encode, filename_complex_decode)

#test diagonal_text method
diagonal_text(filename, filename_diag)

#test count_all_words method
count_all_words(filename)