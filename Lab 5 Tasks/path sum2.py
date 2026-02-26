from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def pathSum(self, root: Optional[TreeNode], targetSum: int):
    results = []
    currentPath = []

    def dfs(node, remaining, path):
        if root is None:
            return results
        
        remaining -= node.val
        currentPath.append(node)

        if node.left is None and node.right is None:
            if remaining == 0:
                results.append(currentPath)

        dfs()

        return