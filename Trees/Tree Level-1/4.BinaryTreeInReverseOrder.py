'''
Print the binary tree data in reverse order

Time Complexity  : O(n)
Space Complexity : O(n)

Author : Kartik Goudar
Date   : 3 Mar, 2023
'''

'''
Input: 1 2 3 4 5 6 7
Output: 4 5 6 7 2 3 1

Maintain the dequed elements in stack to get the reverse order
'''

def levelOrderInReverse(root):
    if not root:
        return 0
    
    q = []
    s = []
    q.append(root)
    node = None
    count = 0

    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        s.append(node)

    while s:
        print(s.pop())
