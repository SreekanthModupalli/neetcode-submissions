class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_dict = {}
        result = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]
            result.append(math.prod(remaining))
        return result