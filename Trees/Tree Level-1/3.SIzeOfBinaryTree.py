'''
Find the size of the binary tree

Time Complexity  : O(n)
Space Complexity : O(n)

Author : Kartik Goudar 
Date   : 3 Mar, 2023
'''

'''
Calculate the size of left and right subtrees respectively
Add 1 (current node) and return to it's parent
'''

def findSize(root):
    if not root:
        return 0
    return findSize(root.left) + findSize(root.right) + 1


# Using Level order traversal

def findSize1(root):
    if not root:
        return 0
    q =  []
    q.append(root)
    node = None
    count = 0
    while q:
        node = q.pop(0)
        count += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return count 

