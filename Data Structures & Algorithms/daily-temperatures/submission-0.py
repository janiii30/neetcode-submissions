class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [(temp, index)]
        result = [0]*len(temperatures)

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t,index = stack.pop()
                result[index] = i-index
            stack.append((temp,i))
        return result
