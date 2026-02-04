import java.util.*;

public class Queue<T> {
    private final LinkedList<T> list;

    public Queue() {
        list = new LinkedList<>();
    }

    // Сложность O(1)
    public void enqueue(T item) {
        list.addLast(item);
    }

    // Сложность O(1)
    public T dequeue() {
        if (list.isEmpty()) {
            return null;
        }
        return list.removeFirst();
    }

    public int size() {
        return list.size();
    }

    public boolean isEmpty() {
        return list.isEmpty();
    }
}
