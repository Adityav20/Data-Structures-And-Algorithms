class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        check = []
        for i in range(1, len(nums)):
            check.append(nums[i]-nums[i-1])
        if min(check) < 0 and max(check) > 0:
            return False
        return True