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
        // всегда возвращает корректный индекс слота
        return 0;
    }

    public int seekSlot(String value)
    {
        // находит индекс пустого слота для значения, или -1
        return -1;
    }

    public int put(String value)
    {
        // записываем значение по хэш-функции

        // возвращается индекс слота или -1
        // если из-за коллизий элемент не удаётся разместить
        return -1;
    }

    public int find(String value)
    {
        // находит индекс слота со значением, или -1
        return -1;
    }
}

// Рефлефлексия по решению задания 6:
