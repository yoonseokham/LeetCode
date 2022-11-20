# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        datas = []
        
        def visit_all_bst(node):
            if not node:
                return
            datas.append(node.val)
            visit_all_bst(node.left)
            visit_all_bst(node.right)
        visit_all_bst(root)
        set_datas = set(datas)
        datas.sort()
        
        def lower_bound(target):
            if target in set_datas:
                return target
            start = 0
            end = len(datas) - 1
            answer  = 10**6 + 1
            while start <= end:
                mid = (start + end)//2
                if target <= datas[mid]:
                    answer = min(answer,datas[mid])
                    end = mid -1
                else:
                    start = mid + 1
            return -1 if answer == 10**6 + 1 else answer

        def upper_bound(target):
            if target in set_datas:
                return target
            start = 0
            end = len(datas) - 1
            answer  = -1
            while start <= end:
                mid = (start + end)//2
                if datas[mid] <= target:
                    answer = max(answer,datas[mid])
                    start = mid + 1
                else:
                    end = mid - 1
            return answer
        return ((upper_bound(query), lower_bound(query)) for query in queries)
