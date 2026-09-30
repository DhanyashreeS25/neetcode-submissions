class Solution:
    def groupAnagrams(self, strs: groups = defaultdict(list)):
        res= defaultdict(list)
        for c in strs:
            count= [0] * 26
            for s in c:
                count[ord(s)-ord("a")]+=1
            res[tuple(count)].append(c)
        return list(res.values())