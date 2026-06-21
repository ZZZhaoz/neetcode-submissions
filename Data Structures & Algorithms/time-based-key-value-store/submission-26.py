class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        candidates = self.m[key]
        l, r = 0, len(candidates) - 1
        ans = -1
        while l <= r:
            mid = (l + r)//2

            if candidates[mid][1] <= timestamp:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        if ans == -1:
            return ""
        return candidates[ans][0]
        
