# LeetCode 49

from collections import defaultdict

class Solution:

    # Solution: sorting
    # Time  Complexity: O(nklogk) -> n is len of inputted array, k is max length of string in inputted array
    # Space Complexity: O(nk)
    def groupAnagrams1(self, strs):
        
        hashAnagram = defaultdict(list)
        
        for i in strs:
            anagrammed = ''.join(sorted(i))
            hashAnagram[anagrammed].append(i)
            
        return hashAnagram.values()

    # Solution: counting number of characters 
    # Time  Complexity: O(nk) -> n is len of inputted array, k is max length of string in inputted array
    # Space Complexity: O(nk)
    def groupAnagrams2(self, strs):

        hashAnagram = defaultdict(list)

        for i in strs:
            letters = [0] * 26
        
            for char in i:
                letters[ord(char) - ord('a')] += 1

            hashAnagram[tuple(letters)].append(i)
        
        return hashAnagram.values()


# TESTING
obj = Solution()
print(obj.groupAnagrams1(["eat","tea","tan","ate","nat","bat"]))
print(obj.groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))