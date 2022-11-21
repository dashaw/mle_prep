# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        input = [1->2->3->4->5]
        output = [5->4->3->2->1]
        
        iterate through, appending each to array, then reverse array
        """
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            print(prev)
            curr = nxt

        return prev



