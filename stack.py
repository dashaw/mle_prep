class Solution:
    def generateParenthesis(self, n):

        """

        n = 3
        root_soln= ""
        soln = []
        dfs_stack = []
        
        current_string = "("
        count_open = 1
        count_closed = 0
        
        current_string = "()"
        count_open = 1
        count_closed = 1
        
        current_string = "()("
        count_open = 2
        count_closed = 1
        
        current_string = "()()"
        count_open = 2
        count_closed = 2
        
        current_string = "()()("
        count_open = 3
        count_closed = 2
        
        current_string = "()()()"
        count_open = 3
        count_open = 3
        soln = ["()()()",]
        """

        def count_character(w,c):
            cnt = 0
            for i in w:
                if i == c:
                    cnt += 1
            return cnt

        # implement DFS

        root_soln = ""
        soln = []

        def dfs(current_string,character):
            
            # add to solution
            current_string += character

            # count number of (
            count_open = count_character(current_string, "(")
            count_closed = count_character(current_string, ")")
            
            if count_closed > n or count_open > n:
                return

            if count_open == count_closed and count_open == n:
                # done & valid
                soln.append(current_string)
                return

            elif count_open == count_closed and count_open < n:
                # add an open
                dfs(current_string,"(")

            elif count_closed < count_open:
                # add closed
                dfs(current_string,")")

                # add open
                dfs(current_string,"(")
                

        
        dfs(root_soln,"(")
        
        return soln

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [[p,s] for p,s in zip(position,speed)]
        combined_sorted = sorted(combined, reverse = True)
        stack = []

        for c in combined_sorted:
            stack.append((target - c[0]) / c[1])
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop(-1)
        return len(stack)
