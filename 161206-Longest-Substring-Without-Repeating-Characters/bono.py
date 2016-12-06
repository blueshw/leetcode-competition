class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        leng = 0
        po_dict = {}
        
        for i, c in enumerate(s):
            if c in po_dict.keys() and po_dict[c] >= start:
                
                max_len = max(max_len, leng)
                
                start = po_dict[c] + 1
                leng = i - start + 1
                po_dict[c] = i
            else:
                po_dict[c] = i
                leng += 1
        return max(max_len, leng)
