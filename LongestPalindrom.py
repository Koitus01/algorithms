class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_list = list(s)
        result = ''

        for index, char in enumerate(s_list):
            palindrome_str = char
            for sub_char in s_list[1 + index:]:
                palindrome_str += sub_char
                palindrome_length = len(palindrome_str)
                if palindrome_length == 2 and palindrome_str[0] == palindrome_str[1] and len(result) < 2:
                    result = palindrome_str
                    break

                if palindrome_length == 3 and palindrome_str[0] == palindrome_str[-1] and len(result) < 3:
                    result = palindrome_str
                    break

                middle_of_palindrome = int(palindrome_length / 2)
                if palindrome_length % 2 == 1:
                    if palindrome_str[middle_of_palindrome][::-1] is palindrome_str[0:middle_of_palindrome]:
                        if len(result) < palindrome_length:
                            result = palindrome_str
                            break
                    # odd
                #else:
                    #break
                    # no odd

        return result



# s = 'canac'
# s_len = len(s)
# start_position = int(s_len / 2)
# print(s[-start_position:])

strings = ['cbbd', 'abac', 'cabala', 'canac', 'pi234pi', 'aaaaapipiaaaaa']

for i in strings:
    print(Solution().longestPalindrome(s=i))
