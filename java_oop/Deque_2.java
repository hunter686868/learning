// 4.* Напишите функцию, которая с помощью Deque проверяет,
// является ли некоторая строка палиндромом (читается одинаково слева направо и справа налево).
import Deque;

public class PalindromeCheck {
    public boolean isPalindrome(String s) {
        Deque<Character> deque = new Deque<>();
        for (char c : s.toCharArray()) {
            deque.addTail(c);
        }
        while (deque.size() > 1) {
            if (deque.removeFront() != deque.removeTail()) {
                return false;
            }
        }
        return true;
    }
}
// 5.* Напишите метод, который возвращает минимальный элемент деки за O(1).
public class MinDeque<T extends Comparable<T>> {
    private MinStack<T> left = new MinStack<>();
    private MinStack<T> right = new MinStack<>();

    public void addFront(T item) {
        left.push(item);
    }

    public void addTail(T item) {
        right.push(item);
    }

    public T removeFront() {
        if (left.size() == 0) move(right, left);
        return left.pop();
    }

    public T removeTail() {
        if (right.size() == 0) move(left, right);
        return right.pop();
    }

    public int size() {
        return left.size() + right.size();
    }

    public T min() {
        T a = left.min();
        T b = right.min();
        if (a == null) return b;
        if (b == null) return a;
        return (a.compareTo(b) <= 0) ? a : b;
    }

    private void move(MinStack<T> from, MinStack<T> to) {
        while (from.size() > 0) to.push(from.pop());
    }

    private static class MinStack<E extends Comparable<E>> {
        private Deque<E> values = new Deque<>();
        private Deque<E> mins = new Deque<>();
        private int size = 0;

        void push(E x) {
            values.addFront(x);
            if (mins.size() == 0) {
                mins.addFront(x);
            } else {
                E cur = mins.removeFront();
                mins.addFront(cur);
                if (x.compareTo(cur) <= 0) mins.addFront(x);
            }
            size++;
        }

        E pop() {
            if (size == 0) return null;
            E v = values.removeFront();

            E curMin = mins.removeFront();
            mins.addFront(curMin);
            if (v != null && curMin != null && v.compareTo(curMin) == 0) {
                mins.removeFront();
            }

            size--;
            return v;
        }

        E min() {
            if (mins.size() == 0) return null;
            E cur = mins.removeFront();
            mins.addFront(cur);
            return cur;
        }

        int size() {
            return size;
        }
    }
}
// 6.* Реализуйте двустороннюю очередь с помощью динамического массива.
// Методы добавления и удаления элементов с обоих концов деки должны работать за амортизированное время o(1).

public class ArrayDeque<T> {
    private Object[] a = new Object[8];
    private int head = 0;
    private int tail = 0;
    private int size = 0;

    public int size() {
        return size;
    }

    public void addFront(T item) {
        if (size == a.length) resize(a.length * 2);
        head = dec(head, a.length);
        a[head] = item;
        size++;
    }

    public void addTail(T item) {
        if (size == a.length) resize(a.length * 2);
        a[tail] = item;
        tail = inc(tail, a.length);
        size++;
    }

    public T removeFront() {
        if (size == 0) return null;
        T v = (T) a[head];
        a[head] = null;
        head = inc(head, a.length);
        size--;
        if (a.length > 8 && size * 4 <= a.length) resize(a.length / 2);
        return v;
    }

    public T removeTail() {
        if (size == 0) return null;
        tail = dec(tail, a.length);
        T v = (T) a[tail];
        a[tail] = null;
        size--;
        if (a.length > 8 && size * 4 <= a.length) resize(a.length / 2);
        return v;
    }

    private void resize(int newCap) {
        Object[] b = new Object[newCap];
        for (int i = 0; i < size; i++) b[i] = a[(head + i) % a.length];
        a = b;
        head = 0;
        tail = size;
    }

    private int inc(int i, int m) {
        i++;
        return (i == m) ? 0 : i;
    }

    private int dec(int i, int m) {
        i--;
        return (i < 0) ? (m - 1) : i;
    }
}