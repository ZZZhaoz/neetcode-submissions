class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if digits == "":
            return []
        
        def dfs(i, com):
            if i >= len(digits):
                res.append(com)
                return
            for char in digitToChar[digits[i]]:
                com = com + char
                dfs(i + 1, com)
                com = com[:-1]  # Removes the last character

        dfs(0, "")
        return res

        