### 1. Раннее связывание
Для небольшой программы можем использовать константы, которые закодируем в начале кода, например в фильтре блума.  
Часто менять их не нужно, поэтому целесообразно обозначить их в начале.  
```
HASH_CONST_1 = 17
HASH_CONST_2 = 223
class BloomFilter:
....
```
### 2. Связывание во время выполнения программы
При работе парсера логично брать данные для парсинга из отдельного файла, в котором можно потом менять параметры
```
def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, value = line.strip().split('=')
            config[name] = value
    return config

# Чтение параметров из файла config.txt
config = read_config('config.txt')

APP_ID = config['APP_ID']
TOKEN = config['TOKEN']
MY_ID = config['MY_ID']
FRIEND_ID = config['FRIEND_ID']
WORDS_COUNT = int(config['WORDS_COUNT'])
```
### 3. Связывание во время компиляции
Пока самое распространенное в моем коде - при создании функции задаем параметры  
Удобно, наглядно. При необходимости можно переопределить при создании очередного экземпляра.

```
class Squad:

    def __init__(self, player, name= 'Random player', gold= 10000):
        self.player = player # чей отряд
        self.name = name # название отряда
        self.gold = gold # количество золота на старте
        self.units = []
```





