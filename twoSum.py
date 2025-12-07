from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dictionary:
                return [dictionary[complement], i]

            dictionary[nums[i]] = i


p = Solution()
print(p.twoSum([2, 11, 7, 11, 15], 9))
