// 3. Динамические массивы

public class DynArray<T>
{
    public T [] array;
    public int count;
    public int capacity;
    Class clazz;

    public DynArray(Class clz)
    {
        clazz = clz; // нужен для безопасного приведения типов
        // new DynArray<Integer>(Integer.class);

        count = 0;
        makeArray(16);
    }

    // Сложность 0(n), т.к. копируем объекты массива
    public void makeArray(int new_capacity)
    {
        T[] old = array;

        array = (T[]) java.lang.reflect.Array.newInstance(this.clazz, new_capacity);
        int lim = Math.min(count, new_capacity);
        if (old != null && lim > 0)
        {
            System.arraycopy(old, 0, array, 0, lim);
        }

        capacity = new_capacity;
        if (count > new_capacity) count = new_capacity;
    }

    // Сложность 0(1)
    public T getItem(int index)
    {
        if (index < 0 || index >= count) throw new IndexOutOfBoundsException();
        return array[index];
    }

    // Сложность 0(1)
    public void append(T itm)
    {
        if (count == capacity) makeArray(capacity * 2);
        array[count] = itm;
        count++;
    }

    // Сложность 0(n), делаем сдвиг массива
    public void insert(T itm, int index)
    {
        if (index < 0 || index > count) throw new IndexOutOfBoundsException();

        if (count == capacity) makeArray(capacity * 2);

        if (index < count)
        {
            System.arraycopy(array, index, array, index + 1, count - index);
        }

        array[index] = itm;
        count++;
    }

    // Сложность 0(n), делаем сдвиг массива
    public void remove(int index)
    {
        if (index < 0 || index >= count) throw new IndexOutOfBoundsException();

        int numMoved = count - index - 1;
        if (numMoved > 0)
        {
            System.arraycopy(array, index + 1, array, index, numMoved);
        }

        array[count - 1] = null;
        count--;

        if (capacity > 16 && count < (capacity / 2)) {
            int newCap = (int) (capacity / 1.5);
            if (newCap < 16) newCap = 16;
            if (newCap < count) newCap = count;
            makeArray(newCap);
        }
    }

}