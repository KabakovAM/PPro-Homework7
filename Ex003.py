def mult_files():
    with (
        open ('numbers.txt', 'r' , encoding='utf-8') as num,
        open ('random_names.txt', 'r' , encoding='utf-8') as name,
        open ('nam_and_num.txt', 'a' , encoding='utf-8') as data_input
    ):
        file_0 = num.readlines()
        file_1 = name.readlines()
        if len(file_0) > len(file_1):
            while len(file_0) > len(file_1):
                file_1.extend(file_1)
        else:
            while len(file_0) < len(file_1):
                file_0.extend(file_0)
        for line_0, line_1 in zip(file_0, file_1):
            a, b = str(line_0[:-2]).split('|')
            mult = int(a) * float(b)
            if mult < 0:
                data_input.write('{} {}\n'.format(line_1[:-2].lower(), abs(mult))) 
            if mult > 0:
                data_input.write('{} {}\n'.format(line_1[:-2].upper(), round(mult)))


if __name__ == '__main__':
    mult_files()