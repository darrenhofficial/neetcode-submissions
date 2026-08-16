class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for idx, string in enumerate(strs):
            locl_string = "".join(sorted(string))
            if locl_string in strs_dict:
                strs_dict[locl_string].append(strs[idx])
            else:
                strs_dict[locl_string]=[strs[idx]]
       
        return list(strs_dict.values())
