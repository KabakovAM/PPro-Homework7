import random
import string


def create_random_file(extension, min_name=6, max_name=30, min_bite=256, max_bite=4096, file_count=42):
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


if __name__ == '__main__':
    create_random_file(extension = '.txt', file_count = 5)