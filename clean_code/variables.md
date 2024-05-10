1.    Добавлена проверка инвариантов, проверяем корректность границ
``` 
    assert top <= bottom
    assert left <= right
```
2. Добавлена проверка корректных размеров матрицы
```
assert n >= 0 and m >= 0
```
3. В конце работы функции присваиваем недопустивые значения временным переменным
```
    zero_count = -1
    one_count = -1
    max_len = -1
```
4. Инициализирование переменной с атрибутом int
```
    summ: int = 0
```
5. Завершение работы с переменной
```
f_index = index
Цикл
f_index = -1
```
6. Завершение работы с переменной
```
return index
index = 0
```
7. Проверка переменной
```
curr_len = zero_count + one_count
assert curr_len >= 0
```
8. В классе юнит добавлена проверка на отрицательные значения
```
self.health = max(0, self.health)
```
9. Добавлена проверка на отрицательное здоровье
```
def set_health(self, health):
        self.__health += health
        if self.__health <= 0:
            self.__health = 0
```
10. Объявление переменных
```
        self.size: int = sz
        self.slots: list = [None] * self.size
        self.values: list = [None] * self.size
        self.hits: list = [0] * self.size
```
11. Проверка при формировании цены
```
assert final_price > 0
```
12. Объявление переменной перед использованием в цикле
```
lst = []
    for i in os.listdir(path):
        i_path = os.path.join(path, i)
        if os.path.isfile(i_path):
            lst.append(i_path)
```
13. Объявление переменной перед использованием в цикле
```
nodes = []
        node = self.head.next
        while isinstance(node, Node):
            if node.value == val:
                nodes.append(node)
```
14. Объявление переменных
```
    files_ext: list = []
    subdirs: list = []
```
15. Объявление переменной
```
max_str: str = ""
```














