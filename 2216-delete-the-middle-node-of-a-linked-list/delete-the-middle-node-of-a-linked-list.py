# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        elif head.next == None:
            return None
        else:
            curr=head
            p1=curr
            p2=None
            while(curr.next and curr.next.next):
                p2=p1
                if p1.next:
                    p1=p1.next
                curr=curr.next.next
            if curr.next == None: #Odd Length
                p2.next=p1.next
            elif curr.next.next == None: #Even Length
                p1.next=p1.next.next
            return head