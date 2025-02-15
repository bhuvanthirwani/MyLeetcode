# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        D={}
        if not head:
            return head
        prev, curr = None, head
        while(curr):
            if curr.val in D:
                prev.next = curr.next
            else:
                D[curr.val] = 1 
                prev=curr
            curr = curr.next
        return head