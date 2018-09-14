# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack = [root]
        output = list()
        while len(stack) != 0:
            popped = stack.pop()
            output.append(popped.val)
            if popped.right:
                stack.append(popped.right)
            if popped.left:
                stack.append(popped.left)
        return output
