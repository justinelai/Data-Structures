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
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = node
        elif value > self.value: #value is greater than self.value
            if self.right: 
                self.right.insert(value) #travel one level down when there's an existing right child
            else:
                self.right = node #if no right value, use node
        #elif self.value == value: #kinda weird, not sure if I need this
        #    return value
        else:
        #elif self.value == None:
            return node


    # start from root and traverse - stop at first instance of a value - if we get to a node with no children, can return false.
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target: #originally had this as elif - wasn't passing tests.
            if self.left is None: #replaced equals with "is" for style reasons
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None: #replaced equals with "is" for style reasons
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
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)

    # First attempt
    """def in_order_print(self, node):
        if node is None:
            return #Error
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)"""


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal - QUEUE
    #
    # add value, enqueue left child, enqueue right child, dequeue parent when done

    def bft_print(self, node):
        bft_queue = Queue()
        bft_queue.enqueue(node)
        while bft_queue:
            node = bft_queue.dequeue()
            if node is None:
                return
            print(node.value)
            if node.left:
                bft_queue.enqueue(node.left)
            if node.right:
                bft_queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal - STACK
    def dft_print(self, node):
        bft_stack = Stack()
        bft_stack.push(node)
        while bft_stack:
            node = bft_stack.pop()
            if node is None:
                return
            print(node.value)
            if node.left:
                bft_stack.push(node.left)
            if node.right:
                bft_stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if node is not None:
            print(node.value)
            node.pre_order_dft(node.left)
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)
