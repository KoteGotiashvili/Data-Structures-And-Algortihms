class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # if data is already exists
        if data == self.data:
            return

        # check left half
        if self.data < data:
            if self.right:
                self.right.add_child(data)  # call recursively
            else:
                # If I'm in leaf node
                self.right = BinarySearchTree(data)

        # check right half
        if self.data > data:
            if self.left:
                self.left.add_child(data)  # call recursively
            else:
                # If I'm in leaf node
                self.left = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def insert_value(self, head, data):
        if head is None:
            return BinarySearchTree(data)
        if head.data < data:
            print(f"Moving to the left subtree of {head.data}")  # Track movement to the left subtree
            head.right = self.insert_value(head.right, data)
        else:
            print(f"Moving to the right subtree of {head.data}")  # Track movement to the right subtree
            head.left = self.insert_value(head.left, data)
        return head

    def print_leaf_nodes(self, tree):
        if tree is None:
            return
        if tree.left is None and tree.right is None:
            print(f'Leaf Nodes are {tree.data}')
            return
        if tree.left is not None:
            #explore first left half before go to right
            self.print_leaf_nodes(tree.left)
        if tree.right is not None:
            self.print_leaf_nodes(tree.right)
    def find_min(self, tree):
        if tree.left is None:
            return tree.data
        return self.find_min(tree.left)
    def find_max(self, tree):
        if tree.right is None:
            return tree.data
        return self.find_max(tree.right)

    def sum_of_tree(self, tree):
        if tree is None:
            return 0
        return tree.data + self.sum_of_tree(tree.left) + self.sum_of_tree(tree.right)

    def pre_order_traversal(self):
        #first visit left then right
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements


    def post_order_traversal(self):
        #start from leaf nodes, first left then right last head node
        elements = []

        if self.left is not None:
            elements += self.left.post_order_traversal()
        if self.right is not None:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # Don't have left and right child means we are on parent node so return none
            if self.left is None and self.right is None:
                return None
            # only has a right child, so change it
            elif self.left is None:
                return self.right
            # only has a left child, so change it
            elif self.right is None:
                return self.left
            # both left and right child exist
            min_val = self.right.find_min(self.right)
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self







# def build_tree(elements):
#     node = BinarySearchTree(elements[0])
#     for i in range(1, len(elements)):
#         node.add_child(elements[i])
#
#     return node
#
#
# array = [17, 4, 1, 20, 9, 23, 18, 34]
# tree = build_tree(array)
# tree.delete(20)
# print(tree.in_order_traversal())


