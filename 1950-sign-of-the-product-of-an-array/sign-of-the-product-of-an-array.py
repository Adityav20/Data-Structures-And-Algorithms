class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = nums[0]
        for i in range(len(nums)-1,0,-1):
            product *= nums[i]

        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
            