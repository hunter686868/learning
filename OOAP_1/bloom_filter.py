class BloomFilter:

    def __init__(self, m: int, k: int):
        # Предусловие: m > 0, k > 0
        # Постусловие: создан пустой битовый массив длиной m, все биты равны 0

        assert m > 0 and k > 0
        self.m = m
        self.k = k
        self.bit_array = 0

    def _hashes(self, item: str):
        # Предусловие: item - строка
        # Постусловие: возвращает k индексов в пределах [0, m-1]

        hashes = []
        for seed in range(1, self.k + 1):
            hash_value = 0
            for char in item:
                hash_value = (hash_value * seed + ord(char)) % self.m
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

