# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

def canJump(nums) -> bool:
        last_index = len(nums) - 1
        i = 0

        while i < last_index:
            if nums[i] == 0:
                 return False
            if i + nums[i] > last_index:
                return False
            elif i + nums[i] == last_index:
                return True
            else:
                i = i + nums[i]
            print(i)
        return True

nums = [2,3,1,1,4]
print(canJump(nums)) # true

nums = [3,2,1,0,4]
print(canJump(nums)) # false