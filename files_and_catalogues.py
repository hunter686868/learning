import os


def names(path, extension, flag):
    files_ext = []
    subdirs = []
    for root, dirs, files in os.walk(path):
        if root == path or flag is True:
            for i in files:
                ext = os.path.splitext(i)[1]
                if ext == extension:
                    files_ext.append(i)
            for j in dirs:
                subdirs.append(j)
    return [files_ext, subdirs]


list = names('/Users/Sergei/Documents/GitHub/learning/files', '.txt', True)

print(list)


def delete_dir(path):
    items = os.listdir(path)
    for i in items:
        i_path = os.path.join(path, i)
        if os.path.isdir(i_path):
            print('В каталоге есть подкаталог')
            return False
    for i in items:
        i_path = os.path.join(path, i)
        os.remove(i_path)
    os.rmdir(path)
    print('Каталог успешно удален')
    return True


test_del = delete_dir('/Users/Sergei/Documents/GitHub/learning/files/dir2/21')

print(test_del)
