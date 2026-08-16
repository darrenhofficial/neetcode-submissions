class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        if len(s) != len(t):
            return False
        sdirt ={}
        tdirt = {}
        for i in s:
            if i in sdirt:
                sdirt[i] += 1
            else :
                sdirt[i] =1
        for i in t:
            if i in tdirt:
                tdirt[i] += 1
            else :
                tdirt[i] =1
        print(sdirt)
        print(tdirt)
        for key,item in sdirt.items():
            
            if key not in tdirt or item != tdirt[key]:
                return False
        return True