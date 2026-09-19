# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Find length of the list
        length = 0
        curr = head

        while curr is not None:
            length += 1
            curr = curr.next

        pos = length - n + 1

        if pos == 1:
            return head.next
        curr = head
        for _ in range(pos - 2):
            curr = curr.next
        curr.next = curr.next.next

        return head
