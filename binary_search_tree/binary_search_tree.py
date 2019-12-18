import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree - need to traverse to find spot
    def insert(self, value):
        node = BinarySearchTree(value)
        if self.value == value:
            return value
        elif self.value == None:
            return node
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = node
        else: #value is greater than self.value
            if self.right:
                self.right.insert(value)
            else:
                self.right = node


    # start from root and traverse - stop at first instance of a value - if we get to a node with no children, can return false.
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target: #originally had this as elif - wasn't passing tests.
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right:
            return self.right.get_max()
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        return cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return #Error
        node.in_order_print(node.left)
        print(node.value)
        node.in_order_print(node.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
