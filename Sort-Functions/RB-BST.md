```python
# Name: Ayan Tuladhar
import sys

# The following function contains constructors to hold the key, pointers and colors for RB tree.


class Node:
    def __init__(self, data):
        self.data = data
        self.first = None
        self.left = None
        self.right = None
        self.red_or_black = 1

# The following function was compiled from the source below.
# https://github.com/vprusso/youtube_tutorials/blob/master/data_structures/trees/binary_trees/binary_tree_size.py
# The following class Stack contains objects for counting nodes, force pushing nodes, popping nodes, looking nodes-
# and checking nodes where each nodes contains keys.
# Uses self function.


class Stack(object):
    def __int__(self):
        self.items=[]

    def __len__(self):
        return self.countNodes()

    def countNodes(self):
        return len(self.items)

    def force(self, item):
        self.items.append(item)

    def drag(self):
        if not self.is_empty():
            return self.items.pop()

    def look(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        q = ""
        for i in range(len(self.items)):
            q += str(self.items[i].value) + "-"
        return q

# The following class contains RB tree implementations.

class RedBlackTree():
    def __init__(self):
        self.TREE = Node(0)
        self.TREE.red_or_black = 0
        self.TREE.left = None
        self.TREE.right = None
        self.root = self.TREE

    def __pre_order_supporter(self, node):
        if node != TREE:
            sys.stdout.write(node.data + " ")
            self.__pre_order_supporter(node.left)
            self.__pre_order_supporter(node.right)

    def __in_order_supporter(self, node):
        if node != TREE:
            self.__in_order_supporter(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_supporter(node.right)

    def __post_order_supporter(self, node):
        if node != TREE:
            self.__post_order_supporter(node.left)
            self.__post_order_supporter(node.right)
            sys.stdout.write(node.data + " ")

    def __search_tree_supporter(self, node, key):
        if node == TREE or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_supporter(node.left, key)
        return self.__search_tree_supporter(node.right, key)

    # Handles delete operations.

    def __fix_delete(self, a):
        while a != self.root and a.red_or_black == 0:
            if a == a.first.left:
                b = a.first.right
                if b.red_or_black == 1:
                    b.red_or_black = 0
                    a.first.red_or_black = 1
                    self.left_rotate(a.first)
                    b = a.first.right
                if b.left.red_or_black == 0 and s.right.red_or_black == 0:
                    b.red_or_black = 1
                    a = a.first
                else:
                    if b.right.red_or_black == 0:
                        b.left.red_or_black = 0
                        b.red_or_black = 1
                        self.right_rotate(b)
                        b = a.first.right
                    b.red_or_black = a.first.red_or_black
                    a.first.red_or_black = 0
                    b.right.red_or_black = 0
                    self.left_rotate(a.first)
                    a = self.root
            else:
                b = a.first.left
                if b.red_or_black == 1:
                    b.red_or_black = 0
                    a.first.red_or_black = 1
                    self.right_rotate(a.first)
                    b = a.first.left
                if b.left.red_or_black == 0 and b.right.red_or_black == 0:
                    b.red_or_black = 1
                    a = a.first
                else:
                    if b.left.red_or_black == 0:
                        b.right.red_or_black = 0
                        b.red_or_black = 1
                        self.left_rotate(b)
                        b = a.first.left
                    b.red_or_black = a.first.red_or_black
                    a.first.red_or_black = 0
                    b.left.red_or_black = 0
                    self.right_rotate(a.first)
                    a = self.root
        a.red_or_black = 0

    # Handles transplant operation.


    def __rb_transplant(self, x, y):
        if x.first == None:
            self.root = y
        elif x == x.first.left:
            x.first.left = y
        else:
            x.first.right = y
        x.first = x.first

    # Works as a supporter for deleting node.

    def __delete_node_supporter(self, node, key):
        c = self.TREE
        while node != self.TREE:
            if node.data == key:
                c = node
            if node.data <= key:
                node = node.right
            else:
                node = node.left
        if c == self.TREE:
            print("Where is the tree?")
            return
        b = c
        b_original_color = b.red_or_black
        if c.left == self.TREE:
            a = c.right
            self.__rb_transplant(c, c.right)
        elif (c.right == self.TREE):
            a = c.left
            self.__rb_transplant(c, c.left)
        else:
            b = self.minimum(c.right)
            b_original_color = b.red_or_black
            a = b.right
            if b.first == c:
                a.first = b
            else:
                self.__rb_transplant(b, b.right)
                b.right = c.right
                b.right.first = b
            self.__rb_transplant(c, b)
            b.left = c.left
            b.left.first = b
            b.red_or_black = c.red_or_black
        if b_original_color == 0:
            self.__fix_delete(a)

    # Handles insert operations.

    def __fix_insert(self, p):
        while p.first.red_or_black == 1:
            if p.first == p.first.first.right:
                o = p.first.first.left
                if o.red_or_black == 1:
                    o.red_or_black = 0
                    p.first.red_or_black = 0
                    p.first.first.red_or_black = 1
                    p = p.first.first
                else:
                    if p == p.first.left:
                        p = p.first
                        self.right_rotate(p)
                    p.first.red_or_black = 0
                    p.first.first.red_or_black = 1
                    self.left_rotate(p.first.first)
            else:
                o = p.first.first.right
                if o.red_or_black == 1:
                    o.red_or_black = 0
                    p.first.red_or_black = 0
                    p.first.first.red_or_black = 1
                    p = p.first.first
                else:
                    if p == p.first.right:
                        p = p.first
                        self.left_rotate(p)
                    p.first.red_or_black = 0
                    p.first.first.red_or_black = 1
                    self.right_rotate(p.first.first)
            if p == self.root:
                break
        self.root.red_or_black = 0

    # Helps displaying the RB Tree.

    def __print_supporter(self, node, space, end):
        if node != self.TREE:
            sys.stdout.write(space)
            if end:
                sys.stdout.write("R----")
                space += "     "
            else:
                sys.stdout.write("L----")
                space += "|    "
            s_color = "RED" if node.red_or_black == 1 else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.__print_supporter(node.left, space, False)
            self.__print_supporter(node.right, space, True)

    # Function for Pre-Order traversal
    def preorder(self):
        self.__pre_order_supporter(self.root)

    # Function for In-Order traversal
    def inorder(self):
        self.__in_order_supporter(self.root)

    # Function for Post-Order traversal
    def postorder(self):
        self.__post_order_supporter(self.root)

    # Function for Search
    def searchTree(self, s):
        return self.__search_tree_supporter(self.root, s)

    # Function to find the minimum
    def minimum(self, node):
        while node.left != self.TREE:
            node = node.left
        return node

    # Function to find the maximum
    def maximum(self, node):
        while node.right != self.TREE:
            node = node.right
        return node

    # Function to find the successor
    def successor(self, a):
        if a.right != self.TREE:
            return self.minimum(a.right)
        b = a.first
        while b != self.TREE and a == b.right:
            a = b
            b = b.first
        return b

    # Function to find the predecessor
    def predecessor(self, a):
        if (a.left != self.TREE):
            return self.maximum(a.left)
        b = a.first
        while b != self.TREE and a == b.left:
            a = b
            b = b.first
        return b

    # Function to rotate left
    def left_rotate(self, a):
        b = a.right
        a.right = b.left
        if b.left != self.TREE:
            b.left.first = a

        b.first = a.first
        if a.first == None:
            self.root = b
        elif a == a.first.left:
            a.first.left = b
        else:
            a.first.right = b
        b.left = a
        a.first = b

    # Function to rotate right
    def right_rotate(self, a):
        b = a.left
        a.left = b.right
        if b.right != self.TREE:
            b.right.first = a

        b.first = a.first
        if a.first == None:
            self.root = b
        elif a == a.first.right:
            b.first.right = b
        else:
            a.first.left = b
        b.right = a
        a.first = b

    # Function to insert the key.
    def insert(self, key):
        node = Node(key)
        node.first = None
        node.data = key
        node.left = self.TREE
        node.right = self.TREE
        node.red_or_black = 1
        b = None
        a = self.root
        while a != self.TREE:
            b = a
            if node.data < a.data:
                a = a.left
            else:
                a = a.right
        node.first = b
        if b == None:
            self.root = node
        elif node.data < b.data:
            b.left = node
        else:
            b.right = node
        if node.first == None:
            node.red_or_black = 0
            return
        if node.first.first == None:
            return
        self.__fix_insert(node)

    # Function to get the root from the tree
    def get_root(self):
        return self.root

    # Function to delete the node of the tree
    def delete_node(self, data):
        self.__delete_node_supporter(self.root, data)

    # Function to display the tree
    def pretty_print(self):
        self.__print_supporter(self.root, "", True)

    # The following getHeight() and countNodes()  were added to the existing source to calculate height of the BST and -
    # to count the total number of nodes.
    # Function to calculate the height of the tree
    def getHeight(self, node):
        if node is None:
            return -1
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)
        return 1 + max(left_height, right_height)

    # Function to count the nodes of the tree
    def countNodes_(self, node):
        if node is None:
            return 0
        return 1 + self.countNodes_(node.left) + self.countNodes_(node.right)

    def countNodes(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.force(self.root)
        countNodes = 1
        while stack:
            node = stack.drag()
            if node.left:
                countNodes += 1
                stack.force(node.left)
            if node.right:
                countNodes += 1
                stack.force(node.right)
        return countNodes

# This is the main driver function for BST where it reads the 1M data ser from "rand1000000.txt".
# The following function inserts all the integers from 1M data sets and populate the
# RB Tree where it adds and deletes node.
# The total number oof height and nodes of BST are calculated.


if __name__ == "__main__":
    bst = RedBlackTree()
    nodes = []
    with open('rand1000000.txt') as f:
        content = f.readlines()
        for line in content:
            for node in line.split('-'):
                nodes.append(node.rstrip())
                # The following function automatically adds the integers from 1M data set to a RB Tree.
                bst.insert(line)

                # The following function prints the tree in order using the 1M dta set.
                # The user can choose three different orders to display the tree.
                # Insert is to add the node and delete is to remove the node fom the tree.
                # Please uncomment and run the program if you would like to add or delete node.

                '''bst.insert("****10 ****11 ****12 ****13 ****14 ****15")
                bst.insert("----21 ----22 ----23 ----24 ----25 ----26")
                bst.insert("10**** 11**** 12**** 13**** 14**** 15****")
                print("Tree after nodes are inserted:")
                print(bst.pretty_print())
                bst.delete_node('****10 ****11 ****12 ****13 ****14 ****15')
                print("Tree after nodes are deleted:")
                print(bst.pretty_print())'''

    print("The Total Height of RB Tree is:", bst.getHeight(bst.root))
    print("The total number of nodes are:", bst.countNodes_(bst.root))


```

    The Total Height of RB Tree is: 22
    The total number of nodes are: 400001
    


```python

```
