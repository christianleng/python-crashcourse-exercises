from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary1 = []
        dictionary2 = []

        for i in range(len(nums1)):
            if nums1[i] not in dictionary1:
                dictionary1.append(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] not in dictionary2:
                dictionary2.append(nums2[j])

        return list(dictionary2 + dictionary1)


p = Solution()
print(p.intersection([1, 2, 2, 1], [2, 2]))
