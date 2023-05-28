# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicate_erase = [k for k,v in self.countNodeValue(head).items() if v==1]
        return self.makeLinkedList(duplicate_erase)
    
    def countNodeValue(self, head):
        current_node = head
        result = collections.defaultdict(bool)
        while current_node:
            result[current_node.val] += 1
            current_node = current_node.next
        return result
    
    def makeLinkedList(self, nodes):
        head = None
        
        def LinkedList(index):
            if index < len(nodes) -1:
                return ListNode(val=nodes[index], next=LinkedList(index+1))
            return ListNode(val=nodes[index], next=None)
        
        for index, _ in enumerate(nodes):
            if not head:
                head = LinkedList(index)
        return head
            
        