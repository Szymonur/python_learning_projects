import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
print(nato_dict)

user_input = input("Write your name: ").upper()

user_name_nato = [nato_dict[char] for char in user_input]

print(user_name_nato)
