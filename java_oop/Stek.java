// Стек
// 1, 2
import java.util.*;

public class Stack<T>
{
    // Для реализации стека, чтобы работа была не с
    // хвостом списка как с верхушкой стека,
    // а с его головой выбрал LinkedList
    private LinkedList<T> data;

    public Stack()
    {
        data = new LinkedList<>();
    }

    public int size()
    // Сложность О(1)
    {
        return data.size();
    }

    public T pop()
    // Сложность О(1)
    {
        if (data.isEmpty()) return null;
        return data.removeFirst();
    }

    public void push(T val)
    // Сложность О(1)
    {
        data.addFirst(val);
    }

    public T peek()
    // Сложность О(1)
    {
        if (data.isEmpty()) return null;
        return data.peekFirst();
    }
}

// 3
// Опустошит список и вернет null