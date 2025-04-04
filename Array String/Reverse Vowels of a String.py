# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        nonvowels = []
        vowels =  ['a','e','i','o','u','A','E','I','O','U']
        
      reversedlst = []
        
        i = 0
        while len(lst) > i:
            if lst[i] in vowels:
                reversedlst.insert(0,lst[i])
            i +=1 

        indexrr = 0
        for i in range(len(lst)):
            if lst[i] in vowels:
                lst[i] = reversedlst[indexrr]
                indexrr +=1
         

        return "".join(lst)













