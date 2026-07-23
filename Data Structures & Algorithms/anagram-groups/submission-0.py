class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_gram = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in hash_gram:
                hash_gram[sorted_s].append(s)
            else:
                hash_gram[sorted_s] = [s]
        return list(hash_gram.values())