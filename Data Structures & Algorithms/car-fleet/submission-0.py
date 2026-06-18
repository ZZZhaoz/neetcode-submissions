class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        my_list = []
        for i in range(len(position)):
            my_list.append((position[i], speed[i], (target - position[i]) / speed[i]))

        my_list.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for num in my_list:
            if not stack:
                stack.append(num)
            else:
                a = stack[-1]
                if num[2] <= a[2]:
                    pass

                else:
                    stack.append(num)
        return len(stack)
        