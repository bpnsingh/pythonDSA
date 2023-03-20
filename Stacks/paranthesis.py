'''Given a string s containing just the characters'(', ')', '{', '}', '[' and ']', determine if theinputstring is valid.

Aninputstring is valid if:

Openbracketsmustbeclosedbythesametypeofbrackets.Openbracketsmustbeclosed in thecorrectorder.Everyclosebrackethasacorrespondingopenbracketofthesametype.

Example1:

Input: s = "()"Output: true
Example2:
Input: s = "()[]{}"Output: true
Example3:
Input: s = "(]"Output: false
Constraints:

1 <= s.length <= 104
sconsistsofparenthesesonly'()[]{}'.'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closedParanthesis = {
            ")":"(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for p in s:
            if p in closedParanthesis:
                if stack and stack[-1] == closedParanthesis[p]:
                    stack.pop()
                else:
                    return  False
            else:
                stack.append(p)
        return True if not stack else False

bipinSolution = Solution()
assert bipinSolution.isValid("()") is True
assert bipinSolution.isValid("()[]{}") is True
assert bipinSolution.isValid("(]") is False
