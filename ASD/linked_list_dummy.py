class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        item.prev = self.tail.prev
        item.next = self.tail

    def find(self, val):
        node = self.head.next
        while node.next is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head.next
        while node.next is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        node = self.head.next
        i = self.head
        while node.next is not None:
            if node.value == val:
                i.next = node.next
                i.prev = node.prev
                if not all:
                    return
            else:
                i = node
            node = node.next

    def clean(self):
        self.head.next = None
        self.tail.prev = None

    def len(self):
        count = 0
        node = self.head.next
        while node.next is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head.next is None and self.tail.prev is None:
                newNode.next = self.tail
                newNode.prev = self.head
                self.head.next = newNode
                self.tail.prev = self.head.next
            else:
                self.tail.prev.next = newNode
                self.tail.prev = newNode.prev
                newNode.next = self.tail
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

