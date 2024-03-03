class Solution(object):
    def twoSum(self, nums, target):
        num_index_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_index_map:
                return [num_index_map[complement], i]
            num_index_map[nums[i]] = i

# # Example usage
# nums = [2, 7, 11, 15]
# target = 9
# print(twosum(nums, target))