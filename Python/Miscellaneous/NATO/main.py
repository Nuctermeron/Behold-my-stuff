import pandas

"""Preparing dictionary of NATO code"""
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter:row.code for (index,row) in data.iterrows()}

"""Asking for word"""
def get_pho():
    name = input("Write your word: ").upper()
    try:
        answer_list = [nato_dictionary[letter] for letter in name]
    except KeyError:
        print("Write text, please")
        get_pho()
    else:
        print(answer_list)

get_pho()
