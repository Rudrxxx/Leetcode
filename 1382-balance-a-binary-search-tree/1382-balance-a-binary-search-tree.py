# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def make_tree(arr):
            if not arr:
                return None
            N = len(arr)
            idx = N//2
            root = arr[idx]
            L = make_tree(arr[:idx])
            R = make_tree(arr[idx+1:])
            root.left = L
            root.right = R
            return root

        def traverse(root):
            if not root:
                return
            else:
                traverse(root.left)
                arr.append(root)
                traverse(root.right)
        
        traverse(root)
        return make_tree(arr)
        