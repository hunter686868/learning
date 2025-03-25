class BloomFilter:

    def __init__(self, filter_len: int, k: int):
        # Предусловие: filter_len > 0, k > 0
        # Постусловие: создан пустой битовый массив длиной filter_len, все биты равны 0

        self.filter_len = filter_len
        self.k = k # Количество хэш функций
        self.bit_array = 0

    def _hashes(self, item: str):
        # Предусловие: item - строка
        # Постусловие: возвращает k индексов в пределах [0, m-1]

        hashes = []
        for seed in range(1, self.k + 1):
            hash_value = 0
            for char in item:
                hash_value = (hash_value * seed + ord(char)) % self.filter_len
            hashes.append(hash_value)
        return hashes

    def add(self, item: str):
        # Предусловие: item - строка
        # Постусловие: все k бит, соответствующие item, установлены в 1

        for index in self._hashes(item):
            self.bit_array |= (1 << index)

    def contains(self, item: str) -> bool:
        # Предусловие: item - строка
        return all(self.bit_array & (1 << index) for index in self._hashes(item))

