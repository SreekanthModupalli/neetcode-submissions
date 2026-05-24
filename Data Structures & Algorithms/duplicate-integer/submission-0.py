class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        print(len(set_nums))
        if len(nums) > len(set_nums):
            return True
        else:
            return False