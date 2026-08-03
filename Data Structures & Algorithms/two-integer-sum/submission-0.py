class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptyMap = {}
        for i , n in enumerate(nums):
            diff = target - n
            if diff in emptyMap:
                return [emptyMap[diff],i]
            emptyMap[n]=i
        