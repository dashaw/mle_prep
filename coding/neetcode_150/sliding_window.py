class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10e4
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit

    def characterReplacement(self, s: str, k: int) -> int:
        """
        s = "AABABBA"
        k = 1
        output = 4 --> replace ind 3 A with B and substring will equal "AABBBBA"

        sliding window
        "A"
        "AA"
        "AAB"
        "AABB" can we create subset with k = 1 moves --> no
        "ABBAB"

        time complexity = O(26*n)
        space complexity = O(1)
        """

        def compute_max_char(count_dict):
            max_count = 0
            for i in count_dict.keys():
                max_count = max(count_dict[i], max_count)

            return max_count

        len_s = len(s)
        left_pointer = 0
        right_pointer = 1
        max_subset = 0

        char_dict = {s[0]: 1}
        for right_pointer in range(1,len_s+1): # O(n)
            foo = s[left_pointer:right_pointer]

            if right_pointer == 1:
                # don't update char dict
                max_count = 1
            else:
                # update char dict and max count
                if s[right_pointer - 1] in char_dict.keys():
                    char_dict[s[right_pointer - 1]] += 1
                else:
                    char_dict[s[right_pointer - 1]] = 1

                max_count = compute_max_char(char_dict) #O(m) m characters

            if len(foo) - max_count > k:
                # not a viable solution
                left_pointer += 1

# --------
# longest-substring-without-repeating-characters
# --------
class Solution:
    def __init__(self):
        self.seen_substr = {}

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        approach
        - start small window
        - check condition
        - if valid at to max calc
        - if not valid then perturb sliding window
        
        time complexity = O(N)
        space complexity = O(N-ish)
        """

        def check_unique(substring):
            seen_dict = {}
            for i in substring:
                if i in seen_dict:
                    self.seen_substr[substring] = False
                    return False
                else:
                    seen_dict[i] = 1
            self.seen_substr[substring] = True
            return True

        len_s = len(s)
        start = 0
        end = start + 1
        max_substring = 1

        """
        abcabcbb

        len_s = 8
        foo = [a]

        end = 2
        [ab]
        max_substring = 2
        foo = [abc]
        max_susbtring = 3
        foo [abca]

        start = 1
        end = 4
        foo = [bca]
        foo = 

        """

        if s == "":
            return 0

        while end <= len_s:
            foo = s[start:end]

            if foo in self.seen_substr:
                is_unique = self.seen_substr[foo]
            else:
                is_unique = check_unique(foo)

            if is_unique:
                max_substring = max(len(foo), max_substring)
                end += 1
            else:
                start += 1
        
        return max_substring

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        approach
        - feels like a straightforward iterative scan problem
        - once we find a letter, start searching for each successive in s2, if doesn't work then restart exploration

        time complexity = O(n) --> sliding window through s2 of size s1
        space complexity = O(26?) --> O(1)
        """
        # found var
        found = False
        max_ind = 0
        len_s1 = len(s1)
        len_s2 = len(s2)

        # edge case
        if len_s1 > len_s2:
            return False

        # else work to get basic info on s1 and s2 chars
        def _compute_dict(str_subset):
            subset_dict = {}
            for i in range(len(str_subset)):
                c = str_subset[i]
                if c in subset_dict.keys():
                    subset_dict[c] += 1
                else:
                    subset_dict[c] = 1
            return subset_dict

        def _compute_matches(candidate_dict, target_dict):
            for i in target_dict.keys():
                if i not in candidate_dict:
                    return False
                else:
                    if candidate_dict[i] != target_dict[i]:
                        return False
            
            return True


        # sliding window
        left_pointer = 0
        right_pointer = len_s1
        num_slides = len_s2 - right_pointer
        s1_dict = _compute_dict(s1)
        new_window_dict = {}

        # initialize

        for i in range(num_slides+1):
            # get sample
            new_window = s2[left_pointer:right_pointer]

            # character dropoff
            c_old = s2[left_pointer-1]
            c_new = s2[right_pointer-1]

            # update dict
            if left_pointer == 0:
                new_window_dict = _compute_dict(new_window)
            else:
                new_window_dict[c_old] -= 1
                if c_new in new_window_dict.keys():
                    new_window_dict[c_new] += 1
                else:
                    new_window_dict[c_new] = 1

            # compare to s1
            if _compute_matches(new_window_dict, s1_dict):
                found = True
                break
            
            left_pointer += 1
            right_pointer += 1

        return found
