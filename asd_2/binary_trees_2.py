class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        self.tree_size = (2 ** (depth + 1)) - 1
        self.Tree = [None] * self.tree_size  # массив ключей

    def FindIndex(self, key):
        index = 0
        while index < self.tree_size:
            if self.Tree[index] is None:
                return -index
            if self.Tree[index] == key:
                return index
            if key < self.Tree[index]:
                index = (2 * index) + 1
            else:
                index = (2 * index) + 2
        return None

    def FindKeyIndex(self, key):
        index = self.FindIndex(key)
        if index == 0 and self.Tree[index] is None:
            return None
        return index

    def AddKey(self, key):
        index = self.FindIndex(key)
        if index is None:
            return -1
        if index > 0:
            return index
        else:
            self.Tree[-index] = key
            return -index
        # индекс добавленного/существующего ключа или -1 если не удалось