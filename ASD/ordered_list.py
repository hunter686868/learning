class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        else:
            return 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        curr_node = self.head
        prev = None
        while curr_node is not None and ((self.__ascending and self.compare(value, curr_node.value) == 1) or
                                         (not self.__ascending and self.compare(value, curr_node.value) == -1)):
            prev = curr_node
            curr_node = curr_node.next
        if prev is None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif curr_node is None:
            prev.next = new_node
            new_node.prev = prev
            self.tail = new_node
        else:
            prev.next = new_node
            new_node.prev = curr_node.prev
            new_node.next = curr_node
            curr_node.prev = new_node

    def find(self, val):
        curr_node = self.head
        while curr_node is not None:
            comparison = self.compare(val, curr_node.value)
            if comparison == 0:
                return curr_node
            elif (self.__ascending and comparison == -1) or (not self.__ascending and comparison == 1):
                return None
            curr_node = curr_node.next
        return None

    def delete(self, val):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value == val:
                if curr_node.prev is not None:
                    curr_node.prev.next = curr_node.next
                else:
                    self.head = curr_node.next
                if curr_node.next is not None:
                    curr_node.next.prev = curr_node.prev
                else:
                    self.tail = curr_node.prev
                return
            curr_node = curr_node.next
        return

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        curr_node = self.head
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1_s = v1.strip()
        v2_s = v2.strip()
        if v1_s < v2_s:
            return -1
        elif v1_s == v2_s:
            return 0
        else:
            return 1

