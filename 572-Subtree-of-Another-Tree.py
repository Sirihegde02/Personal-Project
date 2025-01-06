# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Helper function to check if two trees are identical:
        def isSameTree(p, q):
            #If both subtrees are empty:
            if not p and not q: 
                return True
            #If one subtree is empty and not the other
            if not p or not q:
                return False
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        #If the main tree is empty return False
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        #Recursively check the left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)