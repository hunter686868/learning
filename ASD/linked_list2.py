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
        while node is not None:
            if node.value == val:
                if node == self.head:
                    self.head = node.next
                    node.next.prev = None
                if node == self.tail:
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next
        return

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
                self.head = newNode
                self.tail = newNode
                newNode.next = None
                newNode.prev = None
            else:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.tail.next = None
        else:
            if afterNode == self.tail:
                afterNode.next = newNode
                newNode.prev = afterNode
                self.tail = newNode
                self.tail.next = None
            else:
                afterNode.next.prev = newNode
                newNode.next = afterNode.next
                afterNode.next = newNode
                newNode.prev = afterNode
        return

    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode

