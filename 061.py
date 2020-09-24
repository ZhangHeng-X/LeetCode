# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        curr, tail, n = head, None, 0
        while curr:
            tail, curr, n = curr, curr.next, n+1
        if n == 0 or k % n == 0:
            return head
        
        k = k % n
        curr, prev = head, None
        for _ in range(n - k):
            prev, curr = curr, curr.next
        prev.next, tail.next = None, head
        return curr
        


