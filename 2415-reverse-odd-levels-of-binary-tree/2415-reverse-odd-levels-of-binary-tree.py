import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodeInfo = collections.namedtuple('nodeInfo', 'node level')
    
    def reverseBinaryTreeByBFS(self, node):
        level_node = collections.defaultdict(list)
        q = collections.deque([self.nodeInfo(node, 0)])
        previousLevel = 0
        while q:
            if not previousLevel%2 and q[0].level%2:
                start = 0
                end = len(q) - 1
                while start < end:
                    q[start].node.val, q[end].node.val = q[end].node.val, q[start].node.val
                    start += 1
                    end -= 1
            currentNode, currentLevel = q.popleft()
            previousLevel = currentLevel
            for child in [currentNode.left, currentNode.right]:
                if child:
                    q.append(self.nodeInfo(child, currentLevel + 1))

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverseBinaryTreeByBFS(root)
        return root