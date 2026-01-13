// 6.* Реализуйте динамический массив на основе банковского метода.
public class DynArrayBank<T>
{
    public T[] array;
    public int count;
    public int capacity;
    Class clazz;

    // append без расширения: +3 кредита
    // копирование элемента при расширении: -1 кредит за копию
    private int credits;

    public DynArrayBank(Class clz)
    {
        clazz = clz;
        count = 0;
        credits = 0;
        makeArray(16);
    }

    public void makeArray(int new_capacity)
    {
        T[] old = array;

        array = (T[]) java.lang.reflect.Array.newInstance(this.clazz, new_capacity);

        int lim = Math.min(count, new_capacity);
        if (old != null && lim > 0)
        {
            credits -= lim;
            System.arraycopy(old, 0, array, 0, lim);
        }

        capacity = new_capacity;
        if (count > new_capacity) count = new_capacity;
    }

    public void append(T itm)
    {
        credits += 3;

        if (count == capacity)
        {
            makeArray(capacity * 2);
        }

        array[count] = itm;
        count++;
    }

    public int getCredits()
    {
        return credits;
    }
}



// 7.* Реализуйте многомерный динамический массив: произвольное количество измерений,
// при этом каждое измерение может внутри масштабироваться по потребности.
// В конструкторе задаётся число измерений и размер по каждому из них.
// Обращаться к такому массиву надо как к обычному многомерному, например: myArr[1,2,3].

public class MultiDynArray<T>
{
    private final int dims;
    private final int[] initCaps;
    private final Class clazz;

    private DynArray<Object> root;

    public MultiDynArray(Class clz, int... capacities)
    {
        if (capacities == null || capacities.length == 0) throw new IllegalArgumentException();
        this.dims = capacities.length;
        this.initCaps = capacities.clone();
        this.clazz = clz;

        root = new DynArray<>(Object.class);
        root.makeArray(Math.max(16, initCaps[0])); // минимальная ёмкость как в DynArray
    }

    public T get(int... idx)
    {
        checkIndex(idx);

        Object node = root;
        for (int d = 0; d < dims; d++)
        {
            DynArray<Object> cur = (DynArray<Object>) node;
            int i = idx[d];

            if (i >= cur.count) return null; // неинициализированная область

            Object next = cur.array[i];
            if (next == null) return null;

            if (d == dims - 1) return (T) next;
            node = next;
        }
        return null;
    }

    public void set(T value, int... idx)
    {
        checkIndex(idx);

        DynArray<Object> cur = root;

        for (int d = 0; d < dims; d++)
        {
            int i = idx[d];

            ensureSize(cur, i + 1, (d == 0) ? initCaps[0] : initCaps[d]);

            if (d == dims - 1)
            {
                cur.array[i] = value;
                return;
            }

            Object child = cur.array[i];
            if (child == null)
            {
                DynArray<Object> next = new DynArray<>(Object.class);
                next.makeArray(Math.max(16, initCaps[d + 1]));
                cur.array[i] = next;
                child = next;
            }
            cur = (DynArray<Object>) child;
        }
    }

    private void ensureSize(DynArray<Object> a, int neededCount, int preferredCap)
    {
        // гарантируем, что count >= neededCount
        while (a.count < neededCount)
        {
            a.append(null);
        }
    }

    private void checkIndex(int... idx)
    {
        if (idx == null || idx.length != dims) throw new IllegalArgumentException();
        for (int v : idx) if (v < 0) throw new IndexOutOfBoundsException();
    }
}
