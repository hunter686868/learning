// Ассоциативный массив

import java.lang.reflect.Array;

class NativeDictionary<T>
{
    public int size;
    public String [] slots;
    public T [] values;

    public NativeDictionary(int sz, Class clazz)
    {
        size = sz;
        slots = new String[size];
        values = (T[]) Array.newInstance(clazz, this.size);
    }

    public int hashFun(String key)
    {
        // всегда возвращает корректный индекс слота
        return 0;
    }

    public boolean isKey(String key)
    {
        // возвращает true если ключ имеется,
        // иначе false
        return false;
    }

    public void put(String key, T value)
    {
        // гарантированно записываем
        // значение value по ключу key
    }

    public T get(String key)
    {
        // возвращает value для key,
        // или null если ключ не найден
        return null;
    }
}