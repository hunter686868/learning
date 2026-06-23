// 9.* Добавьте метод, который "переворачивает" порядок
// элементов в связном списке, меняя его на противоположный.
public void reverse()
{
    // сложность O(n)
    if (head == null || head.next == null) return;

    Node current = head;
    while (current != null)
    {
        Node tmp = current.prev;
        current.prev = current.next;
        current.next = tmp;

        current = current.prev;
    }

    Node tmpHT = head;
    head = tail;
    tail = tmpHT;
}

// 10.* Добавьте булев метод, который сообщает,
// имеются ли циклы (замкнутые на себя по кругу) внутри списка.
public boolean hasCycle()
{
    // сложность O(n)
    Node slow = head;
    Node fast = head;

    while (fast != null && fast.next != null)
    {
        slow = slow.next;
        fast = fast.next.next;
        if (slow == fast) return true;
    }
    return false;
}

// 11.* Добавьте метод, сортирующий список.
public void sort()
{
    // сложность O(n log n)
    if (head == null || head.next == null) return;

    head = mergeSort(head);

    Node t = head;
    while (t.next != null) t = t.next;
    tail = t;
}

private Node mergeSort(Node h)
{
    if (h == null || h.next == null) return h;

    Node second = split(h);

    h = mergeSort(h);
    second = mergeSort(second);

    return merge(h, second);
}

private Node split(Node h)
{
    Node slow = h;
    Node fast = h;

    while (fast.next != null && fast.next.next != null)
    {
        slow = slow.next;
        fast = fast.next.next;
    }

    Node second = slow.next;
    slow.next = null;
    if (second != null) second.prev = null;
    return second;
}

private Node merge(Node a, Node b)
{
    if (a == null) return b;
    if (b == null) return a;

    if (a.value <= b.value)
    {
        a.next = merge(a.next, b);
        if (a.next != null) a.next.prev = a;
        a.prev = null;
        return a;
    }
    else
    {
        b.next = merge(a, b.next);
        if (b.next != null) b.next.prev = b;
        b.prev = null;
        return b;
    }
}


// 12.* Добавьте метод, объединяющий два списка в третий.
public static LinkedList2 mergeSorted(LinkedList2 a, LinkedList2 b)
{
    // сложность O(n+m)
    LinkedList2 res = new LinkedList2();
    Node pa = (a == null) ? null : a.head;
    Node pb = (b == null) ? null : b.head;

    while (pa != null && pb != null)
    {
        if (pa.value <= pb.value)
        {
            res.addInTail(new Node(pa.value));
            pa = pa.next;
        }
        else
        {
            res.addInTail(new Node(pb.value));
            pb = pb.next;
        }
    }

    while (pa != null)
    {
        res.addInTail(new Node(pa.value));
        pa = pa.next;
    }

    while (pb != null)
    {
        res.addInTail(new Node(pb.value));
        pb = pb.next;
    }

    return res;
}


// 13.* Фиктивный узел
public class LinkedList2Dummy
{
    private final Node dummyHead;
    private final Node dummyTail;

    public LinkedList2Dummy()
    {
        dummyHead = new Node(0); // значение не важно, узел "служебный"
        dummyTail = new Node(0);

        dummyHead.prev = null;
        dummyHead.next = dummyTail;

        dummyTail.prev = dummyHead;
        dummyTail.next = null;
    }
}

