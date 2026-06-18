class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        nums = self.m[key]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if timestamp >= nums[mid][1]:
                res = nums[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        if timestamp < nums[0][1]:
            return ""
        return res
        
        
