from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if root is None:
        return False
    
    targetSum -= root.val

    if root.left is None and root.right is None:
        return targetSum == 0

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)




#input