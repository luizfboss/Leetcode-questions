# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s: str, t: str) -> bool:
    expected = 0
    s_index = 0
    t_index = 0

    # edge cases
    if s == "":
        return True
    if t == "":
        return False
    
    # for i in range(0, len(t)):
    #     if expected <= len(s)-1:
    #         print(s[expected])
    #         if s[expected] == t[i]:
    #             expected += 1
    # return expected == len(s)

    
    while t_index < len(t) and s_index < len(s):
        t_p = t[t_index]
        s_p = s[s_index]
        # if chars are the same, move index of smaller string
        if t_p == s_p:
            s_index += 1
            expected += 1
        # if different, move chars from bigger string
        print(expected)   
        if expected == len(s):
            return True  
        t_index += 1   
    return False


print(isSubsequence("abc", "ahbgdc")) # true
print(isSubsequence("axc", "ahbgdc")) # false