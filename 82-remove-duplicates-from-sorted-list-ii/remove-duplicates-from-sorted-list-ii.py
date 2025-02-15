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
            D[curr.val] = 1 if curr.val not in D else D[curr.val] + 1
            curr=curr.next
        curr=head
        while(curr):
            if head == None:
                head = curr
            if curr.val in D and D[curr.val] > 1:
                if prev:
                    prev.next = curr.next
                else:
                    head = None
            else:
                D[curr.val] = 1 
                prev=curr
            curr = curr.next
        return head
        