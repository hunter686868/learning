class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        if self.Root is None:
            return BSTFind()

        def find_node(node, key):
            if node is None:
                return None
            if node.NodeKey == key:
                return node
            if key < node.NodeKey:
                if node.LeftChild is not None:
                    return find_node(node.LeftChild, key)
                return [node, True]
            else:
                if node.RightChild is not None:
                    return find_node(node.RightChild, key)
                return [node, False]

        result = find_node(self.Root, key)
        find_result = BSTFind()
        if isinstance(result, list):
            find_result.Node = result[0]
            find_result.ToLeft = result[1]
        else:
            find_result.Node = result
            find_result.NodeHasKey = True

        return find_result

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey:
            return False

        new_node = BSTNode(key, val, find_result.Node)
        if find_result.Node is None:
            self.Root = new_node
        elif find_result.ToLeft:
            find_result.Node.LeftChild = new_node
        else:
            find_result.Node.RightChild = new_node
        return True

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FromNode is None:
            return None
        current_node = FromNode
        if FindMax:
            while current_node.RightChild is not None:
                current_node = current_node.RightChild
        else:
            while current_node.LeftChild is not None:
                current_node = current_node.LeftChild

        return current_node

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        find_result = self.FindNodeByKey(key)
        if not find_result.NodeHasKey:
            return False

        node_to_delete = find_result.Node
        parent = node_to_delete.Parent

        if node_to_delete.LeftChild is None and node_to_delete.RightChild is None:
            if parent is None:
                self.Root = None
            elif node_to_delete == parent.LeftChild:
                parent.LeftChild = None
            else:
                parent.RightChild = None

        elif node_to_delete.LeftChild is not None and node_to_delete.RightChild is None:
            if parent is None:
                self.Root = node_to_delete.LeftChild
            else:
                if node_to_delete == parent.LeftChild:
                    parent.LeftChild = node_to_delete.LeftChild
                else:
                    parent.RightChild = node_to_delete.LeftChild
            node_to_delete.LeftChild.Parent = parent

        elif node_to_delete.RightChild is not None and node_to_delete.LeftChild is None:
            if parent is None:
                self.Root = node_to_delete.RightChild
            else:
                if node_to_delete == parent.LeftChild:
                    parent.LeftChild = node_to_delete.RightChild
                else:
                    parent.RightChild = node_to_delete.RightChild
            node_to_delete.RightChild.Parent = parent

        else:
            successor = self.FinMinMax(node_to_delete.RightChild, False)
            if successor.Parent != node_to_delete:
                if successor.RightChild is not None:
                    successor.RightChild.Parent = successor.Parent
                successor.Parent.LeftChild = successor.RightChild
                successor.RightChild = node_to_delete.RightChild
                successor.RightChild.Parent = successor

            if parent is None:
                self.Root = successor
            elif node_to_delete == parent.LeftChild:
                parent.LeftChild = successor
            else:
                parent.RightChild = successor

            successor.Parent = parent
            successor.LeftChild = node_to_delete.LeftChild
            successor.LeftChild.Parent = successor

        return True

    def Count(self):
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.LeftChild) + count_nodes(node.RightChild)
        return count_nodes(self.Root)

    def WideAllNodes(self):
        if self.Root is None:
            return ()

        nodes_list = []
        queue = [self.Root]

        while queue:
            current_node = queue.pop(0)
            nodes_list.append(current_node)
            if current_node.LeftChild:
                queue.append(current_node.LeftChild)
            if current_node.RightChild:
                queue.append(current_node.RightChild)

        result = tuple(nodes_list)
        return result

    def DeepAllNodes(self, order):
        if self.Root is None:
            return ()
        nodes_list = []

        def in_order(node):
            if node:
                in_order(node.LeftChild)
                nodes_list.append(node)
                in_order(node.RightChild)

        def post_order(node):
            if node:
                post_order(node.LeftChild)
                post_order(node.RightChild)
                nodes_list.append(node)

        def pre_order(node):
            if node:
                nodes_list.append(node)
                pre_order(node.LeftChild)
                pre_order(node.RightChild)

        if order == 0:
            in_order(self.Root)
        if order == 1:
            post_order(self.Root)
        if order == 2:
            pre_order(self.Root)

        result = tuple(nodes_list)
        return result
