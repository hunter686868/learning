// 7. Упорядоченный список
import java.util.*;

class Node<T>
{
    public T value;
    public Node<T> next, prev;

    public Node(T _value)
    {
        value = _value;
        next = null;
        prev = null;
    }
}

public class OrderedList<T>
{
    public Node<T> head, tail;
    private boolean _ascending;

    public OrderedList(boolean asc)
    {
        head = null;
        tail = null;
        _ascending = asc;
    }

    // Метод сравнения двух значений
    public int compare(T v1, T v2)
    {
        // Сложность O(1)

        if (v1 == null && v2 == null) return 0;
        if (v1 == null) return -1;
        if (v2 == null) return 1;

        if (v1 instanceof Number && v2 instanceof Number)
        {
            double a = ((Number)v1).doubleValue();
            double b = ((Number)v2).doubleValue();
            if (a < b) return -1;
            if (a > b) return 1;
            return 0;
        }

        if (v1 instanceof String && v2 instanceof String)
        {
            String a = ((String)v1).trim();
            String b = ((String)v2).trim();
            int c = a.compareTo(b);
            if (c < 0) return -1;
            if (c > 0) return 1;
            return 0;
        }

        if (v1 instanceof Comparable && v2 instanceof Comparable)
        {
            int c = ((Comparable)v1).compareTo(v2);
            if (c < 0) return -1;
            if (c > 0) return 1;
            return 0;
        }

        return 0;
    }

    // Добавление нового элемента по значению
    public void add(T value)
    {
        // Сложность O(n)
        Node<T> n = new Node<T>(value);

        if (head == null)
        {
            head = n;
            tail = n;
            return;
        }

        Node<T> cur = head;

        while (cur != null)
        {
            int cmp = compare(value, cur.value);
            boolean insertBefore = _ascending ? (cmp <= 0) : (cmp >= 0);

            if (insertBefore)
            {
                n.next = cur;
                n.prev = cur.prev;

                if (cur.prev != null)
                    cur.prev.next = n;
                else
                    head = n;

                cur.prev = n;
                return;
            }

            cur = cur.next;
        }

        n.prev = tail;
        tail.next = n;
        tail = n;
    }

    public Node<T> find(T val)
    {
        // Сложность O(n)
        Node<T> cur = head;

        while (cur != null)
        {
            int cmp = compare(cur.value, val);

            if (cmp == 0)
                return cur;

            if (_ascending)
            {
                if (cmp > 0) return null;
            }
            else
            {
                if (cmp < 0) return null;
            }

            cur = cur.next;
        }

        return null;
    }

    // Удаление самого первого (одного) элемента по значению: Delete()
    public void delete(T val)
    {
        // Сложность O(n)
        Node<T> node = find(val);
        if (node == null) return;

        if (node.prev != null)
            node.prev.next = node.next;
        else
            head = node.next;

        if (node.next != null)
            node.next.prev = node.prev;
        else
            tail = node.prev;
    }

    public void clear(boolean asc)
    {
        // Сложность O(1)
        _ascending = asc;
        head = null;
        tail = null;
    }

    public int count()
    {
        // Сложность O(n)
        int c = 0;
        Node<T> cur = head;

        while (cur != null)
        {
            c++;
            cur = cur.next;
        }

        return c;
    }

    ArrayList<Node<T>> getAll()
    {
        // Сложность O(n)
        ArrayList<Node<T>> r = new ArrayList<Node<T>>();
        Node<T> node = head;
        while (node != null)
        {
            r.add(node);
            node = node.next;
        }
        return r;
    }
}

// Рефлексия
// В рекомендациях указаны оптимальные алгоримы, как и должно все работать.
// Полезно знать как оно работает на уровень ниже, при вызове метода особо об этом не задумываешься.