class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False
        
        dict_s = {}
        dict_t = {}

        for n in range(0,len_s):
            if s[n] not in dict_s.keys():
                dict_s[s[n]] = 1
            if t[n] not in dict_t.keys():
                dict_t[t[n]] = 1

            dict_s[s[n]] += 1
            dict_t[t[n]] += 1
        
        return dict_s == dict_t