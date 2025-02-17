# Filename: vigenere.py
# Author: MATH 4175 Group 7 (Andrew Tran, Anthony Tran, Jack Greer, Jason Pak, Michael Peters)
# Date: 23 Sep 2022 (Date Last Modified: 23 Sep 2022, Jack Greer)
# Description: This file contains a Python algorithm that can decrypt a Vigenere cipher.

plain_to_cipher_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}

cipher_to_plain_dict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}

letter_frequencies_dict = {"A": 0.082, "B": 0.015, "C": 0.028, "D": 0.043, "E": 0.127, "F": 0.022, "G": 0.020, "H": 0.061, "I": 0.070, "J": 0.002, "K": 0.008, "L": 0.040, "M": 0.024, "N": 0.067, "O": 0.075, "P": 0.019, "Q": 0.001, "R": 0.060, "S": 0.063, "T": 0.091, "U": 0.010, "W": 0.023, "X": 0.001, "Y": 0.020, "Z": 0.001}
letter_frequencies_list = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.010, 0.023, 0.001, 0.020, 0.001]

# Return the modulus 26 of num
def mod_26(num):
    return num % 26

# For a key length m, return a list of m substrings
def get_substring_list(txt_string, m):
    substring_list = []
    for n in range(m):
        substring_list.append(get_substring_yn(txt_string, n, m))
        # print("String y_" + str(n+1) + ": " + str(substring_list[n]))

    #Output
    print("For m = "+ str(m) +":")
    for n in range(m):
        output_part1(substring_list[n],n+1)

    return substring_list
        
# Return a substring y_n of txt_string, consisting of every m-th letter of txt_string, offset by
# n. For example, if m = 3, and plaintext = "jasonloudpak"
# "jas onl oud pak"
# y1 = "joop"
# y2 = "anua"
# y3 = "sldk"
def get_substring_yn(txt_string, n, m):
    #arr[start:stop:step]
    string_yn = txt_string[(n)::m]
    return string_yn

# Output for part 1.
def output_part1(txt_string, n):
    print("Substring (y_"+ str(n) + "): ")
    print(txt_string)
    # print("Index of Coincidence: "+ get_index_of_coincidence(txt_string))

# Given a text string, return the frequency of each letter in that string
def get_frequency(txt_string):
    # Create list which contains frequency of each letter (consider making this a map)
    alphabet_frequency = [0] * 26
    # TODO: Iterate through text string, and fill out alphabet_frequency[]
    for i in range(26):
        # substring with one letter 'A' shifted by index i (how to do that? idk)
        letter = chr(i + 65)
        print(letter)
        alphabet_frequency[i] = str.count(letter)
    return alphabet_frequency

# Given a text string, 
def get_index_of_coincidence(txt_string):
    alphabet_freq = get_frequency(txt_string)
    print(alphabet_freq)

    # Numerator: Sum of nC2 for each letter (e.g. if txt_string = "AABBBC", num = (2*1) + (3*2) + (1*0) = 8)
    numerator = 0
    for i in range(len(alphabet_freq)):
        numerator += alphabet_freq[i] * (alphabet_freq[i] - 1)
    
    # TODO: get proper length function
    denominator = len(txt_string) * (len(txt_string) - 1)

    return (numerator / denominator) 

#
def take_dot_product(txt_substring, letter_frequencies):
    print("sneed's feed and seed")
    #sum([i * j for (i, j) in zip(, )])
    
# Create the table
def create_table():
    print("sneed's feed and seed")
    

# Part 1
# Suppose we made a guess by other methods that the key word length
# is 7.
# Calculate the index of coincidences for the above ciphered text by assuming m = 6, 7, 8 and verify
# that the index of coincidences method supports our guess that m = 7. You may manually type the
# reason why your calculations below support our guess.

    # Step 1: m = 6
    # Split the cipher text into six substrings y1, y2, ..., y6,
    # as explained in the class, and calculated index of coincidence
    # for each string. You will have to list six #s here, not just
    # their average.

    # Step 2: m = 7
    # Split the cipher text into seven substrings y1, ..., y7 as
    # explained in the class, and calculate the index of coincidence
    # for each substring. You will have to get seven numbers here.

    # Step 3: m = 8
    # Split the cipher text into eight substrings y1, ..., y8 as
    # explained in the class, and calculate the index of coincidence
    # for each substring. You will have to get eight numbers here.

# Part 2
# Create a table with 7 columns (one for each substring y1, y2, y3, y4, y5, y6, y7 as given in
# slide 26 of sec2.4.pdf in class notes. By using the table, find the keyword. Your keyword should be
# a meaningful English word. If your keyword is correct, it should lead you to a meaningful plaintext.

# Part 3
# By using your keyword, decrypt the given cipher text. You should include spaces between
# words and insert period (.) at the end of each sentence and capitalize the first letter of each sentence
# so that the grader should be able to read your plaintext easily. Otherwise, points will be reduced.
# Your plaintext should be typed and neatly formatted to receive full credit.

sample_text = "JASONLOUDPAK"
print(sample_text)
get_substring_list(sample_text, 6)

sample_frequency = get_frequency(sample_text)
#print(sample_frequency)

# if __name__ == '__main__':
#     sample_text = "jasonloudpak"
#     get_substring_list(sample_text, 3)
    