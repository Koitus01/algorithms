# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(int(40 / 10))
        print(l1.val, l1.next.val, l1.next.next.val)


s = Solution()
s.addTwoNumbers(l1=ListNode(123, ListNode(234, ListNode(666))), l2=ListNode())
