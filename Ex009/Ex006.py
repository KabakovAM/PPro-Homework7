import random
import os
import string


def create_random_file(folder, extension, min_name, max_name, min_bite, max_bite, file_count):
    name_list = []
    for i in range(file_count):
        for k in range(random.randint(min_name, max_name)):
            letter = random.choice(string.ascii_letters)
            name_list.append(letter)
        name_list.append(extension)
        if not os.path.isdir(folder):
            os.makedirs(folder)
        if ''.join(name_list) in os.listdir(folder):
            return create_random_file(folder, extension, min_name, max_name, min_bite, max_bite, file_count - i)
        name_list.insert(0,'/')
        name_list.insert(0,folder)
        file_name = ''.join(name_list)
        name_list.clear()
        with open(file_name, 'ab') as data_input:
            data_input.write(b'X' * random.randint(min_bite, max_bite))


def create_random_extension(folder, extensions_dic: dict, min_name=6, max_name=30, min_bite=256, max_bite=4096):
    for key, item in extensions_dic.items():
        create_random_file(folder, key, min_name, max_name, min_bite, max_bite, item)


if __name__ == '__main__':
    extensions_dic = {'.jpeg': 3, '.txt': 2, '.md': 1}
    folder = 'C:\\Users\\kabaa\\Desktop\\Python\\Python_pro\\files'
    create_random_extension(folder, extensions_dic)