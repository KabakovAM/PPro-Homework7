import os
FOLDER_DIC = {'mp4':'video', 'txt':'text', 'md':'text', 'jpeg':'foto', 'bmp':'foto'}


def file_sort(folder):
    os.chdir(folder)
    file_list = os.listdir(folder)
    for i in range(len(file_list)):
        file_list[i] = file_list[i].split('.')
        if file_list[i][1] in FOLDER_DIC:
            if not os.path.isdir(FOLDER_DIC[file_list[i][1]]):
                os.makedirs(FOLDER_DIC[file_list[i][1]])
            os.replace('.'.join(file_list[i]), FOLDER_DIC[file_list[i][1]])
    print(list(FOLDER_DIC.values()))


if __name__ == '__main__':
    folder = 'C:\\Users\\kabaa\\Desktop\\Python\\Python_pro\\files'
    file_sort(folder)