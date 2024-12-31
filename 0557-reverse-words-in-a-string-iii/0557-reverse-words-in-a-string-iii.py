class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = s.split(' ')
        new_string = ''
        for i in string_list:
            reversed_string = i[::-1]
            new_string += reversed_string + ' '
        return new_string.strip()