class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.Level = 0 if parent is None else parent.Level + 1  # уровень узла


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None
        if root is not None:
            root.Level = 0  # уровень корневого узла всегда 0

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
        NewChild.Level = ParentNode.Level + 1
        self._update_levels(NewChild)

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None

    def GetAllNodes(self):
        all_nodes = []
        def CollectNodes(node):
            if node:
                all_nodes.append(node)
                for child in node.Children:
                    CollectNodes(child)

        CollectNodes(self.Root)
        return all_nodes

    def FindNodesByValue(self, val):
        all_value_nodes = []

        def CollectNodesValue(node):
            if node:
                if node.NodeValue == val:
                    all_value_nodes.append(node)
                for child in node.Children:
                    CollectNodesValue(child)

        CollectNodesValue(self.Root)
        return all_value_nodes

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode.Parent is not None:
            OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)
        OriginalNode.Level = NewParent.Level + 1
        self._update_levels(OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        def is_leaf(node):
            return len(node.Children) == 0

        return sum(1 for node in self.GetAllNodes() if is_leaf(node))

    def _update_levels(self, node):
        for child in node.Children:
            child.Level = node.Level + 1
            self._update_levels(child)

    def EvenTrees(self):
        return []

