# Why does this work?
# By default a binary search trees left side should always
# be less than the right side, otherwise it isn't a binary
# search tree.
# SO

# As long as the current value is not None, the loop will continue



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        while current:
            # if the target values are larger than the current value
            # traves down the tree to the right
            if p.val > current.val and q.val > current.val:
                current = current.right
            # if the target values are smaller than the current value
            # traverse to the left.
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # we stop because we reached the LCA, there is no scenario in 
            # which the node will continue to diverge because 
            # we found at least one or both values.
            else:
                return current
                
