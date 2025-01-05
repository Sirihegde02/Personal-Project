# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, current_path, current_sum):
            #Base case: (Failure coz no path) If there is no node, then return (end the branch)
            if not node:
                return

            #Add the node's val to the path and update the sum:
            current_path.append(node.val)
            current_sum += node.val

            #Base case-2: (Success) If we are the leaf and the sum is the target:
            if not node.left and not node.right and current_sum == targetSum:
                res.append(current_path.copy()) #Add a copy

            #Recursive case: Do the same for the left and right subtrees: 
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)

            #Remove the current node's val from the path and reset
            current_path.pop()
        
        dfs(root, [], 0)
        return res