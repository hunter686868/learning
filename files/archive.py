from zipfile import ZipFile
import os


def arch(name, extension):
    curr_path = os.getcwd()
    files = os.listdir(curr_path)
    path = f'{name}.zip'
    with ZipFile(path, 'w') as tstzip:
        for i in files:
            if i.endswith(extension):
                tstzip.write(i)


arch('tst', '.txt')

# Проверим, что функция добавила в архив
path = os.getcwd()
with ZipFile(f'{path}/tst.zip') as testzip:
    print(testzip.namelist())
