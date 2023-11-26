# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(self, nums: [int]) -> int:
        seen = {}
        greatest = 0

        # mapping through array
        for i in range(0, len(nums)):
            # if it exists, add one to it
            if nums[i] in seen.keys():
                seen[nums[i]] += 1
            # if it doesnt, create item in dict
            else:
                seen[nums[i]] = 1
            
            if seen[nums[i]] > greatest:
                greatest = seen[nums[i]] 
    
        return list(seen.keys())[list(seen.values()).index(greatest)]