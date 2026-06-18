class Solution:
    
    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return"fadfadfadfa"
        s = ""
        for string in strs:
            s += string
            s += "."
            # len_list.append(len(string))
        s = s[:-1]
        return s


    def decode(self, s: str) -> List[str]:
        if s == "fadfadfadfa":
            return []
        return s.split(".")

