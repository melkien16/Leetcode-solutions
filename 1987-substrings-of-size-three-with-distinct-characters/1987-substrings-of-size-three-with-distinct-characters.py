class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ptr = 0
        count = 0

        if len(s) < 3:
            return 0
        while ptr + 2 < len(s):
            if s[ptr] != s[ptr + 1] and s[ptr] != s[ptr + 2] and s[ptr + 2] != s[ptr + 1]:
                count += 1

            ptr += 1
        return count