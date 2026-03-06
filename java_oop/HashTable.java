// 8. Хэширование

public class HashTable
{
    public int size;
    public int step;
    public String [] slots;

    public HashTable(int sz, int stp)
    {
        size = sz;
        step = stp;
        slots = new String[size];
        for(int i=0; i<size; i++) slots[i] = null;
    }

    public int hashFun(String value)
    {
        // Сложность O(n)
        int hash = 0;

        for (int i = 0; i < value.length(); i++)
        {
            hash += value.charAt(i);
        }

        return hash % size;
    }

    public int seekSlot(String value)
    {
        // находит индекс пустого слота для значения, или -1
        // Сложность 0(n)
        int index = hashFun(value);

        for (int i = 0; i < size; i++)
        {
            int current = (index + i * step) % size;

            if (slots[current] == null)
            {
                return current;
            }
        }
        return -1;
    }

    public int put(String value)
    {
        // записываем значение по хэш-функции
        // возвращается индекс слота или -1
        // если из-за коллизий элемент не удаётся разместить
        // Сложность 0(n)
        int slot = seekSlot(value);

        if (slot == -1)
        {
            return -1;
        }

        slots[slot] = value;

        return slot;
    }

    public int find(String value)
    {
        // находит индекс слота со значением, или -1
        // Сложность 0(n)
        int index = hashFun(value);

        for (int i = 0; i < size; i++)
        {
            int current = (index + i * step) % size;

            if (slots[current] == null)
            {
                return -1;
            }

            if (slots[current].equals(value))
            {
                return current;
            }
        }

        return -1;
    }
}

// Рефлефлексия по решению задания 6:
// При проверке палиндрома использована дека:
// добавил и сравнивал элементы, удаляя их с начала и конца,
// рекомендации сответствует.
// Для получения минимума за O(1) были использованы два стека с поддержкой минимума,
// а дека реализована через цикл с указателями head и tail,
// операции добавления и удаления (и с начала и с конца) выполняются O(1).