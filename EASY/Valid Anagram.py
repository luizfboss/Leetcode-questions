def isAnagram(s: str, t: str) -> bool:
        # Hash maps
        seen_s = {}
        seen_t = {}

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            if s[i] in seen_s:
                seen_s[s[i]] += 1
            else:
                seen_s[s[i]] = 1

            if t[i] in seen_t:
                seen_t[t[i]] += 1
            else:
                seen_t[t[i]] = 1  
        
        for letter in seen_s.keys():
            if letter in seen_t:
                if seen_s[letter] != seen_t[letter]:
                    return False
            else:
                return False
        return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t)) # true

s = "rat"
t = "car"
print(isAnagram(s, t)) # false