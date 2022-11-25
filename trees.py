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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        BST propery:
        left subtree are values less than node
        right subtree are values greater than node
        left/right subtrees are also BST

        Time complexity = O(n)
        Space complexity = O(1)
        """
        
        node = root
        p_val = p.val
        q_val = q.val

        while node:
            if p_val > node.val and q_val > node.val:
                node = node.right
            elif p_val < node.val and q_val < node.val:
                node = node.left
            else:
                return node

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
        [3,9,20,null,null,15,7]

        queue = []
        visited = {}
        result = []
        depth = 1

        queue = [[1,3]]

        foo = [1,3]
        lvl = 1
        node = 3

        visited[1] = [3]

        queue = [[2,9],[2,20]]
        foo = [2,9]
        lvl = 2
        node = 9

        visited[2] = [9]

        queue = [[2,20]]
        foo = [2,20]
        lvl = 2
        node = 20

        visited[2] = [9,20]

        queue = [[3,15],[3,7]]
        """
        queue = []
        visited = {}
        result = []
        depth = 1

        queue.append([1,root])

        while queue:
            foo = queue.pop(0)
            lvl = foo[0]
            node = foo[1]
            # print(f'queue = {queue}')
            # print(f'node = {node}')

            if node:
                # add to visited
                if lvl in visited.keys():
                    visited[lvl].append(node.val)
                else:
                    visited[lvl] = [node.val]

                # add to queue
                if node.left: queue.append([lvl+1,node.left])
                if node.right: queue.append([lvl+1,node.right])

        # prepare final result
        for i in sorted(visited.keys()):
            result.append(visited[i])

        return result

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        here "invert" seems to me to swap left and right children

        so what we need to do is go through the tree and swap left/right children

        does it matter if we traverse bfs vs. dfs?

        seems like bfs is the way to go so we want to use a queue

        """

        if not root:
            return root
            
        queue = []

        queue.append(root)

        while queue:
            foo = queue.pop(0)
            foo.left, foo.right = foo.right, foo.left

            if foo.left:
                queue.append(foo.left)

            if foo.right:
                queue.append(foo.right)

        return root

    def goodNodes(self, root: TreeNode) -> int:
        """
        this feels like a dfs search problem

        approach
        - root (always good)
        - visit 1 (somehow keep track there was a 3 before, so not good)
        - visit 3 (somehow keep track that this is the max) --> good
        - visit 4 (keep track of others in path)
        - 

        so crux of this problem feels like find an elegant way to do is_max_path comparison.
        how do we keep track of path?

        so for everything we push onto stack maybe we can also keep track of max thus far
        so stack would look like [[1,3],[1,4],[1,5]]
        so propogate max thus far of parent, compare to current parent, push update max in path to stack

        actually i think what we want here is recursive dfs

        time complexity = O(N)
        space complexity = O(N) <-- stack calls
        """
        max_in_path = int(-10**5)
        num_good = 0

        def dfs(max_in_path, node):
            nonlocal num_good
            if node.val >= max_in_path:
                num_good += 1
                max_in_path = node.val

            if node.left: dfs(max_in_path, node.left)
            if node.right: dfs(max_in_path, node.right)

        dfs(max_in_path, root)

        return num_good
