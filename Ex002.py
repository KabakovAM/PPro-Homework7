import random
import string


def random_names():
    name_list = []
    vowels = ['e','y','u','i','o','a']
    check_vowels = False
    for i in range(random.randint(4, 7)):
        letter = random.choice(string.ascii_letters)
        if letter in vowels and check_vowels == False:
            check_vowels = True
        letter = letter.lower()
        if i == 0:
            name_list.append(letter.upper())
        else:
            name_list.append(letter)
        if check_vowels == False:
            return random_names()
    with open('random_names.txt', 'a', encoding='utf-8') as data_input:
        data_input.write(f'{"".join(name_list)}\n')


if __name__ == '__main__':
    random_names()