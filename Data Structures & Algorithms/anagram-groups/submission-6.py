# O(m*nlogn)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         mapa = {}
#         for stri in strs:
#             temp = stri
#             a = sorted(stri)
#             s = ""
#             for c in a:
#                 s += c 
#             if s not in mapa:
#                 mapa[s] = []
#             mapa[s].append(temp)
#         answer = []
#         for key in mapa:
#             answer.append(mapa[key])
#         return answer

# O(m*n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        answer = []
        for str in strs:
            count = [0 for i in range(26)]
            for s in str:
                count[ord(s) - ord("a")] += 1
            if tuple(count) not in res:
                res[tuple(count)] = []
            res[tuple(count)].append(str)
        for key in res:
            answer.append(res[key])
        return answer

