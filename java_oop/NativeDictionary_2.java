import java.lang.reflect.Array;

// 5.* Реализуйте словарь с использованием упорядоченного
// списка по ключу для оптимизации производительности поиска.
class SortedDictionary<T>
{
    private java.util.ArrayList<String> keys;
    private java.util.ArrayList<T> values;

    public SortedDictionary()
    {
        keys = new java.util.ArrayList<>();
        values = new java.util.ArrayList<>();
    }

    public void put(String key, T value)
    {
        // Сложность O(n)
        int index = findIndex(key);

        if (index >= 0)
        {
            values.set(index, value);
            return;
        }

        int insertPos = -index - 1;
        keys.add(insertPos, key);
        values.add(insertPos, value);
    }

    public T get(String key)
    {
        // Сложность O(log n)
        int index = findIndex(key);

        if (index >= 0)
        {
            return values.get(index);
        }

        return null;
    }

    public boolean isKey(String key)
    {
        // Сложность O(log n)
        return findIndex(key) >= 0;
    }

    public T remove(String key)
    {
        // Сложность O(n)
        int index = findIndex(key);

        if (index < 0)
        {
            return null;
        }

        keys.remove(index);
        return values.remove(index);
    }

    private int findIndex(String key)
    {
        // Сложность O(log n)
        int left = 0;
        int right = keys.size() - 1;

        while (left <= right)
        {
            int mid = (left + right) / 2;
            int cmp = keys.get(mid).compareTo(key);

            if (cmp == 0)
            {
                return mid;
            }

            if (cmp < 0)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        return -(left + 1);
    }
}

// Создайте словарь, в котором ключи представлены битовыми
// строками фиксированной длины. Реализуйте методы добавления,
// удаления и поиска элементов, используя битовые операции для ускорения работы.
class BitKeyDictionary<T>
{
    private String[] keys;
    private T[] values;
    private boolean[] used;
    private int size;

    public BitKeyDictionary(int sz, Class clazz)
    {
        size = sz;
        keys = new String[size];
        values = (T[]) Array.newInstance(clazz, size);
        used = new boolean[size];
    }

    public void put(String key, T value)
    {
        // Сложность O(n)
        int index = seekSlot(key);

        if (index != -1)
        {
            keys[index] = key;
            values[index] = value;
            used[index] = true;
        }
    }

    public T get(String key)
    {
        // Сложность O(n)
        int index = findSlot(key);

        if (index == -1)
        {
            return null;
        }

        return values[index];
    }

    public boolean isKey(String key)
    {
        // Сложность O(n)
        return findSlot(key) != -1;
    }

    public T remove(String key)
    {
        // Сложность O(n)
        int index = findSlot(key);

        if (index == -1)
        {
            return null;
        }

        T oldValue = values[index];
        keys[index] = null;
        values[index] = null;
        used[index] = false;

        rehashFrom(index);
        return oldValue;
    }

    private int hashFun(String key)
    {
        // Сложность O(n)
        int hash = 0;

        for (int i = 0; i < key.length(); i++)
        {
            hash = (hash << 1) ^ key.charAt(i);
        }

        if (hash < 0)
        {
            hash = -hash;
        }

        return hash % size;
    }

    private int seekSlot(String key)
    {
        // Сложность O(n)
        int index = hashFun(key);

        for (int i = 0; i < size; i++)
        {
            int current = (index + i) % size;

            if (!used[current] || keys[current].equals(key))
            {
                return current;
            }
        }

        return -1;
    }

    private int findSlot(String key)
    {
        // Сложность O(n)
        int index = hashFun(key);

        for (int i = 0; i < size; i++)
        {
            int current = (index + i) % size;

            if (!used[current])
            {
                return -1;
            }

            if (keys[current].equals(key))
            {
                return current;
            }
        }

        return -1;
    }

    private void rehashFrom(int start)
    {
        // Сложность O(n)
        int index = (start + 1) % size;

        while (used[index])
        {
            String keyToMove = keys[index];
            T valueToMove = values[index];

            keys[index] = null;
            values[index] = null;
            used[index] = false;

            int newIndex = seekSlot(keyToMove);
            keys[newIndex] = keyToMove;
            values[newIndex] = valueToMove;
            used[newIndex] = true;

            index = (index + 1) % size;
        }
    }
}