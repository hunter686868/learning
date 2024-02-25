class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        if not self.head:
            return
        node = self.head
        i = node.prev
        while node is not None:
            if node.value == val:
                if i is None:
                    self.head = node.next
                    self.head.prev = None
                else:
                    i.next = node.next
                    i.prev = node.prev
                if node == self.tail:
                    self.tail = i
                    i.prev = node.prev
                    i.next = None
                if not all:
                    return
            else:
                i = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None and self.tail is None:
                newNode.next = None
                newNode.prev = None
                self.head = newNode
                self.tail = self.head
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.tail.next = None
        else:
            if afterNode.next is None:
                afterNode.next = newNode
                newNode.prev = afterNode
                self.tail = newNode
                self.tail.next = None
            else:
                afterNode.next.prev = newNode
                newNode.next = afterNode.next
                afterNode.next = newNode

    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode

