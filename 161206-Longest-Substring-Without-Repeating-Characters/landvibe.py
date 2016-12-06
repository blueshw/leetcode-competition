class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        maxValue = 0
        start = 0
        for i, c in enumerate(s):
            length = i - start
            if c in dic and dic[c] >= start:
                start = dic[c] + 1
            elif len(s) - 1 == i:
                length += 1
            maxValue = length if length > maxValue else maxValue
                
            dic[c] = i
        return maxValue
