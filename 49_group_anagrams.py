"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for substring in strs:
            count = [0] * 26
            for char in substring:
                count[ord(char) - ord("a")] += 1
            count = tuple(count)
            if count in output.keys():
                output[count].append(substring)
            else:
                output[count] = [substring]
        return output.values()