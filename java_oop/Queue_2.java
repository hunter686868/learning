// Доп. задачи
import java.util.*;
// Функция, которая "вращает" очередь по кругу на N элементов.
public class QueueRotate {
    public static <T> void rotate(Queue<T> q, int n) {
        int sz = q.size();
        if (sz == 0) return;

        n = n % sz;
        for (int i = 0; i < n; i++) {
            q.enqueue(q.dequeue());
        }
    }
}

// Очередь с помощью двух стеков.
public class QueueWithStacks<T> {
    private Stack<T> stack1;
    private Stack<T> stack2;

    public QueueWithStacks() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    public void enqueue(T item) {
        stack1.push(item);
    }

    public T dequeue() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }

    public int size() {
        return stack1.size() + stack2.size();
    }
}


// Функция, которая обращает все элементы в очереди в обратном порядке.
public static final class TwoStackQueue<T> {
    private final Stack<T> in = new Stack<T>();
    private final Stack<T> out = new Stack<T>();
    private int size = 0;

    public void enqueue(T item) {
        in.push(item);
        size++;
    }

    public T dequeue() {
        if (size == 0) return null;
        if (out.size() == 0) {
            while (in.size() > 0) {
                out.push(in.pop());
            }
        }
        size--;
        return out.pop();
    }

    public int size() {
        return size;
    }
}

// Круговая очередь статическим массивом фиксированного размера.
public final class CircularQueue<T> {
    private final Object[] data;
    private int head = 0;
    private int tail = 0;

    public CircularQueue(int capacity) {
        if (capacity <= 0) {
            throw new IllegalArgumentException("capacity must be > 0");
        }
        // +1 нужен для различения пусто / полно
        data = new Object[capacity + 1];
    }

    public boolean enqueue(T item) {
        int nextTail = (tail + 1) % data.length;
        if (nextTail == head) {
            return false; // очередь полна
        }
        data[tail] = item;
        tail = nextTail;
        return true;
    }

    public T dequeue() {
        if (head == tail) {
            return null; // очередь пуста
        }
        Object value = data[head];
        data[head] = null;
        head = (head + 1) % data.length;
        return (T) value;
    }

    public boolean isEmpty() {
        return head == tail;
    }
}

