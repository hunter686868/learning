class Heap:
    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        # создаём массив кучи HeapArray из заданного
        heap_size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * heap_size

        for item in a:
            self.Add(item)
        # размер массива выбираем на основе глубины depth

    def GetMax(self):
        if len(self.HeapArray) == 0 or self.HeapArray[0] is None:
            return -1  # если куча пуста

        max_value = self.HeapArray[0]
        last_item_index = len(self.HeapArray) - 1

        # Найти последний элемент в куче
        while last_item_index >= 0 and self.HeapArray[last_item_index] is None:
            last_item_index -= 1

        if last_item_index < 0:
            return -1  # если в куче нет элементов

        # Переместить последний элемент на место корня
        self.HeapArray[0] = self.HeapArray[last_item_index]
        self.HeapArray[last_item_index] = None
        self.heap_down(0)

        return max_value

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if None not in self.HeapArray:
            return False  # если куча вся заполнена

        # Найти первый свободный слот
        index = self.HeapArray.index(None)
        self.HeapArray[index] = key
        self.heap_up(index)
        return True

    def heap_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.HeapArray) and self.HeapArray[left_child_index] is not None \
                and self.HeapArray[left_child_index] > self.HeapArray[largest]:
            largest = left_child_index

        if right_child_index < len(self.HeapArray) and self.HeapArray[right_child_index] is not None \
                and self.HeapArray[right_child_index] > self.HeapArray[largest]:
            largest = right_child_index

        if largest != index:
            self.HeapArray[index], self.HeapArray[largest] = self.HeapArray[largest], self.HeapArray[index]
            self.heap_down(largest)

    def heap_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.HeapArray[parent_index] < self.HeapArray[index]:
            self.HeapArray[parent_index], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

