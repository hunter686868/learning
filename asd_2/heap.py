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
        if self.HeapArray is None or self.HeapArray[0] is None:
        # вернуть значение корня и перестроить кучу
            return -1  # если куча пуста

        max_value = self.HeapArray[0]

        for index in range(1, len(self.HeapArray)):
            self.HeapArray[index - 1] = self.HeapArray[index]
        self.HeapArray.pop()
        return max_value

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if self.HeapArray and None not in self.HeapArray:
            return False  # если куча вся заполнена

        index = 0

        while index < len(self.HeapArray) and self.HeapArray[index] is not None:
            index += 1

        self.HeapArray[index] = key

        parent_index = (index - 1) // 2
        while index > 0 and self.HeapArray[parent_index] < self.HeapArray[index]:
            self.HeapArray[parent_index] = self.HeapArray[index]
            self.HeapArray[index] = self.HeapArray[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2
        return True
