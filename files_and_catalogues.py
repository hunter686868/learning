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

list = names('C:\Users\hunter\PycharmProjects\learning\files', '.txt', True)

print(list)
