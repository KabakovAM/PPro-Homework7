from random import randint, random


def add_num_to_file(count, file_name):
    with open(file_name, 'a', encoding='utf-8') as data_input:
        for _ in range(count):
            temp = '{}|{}\n'.format(randint(-1000, 1000), randint(-1000, 1000) * random())
            data_input.write(temp)


if __name__ == '__main__':
    add_num_to_file(10, 'numbers.txt')
    