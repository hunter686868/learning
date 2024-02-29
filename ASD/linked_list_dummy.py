class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Dummy:
    def __init__(self):
        self.prev = None
        self.next = None
class LinkedList2:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        self.tail.prev = item
        item.next = self.tail


    def find(self, val):
        node = self.head.next
        while node != self.tail:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head.next
        while node != self.tail:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        node = self.head.next
        while node != self.tail:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    return
            node = node.next
        return

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        count = 0
        node = self.head.next
        while node != self.tail:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head.next == self.tail:
                self.head.next = newNode
                self.tail.prev = newNode
                newNode.next = self.tail
                newNode.prev = self.head
            else:
                newNode.prev = self.tail.prev
                self.tail.prev.next = newNode
                self.tail.prev = newNode
                newNode.next = self.tail
        else:
            afterNode.next.prev = newNode
            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode
        return

    def add_in_head(self, newNode):
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        newNode.prev = self.head

