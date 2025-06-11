class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for num in nums:
            if num < 0: sign *= -1
            elif num ==0 : return 0
        return sign
        
        """product = nums[0]
        for i in range(len(nums)-1,0,-1):
            product *= nums[i]

        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0 """
            