'''
Find the max element in binary tree


Time Complexity  : O(n)
Space Complexity : O(n)


Author : Kartik Goudar 
Date   : 2 Mar, 2023

'''

max = float("-inf")  # Do not set to '0' as there may be negetive numbers in the tree

def findMax(root):
    global max 
    if not root:
        return max
    if root.data >= max:
        max = root.data
    findMax(root.left)
    findMax(root.right)
    return max

'''

How does this work?

-> Find the max element in the left sub tree
-> Find the max element in the right sub tree
-> Compare them with the root data
-> Select the one which is giving the max value

consider an example

                5         
        3               8
    2       4       6       10

Clearly the max element is 10. How does our algorithm work?

1.      root = 5 (root exists so lines 13 & 14 are skipped)
a)          5 > -inf (lines 15 & 16 are executed)
b)           check the left sub tree (line 17)
c)            our algorithm is paused as left sub tree exists(It'll stay paused until all the elements of the left sub tree are executed)


1.1.    root = 3 (left sub tree)(root exists so lines 13 & 14 are skipped)
            3 < 5 (lines 15 & 16 are skipped)
             check the left sub tree (line 17)
              our algorithm is paused as left sub tree exists(It'll stay paused until all the elements of the left sub tree are executed)
              

1.2     root = 2 (left sub tree)(root exists so lines 13 & 14 are skipped)
            2 < 5 (lines 15 & 16 are skipped)
             check the left sub tree (line 17)(line 13 is executed after the execution of line 17)(left sub tree is not present)
              line 18 is executed (again recursion is called and right sub tree is not present)
               execution of 1.2 is now compleated and the recursion root is now in (root = 3) and line 18 is executed
               

1.3     root = 4 (right sub tree)(root exists so lines 13 & 14 are skipped)
            4 < 5 (lines 15 & 16 are skipped) 
             check the left sub tree (line 17)(recursion is called and line 13 is executed after the execution of line 17)(left sub tree is not present)
              line 18 is executed (again recursion is called and right sub tree is not present)
              

        
The answers from (1.2) and (1.3) are fed to (1.1) and the algorithm is unpaused and  now the recursion is at the tree root (root = 5)
The execution of the left sub tree is complete
Now the execution of the right sub tree takes place and similer processes are taken place to obtain the answer as 10 

'''

# Same problem using Level order Traversal
# Time complextiy - O(n)
# Space complexity - O(n)
 

def findMax(root):
    if not root:
        return
    
    queue = []
    queue.append(root)
    node = None 
    max = 0

    while queue:
        node = queue.pop(0)
        if node.data > max:
            max = node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return max 
