# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        get_nodes = LinkedListToList()
        get_nodes(head)
        nodes = get_nodes.result_list
        answer = 0
        for i, j in zip(
                range(0,
                      len(nodes) // 2),
                range(
                    len(nodes) - 1,
                    0,
                    -1,
                ),
        ):
            answer = max(
                nodes[i] + nodes[j],
                answer,
            )
        return answer


class LinkedListToList:
    def __init__(self):
        self.result_list = []

    def __call__(self, cur_node):
        if cur_node:
            self.result_list.append(cur_node.val)
            self.__call__(cur_node.next)
