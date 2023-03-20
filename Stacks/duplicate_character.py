'''
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can.
#
# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
# The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
# "abbacab"--> aacab  --> cab

Approach:
We can maintain a stack where before pushing any character to stack, we will check that top of stack is same as character
to be inserted . if matches then we pop out that character from stack and dont instert that character otherwise will inster that
character.
'''

class Solution:
    def remove_duplicate(self,word):
        stack = []
        stack.append(word[0])
        for i in range(1,len(word)):
            if stack and stack[-1] == word[i]:
                stack.pop()
            else:
                stack.append(word[i])
        return ''.join(stack)
bipinSolver = Solution()
print(bipinSolver.remove_duplicate("abbaca"))
print(bipinSolver.remove_duplicate("abbacab"))
