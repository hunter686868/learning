// 2. Двунаправленный связанный список

import java.util.*;

public class LinkedList2
{
    public Node head;
    public Node tail;

    public LinkedList2()
    {
        head = null;
        tail = null;
    }

    public void addInTail(Node _item)
    {
        if (head == null) {
            this.head = _item;
            this.head.next = null;
            this.head.prev = null;
        } else {
            this.tail.next = _item;
            _item.prev = tail;
        }
        this.tail = _item;
    }

    public Node find(int _value)
    {
        // Поиск первого узла по значению, сложность O(n)
        Node current = head;
        while (current != null)
        {
            if (current.value == _value) return current;
            current = current.next;
        }
        return null;
    }

    public ArrayList<Node> findAll(int _value)
    {
        // Поиск всех узлов по значению, сложность O(n)
        ArrayList<Node> nodes = new ArrayList<Node>();
        Node current = head;
        while (current != null)
        {
            if (current.value == _value) nodes.add(current);
            current = current.next;
        }
        return nodes;
    }

    public boolean remove(int _value)
    {
        // Удаление одного (первого найденного) узла по значению, сложность O(n)
        Node current = head;

        while (current != null)
        {
            if (current.value == _value)
            {
                if (current == head && current == tail)
                {
                    head = null;
                    tail = null;
                }
                else if (current == head)
                {
                    head = current.next;
                    head.prev = null;
                }
                else if (current == tail)
                {
                    tail = current.prev;
                    tail.next = null;
                }
                else
                {
                    current.prev.next = current.next;
                    current.next.prev = current.prev;
                }

                current.prev = null;
                current.next = null;

                return true;
            }
            current = current.next;
        }

        return false;
    }

    public void removeAll(int _value)
    {
        // Удаление всех узлов по значению, сложность O(n)
        Node current = head;

        while (current != null)
        {
            Node next = current.next;

            if (current.value == _value)
            {
                if (current == head && current == tail)
                {
                    head = null;
                    tail = null;
                }
                else if (current == head)
                {
                    head = current.next;
                    head.prev = null;
                }
                else if (current == tail)
                {
                    tail = current.prev;
                    tail.next = null;
                }
                else
                {
                    current.prev.next = current.next;
                    current.next.prev = current.prev;
                }

                current.prev = null;
                current.next = null;
            }

            current = next;
        }
    }

    public void clear()
    {
        // Очистка списка, сложность O(1)
        head = null;
        tail = null;
    }

    public int count()
    {
        // Подсчет элементов, сложность O(n)
        int cnt = 0;
        Node current = head;
        while (current != null)
        {
            cnt++;
            current = current.next;
        }
        return cnt;
    }

    public void insertAfter(Node _nodeAfter, Node _nodeToInsert)
    {
        // Вставка узла после заданного, сложность O(1) (если _nodeAfter уже известен/дан ссылкой)

        if (_nodeToInsert == null) return;

        // если _nodeAfter = null - добавляем новый элемент первым в списке
        if (_nodeAfter == null)
        {
            if (head == null)
            {
                head = _nodeToInsert;
                tail = _nodeToInsert;
                _nodeToInsert.prev = null;
                _nodeToInsert.next = null;
                return;
            }

            _nodeToInsert.prev = null;
            _nodeToInsert.next = head;
            head.prev = _nodeToInsert;
            head = _nodeToInsert;
            return;
        }

        if (head == null) return;

        if (_nodeAfter == tail)
        {
            _nodeToInsert.prev = tail;
            _nodeToInsert.next = null;
            tail.next = _nodeToInsert;
            tail = _nodeToInsert;
            return;
        }

        Node afterNext = _nodeAfter.next;
        if (afterNext == null)
        {
            _nodeToInsert.prev = _nodeAfter;
            _nodeToInsert.next = null;
            _nodeAfter.next = _nodeToInsert;
            tail = _nodeToInsert;
            return;
        }

        _nodeToInsert.prev = _nodeAfter;
        _nodeToInsert.next = afterNext;
        afterNext.prev = _nodeToInsert;
        _nodeAfter.next = _nodeToInsert;
    }
}

class Node
{
    public int value;
    public Node next;
    public Node prev;

    public Node(int _value)
    {
        value = _value;
        next = null;
        prev = null;
    }
}
