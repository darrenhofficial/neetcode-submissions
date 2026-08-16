from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        memory = defaultdict(list)
        for string in strs:
            memory[str(sorted(string))].append(string)
        return list(memory.values())