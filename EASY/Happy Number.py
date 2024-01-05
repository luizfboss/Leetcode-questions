# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def isHappy(n):

    # edge cases
    if n == 0:
        return False

    # break number into string
    n_string = str(n)
    # store previously seen numbers in a list
    seen = []
    # variable that will store the current sum
    total = 0

    while total != 1:
        print(n_string)
        # for loop to iterate through digits from current number 
        for digit in n_string:
            total += int(digit) ** 2


        # compare to return something
        # true - if number is equal to 1 -> out of while loop

        # false - if number is already in seen
        if total in seen:
            return False
        if total == 1:
            return True
        
        seen.append(total)
        n_string = str(total)
        total = 0

# Testing 
print(isHappy(19)) # True
