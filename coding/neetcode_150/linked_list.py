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

    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """ approach traverse linked-list, keep track of visited node, 
        if see a node we ahve already visited before end of list, output false
        
        space-complexity & time = O(n) for the dictionary
        """

        visited = {}

        while head:
            if head in visited.keys():
                return True
            visited[head] = 1
            head = head.next

        return False

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        traverse both lists working essentially from right to left of the number
        whenever adding the two digits > 10, then do <something> to reflect 
        time complexity = O(N) for N larger length of the two lists
	space complexity = O(N)

        l1 =
        [2,4,9]
        l2 =
        [5,6,4,9]

        Output
        [7,0,4,5]
        Expected
        [7,0,4,0,1]
        """
        carry = 0
        dummy = ListNode(-1)
        curr = dummy

        while l1 or l2:
            if not l1:
                v1 = 0
                v2 = l2.val
            elif not l2:
                v1 = l1.val
                v2 = 0
            else:
                v1 = l1.val
                v2 = l2.val

            # get new result
            v3 = v1 + v2 + carry

            # see if there is a carry issue and append result
            if v3 > 9:
                keep = v3 - 10
                if keep > 0:
                    carry = v3//10
                else:
                    carry = 1
            else:
                keep = v3
                carry = 0

            # add new ListNode and update curr pointer
            curr.next = ListNode(keep)
            curr = curr.next
            
            # update pointers
            if not l1:
                l2 = l2.next
            elif not l2:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        """
	https://leetcode.com/problems/copy-list-with-random-pointer/
        #### Approach
        1. create hash map linking old node to new node
        2. iterate through linked list again but create full structure now that we have every node mapped
        """
        # initial vars
        old_copy = {None:None}
        curr = head

        while curr:
            old_copy[curr] = Node(curr.val)
            curr = curr.next

        # new linked list
        curr = head

        while curr:
            copy = old_copy[curr]
            copy.next = old_copy[curr.next]
            copy.random = old_copy[curr.random]
            curr = curr.next

        return old_copy[head]

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/swap-nodes-in-pairs/
        #### Approach
        1. iterate through linked list, for every two nodes swap their node.nexts
        2. do not modify the values in the list's nodes

        curr = head
        tmp_back -> 1
        curr -> 2
        tmp_ahead -> 3
        tmp_back.next -> 3

        """
        # initial vars
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save
            next_pointer = curr.next.next
            second = curr.next

            # reverse
            second.next = curr
            curr.next = next_pointer
            prev.next = second

            # update
            prev = curr
            curr = next_pointer

        return dummy.next
