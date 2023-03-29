class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_list = list(s)
        len_s_list = len(s_list)
        half_of_len_s_list = len_s_list / 2
        result = ''

        for index, char in enumerate(s_list):
            palindrome_str = char
            if len(result) > half_of_len_s_list:
                break
            for sub_char in s_list[1 + index:]:
                palindrome_str += sub_char
                palindrome_length = len(palindrome_str)

                middle_of_palindrome = int(palindrome_length / 2)
                if palindrome_length % 2 == 1:
                    begin_of_palindrome = palindrome_str[0:middle_of_palindrome]
                    end_of_palindrome = palindrome_str[middle_of_palindrome + 1:palindrome_length][::-1]
                else:
                    half_of_palindrome_length = middle_of_palindrome
                    begin_of_palindrome = palindrome_str[0:half_of_palindrome_length]
                    end_of_palindrome = palindrome_str[half_of_palindrome_length:palindrome_length][::-1]

                if begin_of_palindrome == end_of_palindrome:
                    if len(result) < palindrome_length:
                        result = palindrome_str

        if result == '':
            return s[0]

        return result


strings = [
    'vthbaypbzzfrgeqkfsazhvocumiiblrrcxprqhpdkifncwazfrhmimewubfxmgehebepiuhkvghnbtvyckioxavjcezgbpztkimjmugprtwhsbthytmznfdihgtiuogiixshdqhczbkhswgfqfeaxajozaazczvfbnhzgazmcvplwutfdoatytwxpoxyzggjysobgdkurqdocpakcaxzvfcpagipbqfdfwhzitlezfpdhayrroztwgfqmcfkrphzehxbyioqxxvusvhqktmdovrwlijwjdxccylqqhbfbsmmjpgknxpivysnvedjmnasjtaufzdopjmzfubyxcrfqwaulbqnhezmtaygstdtldkqeeeeqkdltdtsgyatmzehnqbluawqfrcxybufzmjpodzfuatjsanmjdevnsyvipxnkgpjmmsbfbhqqlyccxdjwjilwrvodmtkqhvsuvxxqoiybxhezhprkfcmqfgwtzorryahdpfzeltizhwfdfqbpigapcfvzxackapcodqrukdgbosyjggzyxopxwtytaodftuwlpvcmzagzhnbfvzczaazojaxaefqfgwshkbzchqdhsxiigouitghidfnzmtyhtbshwtrpgumjmiktzpbgzecjvaxoikcyvtbnhgvkhuipebehegmxfbuwemimhrfzawcnfikdphqrpxcrrlbiimucovhzasfkqegrfzzbpyabhtv',
    'cbbd',
    'abcda',
    'ccc',
    'pgaagx',
    'ac',
    'a',
    'cbbd',
    'abac',
    'cabala',
    'canac',
    'pi234pi',
    'aaaaapipiaaaaa'
]

for i in strings:
    print(Solution().longestPalindrome(s=i))
