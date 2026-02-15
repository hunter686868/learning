import java.util.*;

public class Deque<T> {
    private LinkedList<T> list;

    public Deque()
    {
        list = new LinkedList<>();
    }

    public void addFront(T item)
    // Сложность 0(1)
    {
        list.addFirst(item);
    }

    public void addTail(T item)
    // Сложность 0(1)
    {
        list.addLast(item);
    }

    public T removeFront() {
        // Сложность 0(1)
        if (list.isEmpty()) {
            return null;
        }
        return list.removeFirst();
    }

    public T removeTail() {
        // Сложность 0(1)
        if (list.isEmpty()) {
            return null;
        }
        return list.removeLast();
    }

    public int size()
        // Сложность 0(1)
        return list.size();
    {
        return 0; // размер очереди
    }
}

// 2. Как можно понизить (выровнять) сложность addHead/removeHead
// и addTail/removeTail, с помощью какого ранее изученного типа данных?

Понизить и выровнять сложность данных операций можно с помощью двусвязного списка.

// Рефлексия по предыдущим задачам:

//В предыдущем задании суть была в том, что сложность операций определяется в зависимости от того,
// что именно мы считаем “головой/хвостом” внутри выбранного хранилища.
// Если реализовывать очередь на динамическом массиве и удалять/вставлять не с конца,
// то сложность возможна O(n).
// Для упрощения лучше использовать структуры с O(1) доступом к концам,
// например связный список.