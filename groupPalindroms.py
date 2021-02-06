class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in results:
                results[sorted_word] = []
            if sorted_word in results:
                results[sorted_word].append(word)

        return list(results.values())
