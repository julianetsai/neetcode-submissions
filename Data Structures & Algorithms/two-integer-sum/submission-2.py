class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map with value, index
        # as you go through nums, look for target-k
        # return target-k index, and curr index
        seenIdx = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in seenIdx:
                return [seenIdx[diff], i]
            seenIdx[n]=i

        return []