class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        return answer
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             answer[i] = j - i
        #             break
        # return answer