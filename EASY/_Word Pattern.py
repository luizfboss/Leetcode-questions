# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern(pattern: str, s: str) -> bool:
        string = s.split()

        if len(pattern) != len(string):
            return False
        
        else:
            seen = {}
            index = 0
            for i in range(0, len(pattern)):
                # if word has already been mapped
                if pattern[i] not in seen.values() and string[i] in seen.keys():
                        return False
                if pattern[i] in seen.values() and string[i] not in seen.keys():
                      return False
                # if the pattern char is not the same as the previously mapped, 
                # return False
                seen[string[i]] = pattern[i]
        return True

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s)) # true

pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s)) # false

pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s)) # false