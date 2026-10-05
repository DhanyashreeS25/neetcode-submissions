class Solution:
    def isValid(self, s: str) -> bool:
        check = []

        for i in range(len(s)):

            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                check.append(s[i])

            else:
                if len(check) == 0:
                    return False

                if s[i] == ")" and check[-1] == "(":
                    check.pop()
                elif s[i] == "}" and check[-1] == "{":
                    check.pop()
                elif s[i] == "]" and check[-1] == "[":
                    check.pop()
                else:
                    return False

        return len(check) == 0