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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find middle 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse from the slow part onward
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        def print_ids():
            print('------------------')
            print(f"first {id(first)}")
            print(f'second {id(second)}')
            print(f'head {id(head)}')
            print(f'previous {id(prev)}')

        while second.next:
            nxt = first.next
            print_ids()

            first.next = second
            print_ids()

            first = nxt
            print_ids()

            nxt = second.next
            print_ids()

            second.next = first
            print_ids()

            second = nxt
            print_ids()

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        approach seems like -->
        recursion until find end
        when returned counter = target,
        update pointers,
        do nothing else
        """
        dummy = ListNode()
        dummy.next = head

        if n == 0:
            return head
        elif head.next is None and n == 1:
            return head.next

        

        def recursion(node):
            nonlocal end_cnt

            if node.next:
                res = recursion(node.next)
                end_cnt += 1

            if end_cnt == n:
                # update stuff
                node.next = res

            return node.next

        end_cnt = 0
        recursion(dummy)
        return dummy.next
