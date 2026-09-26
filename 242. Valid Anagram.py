"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        # Array of 26 zeros to represent each letter of the alphabet ('a' to 'z')
        counts = [0] * 26
        
        # Increment for letters in s and decrement for letters in t
        for i in range(len(s)):
            # ord() gives the ASCII integer for the character. 
            # Subtracting ord('a') maps the character to an index from 0 to 25.
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        # If it's a perfect anagram, all values in the array must be back to 0
        for count in counts:
            if count != 0:
                return False
                
        return True

# Test block to verify the code runs correctly
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Input: s = '{s1}', t = '{t1}'")
    print(f"Output: {solution.isAnagram(s1, t1)}\n")
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    print(f"Input: s = '{s2}', t = '{t2}'")
    print(f"Output: {solution.isAnagram(s2, t2)}\n")

    # Test case 3 (Extra: different lengths)
    s3 = "a"
    t3 = "ab"
    print(f"Input: s = '{s3}', t = '{t3}'")
    print(f"Output: {solution.isAnagram(s3, t3)}")