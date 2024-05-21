### 1.

```
    def hash_fun(self, value):
        # Вычисление хэш-значения для строки (1)
        ...
```

### 2, 3.

```
    def put(self, value):
        # Вставка значения в кеш (2)
        index = self.seek_slot(value)
        if index is not None:
            # Найден пустой слот (5)
            ...
```

### 4.

```
        if self.slots[index] == value:
            # Значение найдено после пробирования (5)
            self.hits[index] += 1
            return index
```

### 5.

```
def func(s1, s2):
    # Проверка вхождения строки s2 в строку s1 (2)
    ...
```

### 6-7.

```
            if s1[i + j] != s2[j]:
                # Прекращаем текущую итерацию, если символы не совпадают (3)
                break
            if j == len(s2) - 1:
                # Возвращаем True, если нашли подстроку s2 в s1 (5)
                return True
```

### 8.

```
    for root, dirs, files in os.walk(path):
        # Проход по всем файлам и каталогам (2)
        if root == path or flag is True:
            ...
```

### 9.

```
        elif os.path.isdir(i_path):
            # Рекурсивный вызов для обработки подкаталогов (2)
            find_files(i_path, lst)
```

### 10.

```
# Получаем сообщения по 200 штук за раз (2)
for i in range(1, requestCount + 1):
    history = session_api.messages.getHistory(count=200, peer_id=user_id, start_message_id=200 * i);
    history = history['items'];
    for j in reversed(history):
        f.write(str(j) + "\n");
    print(str(i) + " out of " + str(requestCount));
```

### 11.

```
# Считаем стоп-слова (1)
ffile = codecs.open('stopwords.txt', 'r', encoding='utf8')
try:
    stops = ffile.read()
finally:
    ffile.close()
```

### 12.

```
# Токенизация текста (1)
text_tokens = word_tokenize(text)
text = nltk.Text(text_tokens)
```



























