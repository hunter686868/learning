from deque import Deque


def palyndrome(palindrom):
    deque = Deque()
    for i in palindrom:
        deque.addTail(i)
    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False
    return True
