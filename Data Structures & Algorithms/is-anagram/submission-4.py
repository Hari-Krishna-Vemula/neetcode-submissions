class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            l1=list(s)
            l2=list(t)
            for ch in s:
                if ch not in l2:
                    return False
                elif ch in l2:
                    l1.remove(ch)
                    l2.remove(ch)
                
            if len(l1)==0:
                return True
        else:
            return False