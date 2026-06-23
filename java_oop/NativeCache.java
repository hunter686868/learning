public class NativeCache<T>
{
    public int size;
    public String[] slots;
    public T[] values;
    public int[] hits;

    private Class clazz;

    public NativeCache(int sz, Class clz)
    {
        size = sz;
        clazz = clz;

        slots = new String[size];
        values = (T[]) java.lang.reflect.Array.newInstance(clazz, size);
        hits = new int[size];
    }

    public int hashFun(String key)
    {
        int hash = 0;
        for (int i = 0; i < key.length(); i++) {
            hash = (hash + key.charAt(i)) % size;
        }
        return hash;
    }

    // Поиск слота для вставки.
    // Сложность O(n)
    public int seekSlot(String key)
    {
        int index = hashFun(key);

        for (int i = 0; i < size; i++) {
            int slot = (index + i) % size;
            if (slots[slot] == null) {
                return slot;
            }
        }

        return -1;
    }

    // Поиск индекса ключа.
    // Сложность O(n)
    private int findSlot(String key)
    {
        int index = hashFun(key);

        for (int i = 0; i < size; i++) {
            int slot = (index + i) % size;
            if (slots[slot] != null && slots[slot].equals(key)) {
                return slot;
            }
        }

        return -1;
    }

    // Проверка наличия ключа.
    // Сложность O(n)
    public boolean isKey(String key)
    {
        return findSlot(key) != -1;
    }

    // Получение значения по ключу.
    // Сложность O(n)
    public T get(String key)
    {
        int slot = findSlot(key);
        if (slot == -1) {
            return null;
        }

        hits[slot]++;
        return values[slot];
    }

    // Добавление значения в кэш.
    // Сложность O(n)
    public void put(String key, T value)
    {
        int existingSlot = findSlot(key);
        if (existingSlot != -1) {
            values[existingSlot] = value;
            return;
        }

        int slot = seekSlot(key);
        if (slot != -1) {
            slots[slot] = key;
            values[slot] = value;
            hits[slot] = 0;
            return;
        }

        int evictIndex = findMinHitsIndex();
        slots[evictIndex] = null;
        values[evictIndex] = null;
        hits[evictIndex] = 0;

        int newSlot = seekSlot(key);
        if (newSlot != -1) {
            slots[newSlot] = key;
            values[newSlot] = value;
            hits[newSlot] = 0;
        }
    }

    // Поиск индекса элемента с минимальным числом обращений.
    // Сложность O(n)
    private int findMinHitsIndex()
    {
        int minIndex = 0;

        for (int i = 1; i < size; i++) {
            if (hits[i] < hits[minIndex]) {
                minIndex = i;
            }
        }

        return minIndex;
    }
}

// Рефлексия по курсу:
// Было интересно еще раз пройти курс, но на другом языке
// программирования. Опять же, все быстро забывается,
// вспомнить, как это работает изнути - "базу"
// всегда полезно. И учитывая текущую ситуацию с LLM
// когда код становится более верхнеуровневым, уже на уровне промтов -
// всегда полезно понимать, что вообще происходит
// и как это можно оптимизировать :)