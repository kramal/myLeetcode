# time complexity O(n + nlogn) ~ O(n)
# space complexity O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count_hash = {}

        for i in range(0, len(nums)):
            count = num_count_hash.get(nums[i])
            if count is None:
                num_count_hash[nums[i]] = 1
            else:
                num_count_hash[nums[i]] = num_count_hash[nums[i]] + 1

        key_min = min(num_count_hash.keys(), key=(lambda k: num_count_hash[k]))

        return key_min
