# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Using a global variable to store max diameter:
        self.res = 0
        #Using DFS to calculate the height of the tree:
        def dfs(current):
            if not current:
                return 0
            #Recursively calculating the height of the left and right subtrees:
            left = dfs(current.left)
            right = dfs(current.right)
            
            #Keep updating for the result to have the maximum diameter:
            self.res = max(self.res, left + right)
            return 1 + max(left, right) #Keep going through the longer subtree
        dfs(root)
        return self.res