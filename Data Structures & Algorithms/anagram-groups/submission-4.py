class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for string in strs:
            r = ""
            for s in sorted(string):
                r += s
            if r not in table:
                table[r] = []
            table[r].append(string)
        result = []
        for key in table:
            result.append(table[key])
        return result