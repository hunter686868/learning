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
            if start > end:
                return None
            middle_index = (end + start) // 2
            value = arr[middle_index]
            node = BSTNode(value, parent)
            node.Level = level
            if level == 0:
                self.Root = node
            node.LeftChild = create_tree(arr, start, middle_index - 1, level + 1, node)
            node.RightChild = create_tree(arr, middle_index + 1, end, level + 1, node)
            return node
        return create_tree(a, 0, len(a) - 1, 0, None)

    def IsBalanced(self, root_node):

        def get_deep(node):
            if node is None:
                return 0
            deep_left = get_deep(node.LeftChild)
            deep_right = get_deep(node.RightChild)
            return max(deep_left, deep_right) + 1

        def check_balance(node):
            if node is None:
                return True
            deep_left = get_deep(node.LeftChild)
            deep_right = get_deep(node.RightChild)
            if abs(deep_right - deep_left) > 1:
                return False
            return check_balance(node.LeftChild) and check_balance(node.RightChild)
        return check_balance(root_node)

