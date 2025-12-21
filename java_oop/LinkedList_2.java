// Доп задачи
// 8.* Напишите функцию, которая получает на вход два связных списка,
// состоящие из целых значений, и если их длины равны, возвращает список,
// каждый элемент которого равен сумме соответствующих элементов входных списков.

public static LinkedList sumLists(LinkedList l1, LinkedList l2)
{
    if (l1 == null || l2 == null) return null;

    int c1 = l1.count();
    int c2 = l2.count();
    if (c1 != c2) return null;

    LinkedList res = new LinkedList();
    Node n1 = l1.head;
    Node n2 = l2.head;

    while (n1 != null) {
        res.addInTail(new Node(n1.value + n2.value));
        n1 = n1.next;
        n2 = n2.next;
    }
    return res;
}
}