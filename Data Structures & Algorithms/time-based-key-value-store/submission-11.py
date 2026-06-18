class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []        
        self.mp[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        a = self.mp[key]
        l, r = 0, len(a) - 1
        res = ""
        if timestamp < a[0][1]:
            return ""
        while l <= r:
            m = (l + r)//2
            if  a[m][1] <= timestamp:
                res = a[m]
                l = m + 1
            else:
                r = m - 1
            # else:
            #     return a[m][0]
        if res == "":
            return ""
        return res[0]
