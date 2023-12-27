import os


def names(path, extension, flag):
    files_ext = []
    subdirs = []
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            subdirs.append(i)
        else:
            if os.path.splitext(i)[1] == extension:
                files_ext.append(i)

    if flag:
        files1 = []
        subdirs1 = []
        for j in subdirs:
            subitems = names(os.path.join(path, j), extension, False)
            files1.extend(subitems[0])
            subdirs1.extend(subitems[1])
        files_ext.extend(files1)
        subdirs.extend(subdirs1)

    return [files_ext, subdirs]


list = names('/Users/Sergei/Documents/GitHub/learning/files', '.txt', True)

print(list)


def delete_dir(path):
    items = os.listdir(path)
    for i in items:
        i_path = os.path.join(path, i)
        if os.path.isdir(i_path):
            #print('В каталоге есть подкаталог')
            return False
    for i in items:
        i_path = os.path.join(path, i)
        os.remove(i_path)
    os.rmdir(path)
    #print('Каталог успешно удален')
    return True


test_del = delete_dir('/Users/Sergei/Documents/GitHub/learning/files/dir2/21')

print(test_del)