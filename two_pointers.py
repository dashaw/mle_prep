class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        approach
        1. remove spaces, characters, lowercase
        2. reverse array in python using [::-1]
        3. see if reverse equals input

        time complexity = O(n)
        space complexity = O(n)
        """

        s = [c.lower() for c in s if c.isalnum()]
        s = ''.join(s)

        print(s)

        if s[::-1] == s:
            return True
        else:
            return False
