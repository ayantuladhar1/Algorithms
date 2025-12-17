```python
# Name: Ayan Tuladhar



# This program illustrates an example of Binary Search Tree using Python
# Binary Search Tree, is a node-based binary tree data structure which has the following properties:
# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.
# There must be no duplicate nodes.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            # deleting node with one child
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root)

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root)

                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data,root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

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

# The following getHeight() and countNodes()  were added to the existing source to calculate height of the BST and -
# to count the total number of nodes.


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

    def getHeight(self, node):
        if node is None:
            return -1
        left_height = self.getHeight(node.leftChild)
        right_height = self.getHeight(node.rightChild)
        return 1 + max(left_height, right_height)

    def countNodes_(self, node):
        if node is None:
            return 0
        return 1 + self.countNodes_(node.leftChild) + self.countNodes_(node.rightChild)

    def countNodes(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.force(self.root)
        countNodes = 1
        while stack:
            node = stack.drag()
            if node.leftChild:
                countNodes += 1
                stack.force(node.leftChild)
            if node.rightChild:
                countNodes += 1
                stack.force(node.rightChild)
        return countNodes

# This is the main driver function for BST where it reads the 1M data ser from "rand1000000.txt".
# The following function inserts all the integers from 1M data sets and populate the BST where it adds and deletes node.
# The total number oof height and nodes of BST are calculated.


if __name__ == '__main__':
    tree = Tree()
    nodes = []
    with open('rand1000000.txt') as f:
        content = f.readlines()
        for line in content:
            for node in line.split('-'):
                nodes.append(node.rstrip())
                # The following function automatically adds the integers from 1M data set to a BST.
                tree.insert(line)
                # The following function prints the tree in pre order using the 1M dta set.
                # The user can choose three different orders to display the tree.
                # Inorder, PreOrder and PostOrder.
                # The following function inserts nodes to the BST
                # Please uncomment the following codes to use add and delete function.

                '''tree.insert("****10 ****11 ****12 ****13 ****14 ****15")
                tree.insert("----21 ----22 ----23 ----24 ----25 ----26")
                tree.insert("10**** 11**** 12**** 13**** 14**** 15****")
                print("Tree after nodes are inserted:")
                # The following function displays the BST in pre order after the nodes are inserted.
                print(tree.postorder())
                # The following function deletes the node from the tree.
                print("Tree after existing node is deleted:")
                tree.delete('****10 ****11 ****12 ****13 ****14 ****15')
                # The following function displays the BST after the node is deleted.
                print(tree.postorder())'''

        print("The Total height of the BST is:", tree.getHeight(tree.root))
        print("The Total number of nodes are:", tree.countNodes_(tree.root))


```

    The Total height of the BST is: 43
    The Total number of nodes are: 200000
    


```python

```
