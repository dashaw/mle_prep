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

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [30, 60, 90]
        [1,1,0]

        [73,74,75,71,69,72,76,73]
        [1,1,4,2,1,1,0,0]



        [[2,75],[3,71]]

        5,72
        """

        num_temperatures = len(temperatures)
        output_array = [0]*num_temperatures
        set_temps = set(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                output_array[stack[-1][0]] = i - stack[-1][0]
                stack.pop(-1)
                
            stack.append([i,t])

        return output_array

    def isValid(self, s: str) -> bool:
        """
        RULES:
        1. open brackets must be closed by same type of bracket
        2. open backet must be closed in the correct order
        3. every close bracket as corresponding open of same type
        """
        length = len(s)
        stack = []

        def check_is_closed(i):
            if i == ')' or i =='}' or i == ']':
                return True
            return False

        def check_matching(i,j):
            if i+j == "()" or i+j == "[]" or i+j == "{}":
                return True
            return False

        if s[0] != '(' and s[0] != '[' and s[0] != '{':
            return False

        elif s[-1] == '(' or s[-1] == '[' or s[-1] == '{':
            return False

        else:
            for i in range(length):
                # push to stack
                stack.append(s[i])

                # is this a closing character
                is_closed = check_is_closed(s[i])

                if is_closed:
                    if len(stack) < 2:
                        return False
                    is_matching = check_matching(stack[-2],stack[-1])

                    if not is_matching:
                        return False
                    else:
                        stack.pop(-1)
                        stack.pop(-1)

            
            if len(stack) == 0:
                return True
            else:
                return False

    def __init__(self):
        self.stack = []
        self.min = math.inf
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        self.stack.pop()
        self.min = math.inf
        for i in self.stack:
            self.min = min(self.min, i)

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min
