# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r=0
        l3 = ListNode(0)
        head = l3
        curr1, curr2 = l1, l2
        while(curr1 or curr2):
            # print('---------------', curr1, curr2, r)
            if curr1 and curr2:
                # print("1")
                s = curr1.val+curr2.val+r
                if s>=10:
                    r=1
                else:
                    r=0
                l3.val = s%10
            elif curr1:
                # print("2")
                s=curr1.val + r
                if s>=10:
                    r=1
                else:
                    r=0
                l3.val = s%10
            elif curr2:
                # print("3")
                s=curr2.val + r
                if s>=10:
                    r=1
                else:
                    r=0
                l3.val = s%10
            # print('########', curr1, curr2, r)
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            if curr1 or curr2:
                l3.next = ListNode(0)
                l3=l3.next
            else:
                if r==1:

                    l3.next = ListNode(1)
                    break
                break
            # print("head: ", head)
            # print("l3: ", l3, r)
            # print("curr1: ", curr1)
            # print("curr2: ", curr2)
        # print("R: ", r)
        return head