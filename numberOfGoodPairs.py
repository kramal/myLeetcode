# O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        # this is O(n^2) time complexity
        count_of_goods = 0
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count_of_goods += 1

        return count_of_goods
        """
        count_of_goods = 0
        elem_hash = {}

        for i in range(0, len(nums)):
            if elem_hash.get(nums[i]) is None:
                elem_hash[nums[i]] = [i]
            else:
                elem_hash[nums[i]].append(i)

        for key, value in elem_hash.items():
            if len(value) > 1:
                count_of_goods += math.comb(len(value), 2)

        return count_of_goods