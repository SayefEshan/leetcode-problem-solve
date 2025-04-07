from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputDict = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word))
            outputDict[sortedWord].append(word)
        return list(outputDict.values())
