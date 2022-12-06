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


    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        time complexity = O(M+N) for m in list1, n in list2
        space complexity = O(1) because alter in place
        """
        # maintain an unchanging reference to node ahead of the return node.
        dummy = ListNode()

        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next            
            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next
