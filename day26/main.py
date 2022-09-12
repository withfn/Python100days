import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

df_dict = {row.letter:row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    try:
        user_input = input("Type a word: ").upper()
        user_code = [df_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(user_code)
    
generate_phonetic()

