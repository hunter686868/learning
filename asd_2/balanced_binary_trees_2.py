class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a):

    # создаём дерево с нуля из неотсортированного массива a
        a.sort()
        def create_tree(arr, start, end, level, parent):
            middle_index = (end + start) // 2
            value = arr[middle_index]
            node = BSTNode(value, parent)
            node.LeftChild = create_tree(arr, start, middle_index - 1, level + 1, node)
            node.RightChildChild = create_tree(arr, middle_index + 1, end, level + 1, node)
            return node
        return create_tree(a, 0, len(a) - 1, 0, None)

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node