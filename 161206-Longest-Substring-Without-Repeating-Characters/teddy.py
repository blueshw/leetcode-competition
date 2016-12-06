class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        info_dic = {}
        start_idx, max_len = 0, 0
        for index in range(0, len(s)):
            txt = s[index]
            if txt in info_dic  and start_idx <= info_dic[txt]:
                start_idx = info_dic[txt] + 1
                
            max_len = max(max_len, index - start_idx + 1)    
            info_dic.update({txt: index})
            
            
        
        return max_len