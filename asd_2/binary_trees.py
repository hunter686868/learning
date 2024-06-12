class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов
        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


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
                    find_node(node.LeftChild, key)
                return True
            else:
                if node.RightChild is not None:
                    find_node(node.RightChild, key)
                return False
        result = find_node(self.Root, key)



    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево
        return False  # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FromNode is None:
            return None

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self):
        return 0  # количество узлов в дереве