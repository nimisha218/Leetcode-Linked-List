# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        start = dummy
        carry = 0

        while l1 and l2:
            if carry != 0:
                res = l1.val + l2.val + carry
                carry = 0
            else:
                res = l1.val + l2.val
            if res >= 10:
                start.next = ListNode(res%10)
                carry = res // 10
            else:
                start.next = ListNode(res)
            
            l1 = l1.next
            l2 = l2.next
            start = start.next
        
        while l1:
            if carry != 0:
                res = l1.val + carry
                carry = 0
            else:
                res = l1.val
            if res >= 10:
                start.next = ListNode(res%10)
                carry = res // 10
            else:
                start.next = ListNode(res)
            l1 = l1.next
            start = start.next
        
        while l2:
            if carry != 0:
                res = l2.val + carry
                carry = 0
            else:
                res = l2.val
            if res >= 10:
                start.next = ListNode(res%10)
                carry = res // 10
            else:
                start.next = ListNode(res)
            l2 = l2.next
            start = start.next
        
        if carry != 0:
            start.next = ListNode(carry)
                
        return dummy.next




        