# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode()
        cur = ret
        t = 0
        while l1 or l2:
            if not l1:
                s = l2.val
                l2 = l2.next
            elif not l2:
                s = l1.val
                l1 = l1.next
            else:
                s = l1.val + l2.val
                l1, l2 = l1.next, l2.next
            cur.next = ListNode((s + t) % 10)
            cur = cur.next
            t = (s + t) // 10
        if t:
            cur.next = ListNode(t)
        return ret.next
            