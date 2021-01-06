import pandas

"""Asking for word"""
name = input("Write your word: ").upper()

"""Preparing dictionary of NATO code"""
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index,row) in data.iterrows()}

answer_list = [nato_dictionary[letter] for letter in name]
print(answer_list)
