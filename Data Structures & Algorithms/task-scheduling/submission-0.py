class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        time = 0
        mp = {}
        for task in tasks:
            if task not in mp:
              mp[task] = 0
            mp[task] += 1
        vals = mp.values()
        nvals = [-x for x in vals]
        heapq.heapify(nvals)
        while q or nvals:
            time += 1
            if nvals:
                cnt = 1 + heapq.heappop(nvals)
                if cnt != 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(nvals, q.popleft()[0])
        
        return time



        
        
        