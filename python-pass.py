

class Solution:

    @staticmethod
    def longest_palindromic(s: str) -> str:
        # initaliz the given string to empty first coz it default case.
        res = ''
        # lenth of result first wil assign to zero.
        reslen = 0

        # we go throw every single char or positon in string.
        for i in range(len(s)):
            # will cheke for odd length palindroms.

            # i have left and right pointer and assign them to  i  wich is center positon now.
            # l= left, r= right, i= center.
            l, r = i, i

            # chake if right and left in bound.
            # now is palindroms.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # update the result res, by chaking the length
                if(r - l + 1) > reslen:
                    res = s[l: r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            # will cheke for even length palindroms.
            # same at top we could extract this as function.
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1) > reslen:
                    res = s[l: r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1

        return res


fi = Solution()

# Example 1:
print(fi.longest_palindromic('babad'))
# Example 2:
print(fi.longest_palindromic('cbbd'))
# Example 3:
print(fi.longest_palindromic('a'))
# Example 4:
print(fi.longest_palindromic('ac'))
