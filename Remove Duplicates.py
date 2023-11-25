# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
def removeDuplicates(nums: [int]) -> int:
        seen = {}
        count = 0
        for i in range(0, len(nums)):
            if nums[i] in list(seen.keys()):
                #remove from the array
                seen[nums[i]] += 1
                nums[i] = "_"

            elif nums[i] not in seen:
                seen[nums[i]] = 1
                count += 1

        for j in range(nums.count("_")):
            nums.remove("_")
        
        return len(nums)

nums = [1,1,2]
print(removeDuplicates(nums)) # 2