### 1. В классе Queue вместо массива используем deque из модуля collections 
```
class Queue:
    def __init__(self):
        self.queue = []
```

```
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
```

### 2. В классе Deque вместо массива используем deque из модуля collections 
```
class Deque:
    def __init__(self):
        self.deque = []
```

```
from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()
```


### 3. Использование цикла без прямой индексации
```
def delete_dir(path):
    items = os.listdir(path)
    for i in range(len(items)):
        i_path = os.path.join(path, items[i])
```

```
def delete_dir(path):
    items = os.listdir(path)
    for i in items:
        i_path = os.path.join(path, i)
```

### 4. Использование Counter для подсчета частоты встречающихся элементов

```
frequency = {}
for el in elements:
    if el in frequency:
        frequency[el] += 1
    else:
        frequency[el] = 1
```

```
from collections import Counter

...
frequency = Counter(elements)
```

### 5. Использование set для нахождения уникальных значений

```
unique_elements = []
for el in elements:
    if el not in unique_elements:
        unique_elements.append(el)
```

```
unique_elements = set(elements)
```
























