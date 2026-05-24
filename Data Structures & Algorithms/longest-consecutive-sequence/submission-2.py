class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = sorted(set(nums))

        valid_nums = []
        longest = [nums[0]]

        for i in range(len(nums)-1):

            if nums[i] + 1 == nums[i+1]:

                if not valid_nums:
                    valid_nums.append(nums[i])

                valid_nums.append(nums[i+1])

            else:

                if len(valid_nums) > len(longest):
                    longest = valid_nums

                valid_nums = []

        if len(valid_nums) > len(longest):
            longest = valid_nums

        return len(longest)