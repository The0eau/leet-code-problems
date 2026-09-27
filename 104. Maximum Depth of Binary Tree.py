"""
104. Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the tree is empty, the depth is 0
        if not root:
            return 0
            
        # Recursively find the max depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The depth of the current node is 1 plus the maximum of its subtrees' depths
        return 1 + max(left_depth, right_depth)

# ---------------------------------------------------------
# Helper functions and Test block to run locally
# ---------------------------------------------------------
def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a level-order list."""
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    # Note: Using None instead of 'null' for Python compatibility
    values1 = [3, 9, 20, None, None, 15, 7]
    root1 = build_tree(values1)
    print(f"Input: root = {values1}")
    print(f"Output: {solution.maxDepth(root1)}\n")
    
    # Test case 2
    values2 = [1, None, 2]
    root2 = build_tree(values2)
    print(f"Input: root = {values2}")
    print(f"Output: {solution.maxDepth(root2)}\n")
    
    # Test case 3 (Extra: Empty tree)
    values3 = []
    root3 = build_tree(values3)
    print(f"Input: root = {values3}")
    print(f"Output: {solution.maxDepth(root3)}")