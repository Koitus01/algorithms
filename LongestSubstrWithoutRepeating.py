class Solution:
    def lengthOfLongestSubstring(self, s: str):
        previous_values = []
        max_value = 0
        local_value = 0
        s_list = list(s)
        s_len = len(s)

        for index, char in enumerate(s_list):
            if index + 1 < s_len and s_list[index + 1] in previous_values and char != s_list[index - 1]:
                local_value += 1
                if max_value < local_value:
                    max_value = local_value
                local_value = 0
                previous_values = []

            if char not in previous_values:
                local_value += 1
                if max_value < local_value:
                    max_value = local_value
                previous_values.append(char)
            else:
                local_value = 1

        return max_value


substrs = [
    'anviaj', # 4
    'dvdf',  # 3
    'abcapaik',  # 4
    'abcabcbb',  # 3
    'bbbbb',  # 1
    'pwwkew',  # 3
    'aab'  # 2
]

for i in substrs:
    print(i)
    print(Solution().lengthOfLongestSubstring(i))
