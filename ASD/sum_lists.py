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







elif (self.compare(value, self.head.value) == -1 and self.__ascending) or \
     (self.compare(value, self.head.value) == 1 and not self.__ascending):
new_node.next = self.head
self.head.prev = new_node
self.head = new_node
return
elif (self.compare(value, self.tail.value) == 1 and not self.__ascending) or \
     (self.compare(value, self.tail.value) == -1 and self.__ascending):
self.tail.next = new_node
new_node.prev = self.tail
self.tail = new_node
return
curr_node = self.head
while curr_node is not None:
    comparison = self.compare(value, curr_node.value)
    if comparison == 0:
        new_node.prev = curr_node
        new_node.next = curr_node.next
        if curr_node.next is not None:
            curr_node.next.prev = new_node
        curr_node.next = new_node
        return
    elif comparison == 1 and self.__ascending:
        new_node.prev = curr_node
        new_node.next = curr_node.next
        if curr_node.next is not None:
            curr_node.next.prev = new_node
        curr_node.next = new_node
        return
    elif comparison == -1 and not self.__ascending:
        new_node.next = curr_node
        new_node.prev = curr_node.prev
        curr_node.prev.next = new_node
        curr_node.prev = new_node
        return
    curr_node = curr_node.next

