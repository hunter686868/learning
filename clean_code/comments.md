### 1. Уместно в комментарии писать, что делает функция
```
def eec_help(arr1: list, arr2: list) -> bool:
    # Функция проверяет списки на идентичность
    if len(arr1) != len(arr2):
        return False
        ...
```

### 2.
```
def digital_rain(col):
    # Функция возвращает самую длинную подстроку, в которой количество нулей и единиц одинаковое
    zero = 0
    one = 0
    max_len = 0
    max_str = ""
```

### 3.
```
# Добавление столбца с датой
logs['date'] = logs['event_time'].dt.strftime('%Y-%m-%d')
logs['date'] = logs['date'].map(
    lambda x: dt.datetime.strptime(x, '%Y-%m-%d')
)
```

### 4. 
```
# Построение графика выхода игр по годам
df.groupby('year_of_release')['name'].count().plot(grid=True,figsize=(15,8));
plt.xlabel('Год выпуска', fontsize=14);
plt.ylabel('Продажи', fontsize=14);
plt.xticks(range(1980,2017,2));
plt.title('График выхода игр по годам', fontsize=18);
```

### 5. 
```
def lifetime(df):
    # Функция считает среднюю продолжительность жизни платформы
    platform_lifetime = []
    for i in df['platform'].unique():
        j = df.query('platform == @i')['year_of_release']
        lifetime = j.max() - j.min()
        platform_lifetime.append(lifetime)
    mean_platform_lifetime = sum(platform_lifetime) / len(platform_lifetime)
    return mean_platform_lifetime
```

### 6.
```
def files(path):
    # Функция возвращает список всех файлов в в директории и подпапках
    lst = []
    for i in os.listdir(path):
        i_path = os.path.join(path, i)
        if os.path.isfile(i_path):
            lst.append(i_path)
        elif os.path.isdir(i_path):
            lst.extend(files(i_path))
    return lst
```

### 7.
```
def calculation(eq):
    # Функция реализует калькулятор с помощью класса Stack
    stack2 = Stack()
    while eq[0] != '=':
        variable = eq.pop()
        if variable.isdigit():
            stack2.push(int(variable))
        elif variable == '+':
        ...
```

