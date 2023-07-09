import random
import string


def create_random_file(extension, min_name, max_name, min_bite, max_bite, file_count):
    name_list = []
    for i in range(file_count):
        for k in range(random.randint(min_name, max_name)):
            letter = random.choice(string.ascii_letters)
            name_list.append(letter)
        name_list.append(extension)
        file_name = ''.join(name_list)
        name_list.clear()
        with open(file_name, 'ab') as data_input:
            data_input.write(b'X' * random.randint(min_bite, max_bite))


def create_random_extension(extensions_dic: dict, min_name=6, max_name=30, min_bite=256, max_bite=4096):
    for key, item in extensions_dic.items():
        create_random_file(key, min_name, max_name, min_bite, max_bite, item)


if __name__ == '__main__':
    extensions_dic = {'.jpeg': 3, '.txt': 2, '.md': 1}
    create_random_extension(extensions_dic)