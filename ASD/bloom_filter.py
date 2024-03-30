class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        val = 0
        for c in str1:
            code = ord(c)
            val = (val * 17 + code) % self.filter_len
        return val

    def hash2(self, str1):
        val = 0
        for c in str1:
            code = ord(c)
            val = (val * 223 + code) % self.filter_len
        return val

    def add(self, str1):
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре