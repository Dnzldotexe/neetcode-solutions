class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        
        for index, word in enumerate(strs):
            chars = str(sorted(word))
            if chars not in group.keys():
                group[chars] = [word]
            else:
                group[chars].append(word)
        return list(group.values())