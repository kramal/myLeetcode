# TC = O(n)
# SC = o(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        # Time complexity = O(n^2)
        # Space complexity = O(n)
        res = [0] * len(nums)

        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    res[i] += 1
        return res
        """
        list_size = len(nums)
        result = [0] * list_size
        ordered_list = sorted(nums)
        ordered_result = [x for x in range(0, list_size)]

        for i in range(0, list_size - 1):
            if ordered_list[i] == ordered_list[i + 1]:
                ordered_result[i + 1] = ordered_result[i]

        mapping = dict(zip(ordered_list, ordered_result))

        for i in range(0, list_size):
            result[i] = mapping.get(nums[i])

        return result


