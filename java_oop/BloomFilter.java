public class BloomFilter {
    private final int filter_len;
    private int bitArray;

    public BloomFilter(int f_len) {
        filter_len = f_len;
        bitArray = 0;
    }

    // Сложность O(n)
    public int hash1(String str1) {
        int result = 0;
        for (int i = 0; i < str1.length(); i++) {
            int code = (int) str1.charAt(i);
            result = (result * 17 + code) % filter_len;
        }
        return result;
    }

    // Сложность O(n)
    public int hash2(String str1) {
        int result = 0;
        for (int i = 0; i < str1.length(); i++) {
            int code = (int) str1.charAt(i);
            result = (result * 223 + code) % filter_len;
        }
        return result;
    }

    // Добавление строки в фильтр Блюма.
    // Сложность O(n)
    public void add(String str1) {
        int hash1 = hash1(str1);
        int hash2 = hash2(str1);

        setBit(hash1);
        setBit(hash2);
    }

    // Проверка возможного наличия строки в фильтре.
    // Сложность O(n)
    public boolean isValue(String str1) {
        int hash1 = hash1(str1);
        int hash2 = hash2(str1);

        return getBit(hash1) && getBit(hash2);
    }

    // Установка бита по индексу.
    // Сложность O(1)
    private void setBit(int index) {
        bitArray = bitArray | (1 << index);
    }

    // Получение значения бита по индексу.
    // Сложность O(1)
    private boolean getBit(int index) {
        return (bitArray & (1 << index)) != 0;
    }
}

// Рефлексия по заданию 9
// В реализации использованы два параллельных списка
// вместо предложенного в рекомендациях подхода
// с хранением в упорядоченном списке пар [ключ, индекс].
// Это упрощает код, но приводит к лишним сдвигам в
// values при вставке.