class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        l = 0
        longest = 0
        sett = set()
        n = len(s)
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            w = (r-l)+1
            longest = max(longest, w)
            sett.add(s[r])

        return longest


def fizzBuzz(n):
    output = ""
    if n % 3 == 0:
        output += "Fizz"
    if n % 5 == 0:
        output += "Buzz"
    if output:
        print(output)

# Example Usage
n = int(input("Enter a number: "))
fizzBuzz(n)
