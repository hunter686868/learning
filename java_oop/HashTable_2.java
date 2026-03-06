import java.util.Random;
//Реализуйте динамическую хэш-таблицу, которая автоматически увеличивает свой размер, если места перестаёт хватать.
public class HashTable
{
    public int size;
    public int step;
    public String[] slots;
    public int count;

    public HashTableStar(int sz, int stp)
    {
        size = sz;
        step = stp;
        slots = new String[size];
        count = 0;
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
        // Сложность O(n)
        int index = hashFun(value);

        for (int i = 0; i < size; i++)
        {
            int current = (index + i * step) % size;

            if (slots[current] == null)
                return current;
        }

        return -1;

    }

    public int put(String value)
    {
        // Сложность O(n)
        int slot = seekSlot(value);

        if (slot == -1)
        {
            resize();
            slot = seekSlot(value);
        }

        slots[slot] = value;
        count++;

        return slot;

    }

    private void resize()
    {
        // Сложность O(n)
        String[] old = slots;

        size = size * 2;
        slots = new String[size];
        count = 0;

        for (String s : old)
        {
            if (s != null)
            {
                put(s);
            }
        }

    }
}

// Реализуйте хэш-таблицу, которая использует несколько хэш-функций
// для каждой операции вставки, чтобы уменьшить вероятность коллизий.
public class HashTableMulti
{
    public int size;
    public String[] slots;

    public HashTableMulti(int sz)
    {
        size = sz;
        slots = new String[size];
    }

    public int hash1(String value)
    {
        int hash = 0;

        for (int i = 0; i < value.length(); i++)
            hash += value.charAt(i);

        return hash % size;
    }

    public int hash2(String value)
    {
        int hash = 0;

        for (int i = 0; i < value.length(); i++)
            hash = hash * 31 + value.charAt(i);

        hash = Math.abs(hash);

        return hash % size;
    }

    public int put(String value)
    {
        int h1 = hash1(value);

        if (slots[h1] == null)
        {
            slots[h1] = value;
            return h1;
        }

        int h2 = hash2(value);

        if (slots[h2] == null)
        {
            slots[h2] = value;
            return h2;
        }

        for (int i = 0; i < size; i++)
        {
            int index = (h1 + i) % size;

            if (slots[index] == null)
            {
                slots[index] = value;
                return index;
            }
        }

        return -1;
    }
}

// Организуйте ddos-атаку на вашу исходную хэш-таблицу
public class HashAttack
{
    public static void main(String[] args)
    {
        HashTable table = new HashTable(17, 3);

        for (int i = 0; i < 100; i++)
        {
            String key = "aa" + i;
            int slot = table.put(key);

            System.out.println(key + " -> " + slot);
        }
    }
}

// Модифицируйте хэш-таблицу для защиты от таких атак
public class HashTableSecure
{
    public int size;
    public int step;
    public String[] slots;
    private int salt;

    public HashTableSecure(int sz, int stp)
    {
        size = sz;
        step = stp;
        slots = new String[size];

        Random r = new Random();
        salt = r.nextInt(100000);
    }

    public int hashFun(String value)
    {
        int hash = salt;

        for (int i = 0; i < value.length(); i++)
        {
            hash += value.charAt(i);
        }

        return Math.abs(hash) % size;
    }
}