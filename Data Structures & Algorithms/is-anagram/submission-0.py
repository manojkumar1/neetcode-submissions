class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for i in s:
            if i in smap:
                smap[i] = smap[i] + 1
            else:
                smap[i] = 1
            
        for i in t:
            if i in tmap:
                tmap[i] = tmap[i] + 1
            else:
                tmap[i] = 1
        print(smap)
        print(tmap)

        if smap == tmap:
            return True
        else:
            return False
            
        