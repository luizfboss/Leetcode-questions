# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums: [int], target: int) -> [int]:
        seen = {}

        for i in range(0, len(nums)):
            if target - nums[i] in seen.keys():
                return [seen[target - nums[i]], i]
            else:
                seen[nums[i]] = i