# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        nodes = []
        for list in lists:
            while list:
                nodes.append(list.val)
                list = list.next
        nodes.sort()
        head = tail =ListNode(0)
        for node in nodes:
            tail.next = ListNode(node)
            tail = tail.next
        return head.next

lists = list()
data = [[1,2,3], [0,1,5]]
for i in range(len(data)):
   lists.append(ListNode(data[i][0]))
   tail = lists[i]
   for j in range(1, len(data[i])):
      tail.next = ListNode(data[i][j])
      tail = tail.next
ans = Solution().mergeKLists(lists)
while bool(ans):
    print(ans.val, end=' ')
    ans = ans.next