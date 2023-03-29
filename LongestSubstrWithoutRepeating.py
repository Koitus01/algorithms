# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        max_value = 0
        s_list = list(s)

        for index, char in enumerate(s_list):
            local_max = 1
            previous_char = []
            for sub_char in s_list[1 + index:]:
                if sub_char is not char and sub_char not in previous_char:
                    local_max += 1
                else:
                    break
                previous_char.append(sub_char)

            if local_max > max_value:
                max_value = local_max

        return max_value


substrs = [
    'abcabcbb',  # 3
    'anviaj',  # 5
    'dvdf',  # 3
    'abcapaik',  # 4
    'bbbbb',  # 1
    'pwwkew',  # 3
    'aab'  # 2
]

for i in substrs:
    print(i)
    print(Solution().lengthOfLongestSubstring(i))
