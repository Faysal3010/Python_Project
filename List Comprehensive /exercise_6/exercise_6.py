import pandas as pd

df = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

'''one way'''
# example=input("Enter a word: ").upper()
# x=[]
# for letter in example:
#     df_letter = df[df.letter == letter]
#     x.append("".join(df_letter.code.values))
# print(x)

'''two way'''

data_dict = {row.letter: row.code for (index, row) in df.iterrows()}
letters = input("Enter a word: ").upper()
result = [data_dict[letter] for letter in letters]
print(result)
