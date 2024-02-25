from linked_list import LinkedList, Node


def sum_lists(list1, list2):
    if list1.len() != list2.len():
        return []
    result_list = LinkedList()
    node1 = list1.head
    node2 = list2.head
    while node1 is not None:
        result_list.add_in_tail(node1.value + node2.value)
        node1 = node1.next
        node2 = node2.next
    return result_list

