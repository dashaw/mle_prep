# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        approach:
        - dfs tree
        - record how far we are down
        - keep/output max

        let's try iterative dfs!

        root = [3,9,20,null,null,15,7]

        stack = [9,20]
        foo = 20
        stack = [9]
        visited = []

        visited = [20]
        stack = [9,15,7]

        visited = [20,7]
        """
        stack = []
        visited = []
        stack.append((1,root))
        depth = 0

        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                # visit
                depth = max(current_depth,depth)
                visited.append(root.val)
                stack.append((current_depth+1,root.left))
                stack.append((current_depth+1,root.right))

        return depth

