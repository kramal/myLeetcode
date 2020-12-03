# hash map task
# TC =  O(n), SC = O(n)
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels_count = 0
        jewels_count_hash = {}

        for jewel in J:
            jewels_count_hash[jewel] = 0

        for stone in S:
            if jewels_count_hash.get(stone) is not None:
                jewels_count += 1

        return jewels_count