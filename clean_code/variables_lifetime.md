Класс Unit, было:
```
class Unit:

    def __init__(self, name, cost, damage, health, armor):
        self.name = name # название юнита
        self.cost = cost # цена обучения юнита
        self.damage = damage # урон юнита
        self.health = health # здоровье юнита
        self.armor = armor # броня юнита

    def attack(self, target):
        print(f'{self.name} атакует {target.name}')
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage * (1 - self.armor)
        self.health = max(0, self.health)
        print(f'У {self.name} осталось {self.health} здоровья')

    def heal(self, heal):
        self.health += heal
        print(f'{self.name} восстанавливает {heal} здоровья')
```
Cтало:
```
class Unit:

    def __init__(self, name, cost, damage, health, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.health = health
        self.armor = armor

    def attack(self, target):
        self._print_attack(target)
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self._apply_damage(damage)
        self._print_health()

    def heal(self, heal_amount):
        self.health += heal_amount
        self._print_heal(heal_amount)

    def _apply_damage(self, damage):
        self.health -= damage * (1 - self.armor)
        self.health = max(0, self.health)

    def _print_attack(self, target):
        print(f'{self.name} атакует {target.name}')

    def _print_health(self):
        print(f'У {self.name} осталось {self.health} здоровья')

    def _print_heal(self, heal_amount):
        print(f'{self.name} восстанавливает {heal_amount} здоровья')
```
1-4 Все выдаваемые сообщения переведены в приватные методы
5 Добавлен приватный метод для применения урона

Было:
```
    def hash1(self, str1):
        val = 0
        for c in str1:
            code = ord(c)
            val = (val * HASH_CONST_1 + code) % self.filter_len
        return val

    def hash2(self, str1):
        val = 0
        for c in str1:
            code = ord(c)
            val = (val * HASH_CONST_2 + code) % self.filter_len
        return val
```
Стало:
```
    def hash1(self, str1):
        return self._hash(str1, HASH_CONST_1)

    def hash2(self, str1):
        return self._hash(str1, HASH_CONST_2)

    def _hash(self, str1, const):
        val = 0
        for c in str1:
            code = ord(c)
            val = (val * const + code) % self.filter_len
        return val
```
6-7 Для упрощения кода создана приватный метод хэширования

Было
```
total = 0
for number in data:
    total += number
average = total / len(data)
```
Стало
```
def calculate_average(data):
    return sum(data) / len(data)

average = calculate_average(data)
```
8 Убрана лишняя переменная и добавлен метод, который можно использовать далее в коде

Было
```
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)
```
Стало
```
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

common_elements = find_common_elements(list1, list2)
```
9 Упрощен код поиска общих значений в двух списках

10 Выражение
```
for item in data:
    count += 1
```
Заменено на:
```
def count_elements(data):
    return len(data)
```

11 Выражение:
```
keys = []
values = []
for key, value in data.items():
    keys.append(key)
    values.append(value)
```
Заменено на:
```
def process_dict(data):
    keys = list(data.keys())
    values = list(data.values())
    return keys, values
```

Было:
```
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0
    
    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price
        print(f"{item} added to cart.")
```
Стало:
```
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0
    
    def add_item(self, item, price):
        self._update_cart(item, price)
        print(f"{item} added to cart.")

    def _update_cart(self, item, price):
        self.items.append(item)
        self.total_price += price
```
12 Вынес логику обновления корзины в отдельный метод _update_cart, чтобы add_item отвечал только за добавление товара.
  
Было:
```
def get_discount_price(price, is_member):
    discount = 0
    if is_member:
        discount = 0.1
    discounted_price = price * (1 - discount)
    return discounted_price
```
Стало:
```
def get_discount_price(price, is_member):
    if is_member:
        discount = 0.1
    else:
        discount = 0
    discounted_price = price * (1 - discount)
    return discounted_price
```
13 Ограничена область видимости переменной

Было:
```
def calculate_discount(price, is_member):
    discount = 0
    if is_member:
        discount = 0.1
    return price * (1 - discount)
```
Стало:
```
def calculate_discount(price, is_member):
    if is_member:
        discount = 0.1
    else:
        discount = 0
    return price * (1 - discount)
```
14 Определил переменную внутри цикла

Было:
```
class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.total_spent = 0

    def add_order(self, order):
        self.orders.append(order)
        self.total_spent += order.total_cost
```
Стало
```
class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.total_spent = 0

    def add_order(self, order):
        self._update_orders(order)
        self._update_total_spent(order.total_cost)

    def _update_orders(self, order):
        self.orders.append(order)

    def _update_total_spent(self, cost):
        self.total_spent += cost
```
15 Для лучшей наглядности методы были разделены

















