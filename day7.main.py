from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: if root is None, return None
        if root is None:
            return None

        # If the value matches the current node's value, return this node
        if root.val == val:
            return root

        # If the value is smaller, search the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)

        # If the value is greater, search the right subtree
        return self.searchBST(root.right, val)


# Helper function to create a binary tree from a list (for easy testing)
def create_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


# Helper function to convert the tree back into a list for easy visualization of result
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


# Example 1: [4, 2, 7, 1, 3], val = 2
root = create_tree([4, 2, 7, 1, 3])
val = 2
solution = Solution()
result = solution.searchBST(root, val)
print(result)

# Print the result subtree as a list
print(tree_to_list(result))  # Output should be [2, 1, 3]

# Example 2: [4, 2, 7, 1, 3], val = 5
val = 5
result = solution.searchBST(root, val)
print(tree_to_list(result))  # Output should be []
