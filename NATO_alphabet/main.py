import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
print(nato_dict)


def generate_phonetic():
    try:
        user_input = input("Write your name: ").upper()
        user_name_nato = [nato_dict[char] for char in user_input]
    except KeyError:
        print("Incorrect name!")
        generate_phonetic()
    else:
        print(user_name_nato)


generate_phonetic()
