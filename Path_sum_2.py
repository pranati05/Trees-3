class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def preorder(root):
            stack = [(root, 0, [])]
            while stack:
                node, num, path = stack.pop()
                if node:
                    num = num + node.val
                    path = path + [node.val]
                if not node.left and not node.right:
                    if num == targetSum:
                        res.append(path)
                if node.left:
                    stack.append((node.left, num, path ))
                if node.right:
                    stack.append((node.right, num, path))

            return res
        output = preorder(root)
        return output
'''Iterative solution using stack'''  

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        return self.helper(root, 0, [], targetSum)

    def helper(self, root, num, path, targetSum):
        if not root:
            return []

        num = num + root.val
        path = path + [root.val]

        if root.left is None and root.right is None:
            if num == targetSum:
                return [path]
            return []
        return self.helper(root.left, num, path, targetSum) + self.helper(root.right, num, path,targetSum)
    
