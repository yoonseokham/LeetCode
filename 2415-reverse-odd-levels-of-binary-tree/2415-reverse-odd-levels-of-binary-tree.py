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

    def get_ordered_list_of_odd_level_node(self, node):
        level_node = collections.defaultdict(list)
        q = collections.deque([self.nodeInfo(node, 0)])

        while q:
            currentNode, currentLevel = q.popleft()
            if currentLevel % 2:
                level_node[currentLevel].append(currentNode.val)
            for child in [currentNode.left, currentNode.right]:
                if child:
                    q.append(self.nodeInfo(child, currentLevel + 1))
        return level_node

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_node = self.get_ordered_list_of_odd_level_node(root)
        for key in level_node.keys():
            level_node[key].reverse()

        q = collections.deque([self.nodeInfo(root, 0)])
        index = 0

        while q:
            currentNode, currentLevel = q.popleft()
            if currentLevel % 2:
                currentNode.val = level_node[currentLevel][index]
                index += 1
            else:
                index = 0
            for child in [currentNode.left, currentNode.right]:
                if child:
                    q.append(self.nodeInfo(child, currentLevel + 1))
        return root