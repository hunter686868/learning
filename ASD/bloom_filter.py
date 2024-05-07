HASH_CONST_1 = 17
HASH_CONST_2 = 223
class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

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

    def add(self, str1):
        val1 = self.hash1(str1)
        val2 = self.hash2(str1)
        self.filter |= (1 << val1) | (1 << val2)

    def is_value(self, str1):
        val1 = self.hash1(str1)
        val2 = self.hash2(str1)
        return (self.filter & (1 << val1)) and (self.filter & (1 << val2)) != 0

