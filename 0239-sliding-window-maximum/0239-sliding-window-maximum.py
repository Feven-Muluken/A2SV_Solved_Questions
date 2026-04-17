class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # answer = []
        # for i in range(len(nums) - k + 1):
        #     answer.append(max(nums[i: i+k]))
        # return answer
        n = len(nums)
        res = []
        dq = deque()  
        
        for i in range(n):
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Record max once window is full
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res
