import java.util.*;

public class LinkedList
{
    public Node head;
    public Node tail;

    public LinkedList()
    {
        head = null;
        tail = null;
    }

    public void addInTail(Node item) {
        if (this.head == null)
            this.head = item;
        else
            this.tail.next = item;
        this.tail = item;
    }

    public Node find(int value) {
        Node node = this.head;
        while (node != null) {
            if (node.value == value)
                return node;
            node = node.next;
        }
        return null;
    }

    // (4) Поиск всех узлов по значению. Сложность 0(n)
    public ArrayList<Node> findAll(int _value) {
        ArrayList<Node> nodes = new ArrayList<>();
        Node node = this.head;
        while (node != null) {
            if (node.value == _value) nodes.add(node);
            node = node.next;
        }
        return nodes;
    }

    // (1) Удаление одного (первого) узла по значению. Сложность 0(n)
    public boolean remove(int _value)
    {
        if (head == null) return false;

        if (head.value == _value) {
            head = head.next;
            if (head == null) tail = null;
            return true;
        }
        Node prev = head;
        Node cur = head.next;

        while (cur != null) {
            if (cur.value == _value) {
                prev.next = cur.next;
                if (cur == tail) tail = prev;
                return true;
            }
            prev = cur;
            cur = cur.next;
        }
        return false;
    }

    // (2) Удаление всех узлов по значению. Сложность 0(n)
    public void removeAll(int _value)
    {
        while (head != null && head.value == _value) {
            head = head.next;
        }

        if (head == null) {
            tail = null;
            return;
        }

        Node prev = head;
        Node cur = head.next;

        while (cur != null) {
            if (cur.value == _value) {
                prev.next = cur.next;
                if (cur == tail) tail = prev;
                cur = prev.next;
            } else {
                prev = cur;
                cur = cur.next;
            }
        }
    }

    // (3) Очистка списка. Сложность 0(1)
    public void clear()
    {
        head = null;
        tail = null;
    }

    // (5) Длина списка. Сложность 0(n)
    public int count()
    {
        return 0; // здесь будет ваш код подсчёта количества элементов в списке
    }
    {
        int c = 0;
        Node node = head;
        while (node != null) {
            c++;
            node = node.next;
        }
        return c;
    }

    // (6) Вставка после заданного узла. Сложность 0(1)
    public void insertAfter(Node _nodeAfter, Node _nodeToInsert)
    {
        if (_nodeToInsert == null) return;

        if (_nodeAfter == null) {
            if (head == null) {
                head = _nodeToInsert;
                tail = _nodeToInsert;
                _nodeToInsert.next = null;
            } else {
                _nodeToInsert.next = head;
                head = _nodeToInsert;
            }
            return;
        }

        _nodeToInsert.next = _nodeAfter.next;
        _nodeAfter.next = _nodeToInsert;

        if (tail == _nodeAfter) {
            tail = _nodeToInsert;
        }
    }
}

class Node
{
    public int value;
    public Node next;
    public Node(int _value)
    {
        value = _value;
        next = null;
    }
}