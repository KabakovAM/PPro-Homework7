import os

def group_rename(folder, *, end_name=None, q_num=None, start_extension=None, end_extension=None, start_name_list=None):
    os.chdir(folder)
    file_list = os.listdir(folder)
    new_name = []
    k = 0
    for i in range(len(file_list)):
        if start_extension:
            if file_list[i].split('.')[1].lower() == start_extension:
                if end_extension:
                    new_name.extend(['.', end_extension])
                else:
                    new_name.extend(['.', file_list[i].split('.')[1].lower()])
            else:
                continue
        else:
            if end_extension:
                new_name.extend(['.', end_extension])
            else:
                new_name.extend(['.', file_list[i].split('.')[1].lower()])
        if q_num:
            if 10**q_num-1 < len(file_list):
                print('Количество файлов превышает заданое количество цифр!')
                return
            else:
                temp = '({}{})'.format('0'*(q_num-len(str(k))), k)
                new_name.insert(0, temp)
                k += 1
        if end_name:
            new_name.insert(0, end_name)
        else:
            if start_name_list:
                new_name.insert(0, file_list[i].split('.')[0][start_name_list[0]:start_name_list[1]])
            else:
                new_name.insert(0, file_list[i].split('.')[0])
        os.rename(file_list[i], ''.join(new_name))
        new_name.clear()


if __name__ == '__main__':
    folder = 'C:\\Users\\kabaa\\Desktop\\Python\\Python_pro\\files'
    group_rename(folder, q_num=4, start_extension='jpg', end_name='Japan')