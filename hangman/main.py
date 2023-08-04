import random

def print_hangman():
    current_word = ''
    for char in word.values():
        current_word += char + " "
    print(current_word)
    if mistakes_counter == 0:
        print(f"    ______    ")
        print(f"    |    |    ")
        print(f"         |    ")
        print(f"         |    ")
        print(f"         |    ")
        print(f"        / \   ")
    if mistakes_counter == 1:
        print(f"    ______    ")
        print(f"    |    |    ")
        print(f"    0    |    ")
        print(f"         |    ")
        print(f"         |    ")
        print(f"        / \   ")
    if mistakes_counter == 2:
        print(f"    ______    ")
        print(f"    |    |    ")
        print(f"    0    |    ")
        print(f"    |    |    ")
        print(f"         |    ")
        print(f"        / \   ")
    if mistakes_counter == 3:
        print(f"    ______    ")
        print(f"    |    |    ")
        print(f"    0    |    ")
        print(f"   /|    |    ")
        print(f"         |    ")
        print(f"        / \   ")
    if mistakes_counter == 4:
        print(f"    ______    ")
        print(f"    |    |    ")
        print(f"    0    |    ")
        print(f"   /|\   |    ")
        print(f"         |    ")
        print(f"        / \   ")
    if mistakes_counter == 5:
        print(f"    ______    ")
        print(f"    |    |    ")
        print(f"    0    |    ")
        print(f"   /|\   |    ")
        print(f"   /     |    ")
        print(f"        / \   ")
    if mistakes_counter == 6:
        print(f"    ______    ")
        print(f"    |    |    ")
        print(f"    0    |    ")
        print(f"   /|\   |    ")
        print(f"   / \   |    ")
        print(f"        / \   ")

def check_char(user_input):
    include_flag = False
    global mistakes_counter
    for char in word.keys():
        if char == user_input:
            word[char] = user_input
            include_flag = True
    if include_flag == False:
        mistakes_counter += 1

def play_again():
    play_again = input("Play again?[Y/N]").lower().strip()
    if play_again == 'y':
        init_game()
    exit()
def check_win():
    if mistakes_counter == 6:
        print(F"You lose! The word was {random_word}")
        play_again()
    if "_" not in word.values():
        print(f"You won! The word was {random_word}")
        play_again()
def play():
    while mistakes_counter <= 6:
        user_input = validate_input()  # handle user input
        check_char(user_input)  # check if word include user input
        print_hangman()
        if check_win():
            break
def init_game():
    def get_list_of_words(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().splitlines()

    words = get_list_of_words('words.txt')
    global random_word
    random_word = random.choice(words).lower()

    global mistakes_counter
    mistakes_counter = 0

    global word
    word = {}

    for i in random_word:
        word[i] = "_"
    print_hangman()
    play()


def validate_input():
    user_input = ''
    while len(user_input) != 1:
        user_input = input("Enter char: ").strip().lower()
    return user_input



init_game()







