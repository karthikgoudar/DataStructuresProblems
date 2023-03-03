'''
Algorithm for insrting an element into binary tree

Time Complexity  : O(n)
Space Complexity : O(n)

Author : Kartik Goudar
Date   : 3 Mar, 2023
'''

'''
We can insert an element wherever we want
We can make use of level order treversal to insert an element
We can insert wherever we find a node whose left or right child is None.
'''

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right == None


    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.left = self.left
            self.left = temp


    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.reight = self.right
            self.right = temp


'''
Insert using level order treversal
'''

def insertBinaryTree(root, data):
    newNode = BinaryTree(data)
    if root is None:
        root = newNode
        return root
    q = []
    q.append(root)
    node = None
    while q:
        node = q.pop(0)
        if data == node.data:
            return root
        
        if node.left:
            q.append(node.left)
        else:
            node.left = newNode
            return root
        
        if node.right:
            q.append(node.right)
        else:
            node.right = newNode
    return root
