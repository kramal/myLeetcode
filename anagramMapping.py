class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        a_map = {}
        index_map = []

        for i in range(0, len(B)):
            a_map[B[i]] = i

        for i in range(0, len(A)):
            index_map.append(a_map.get(A[i]))

        return index_map