from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        compteur = {}
        for i in range(len(nums1)):
            if nums1[i] in compteur:
                compteur[nums1[i]] += 1
            else:
                compteur[nums1[i]] = 1

        resultat = []
        for num in nums2:
            if num in compteur and compteur[num] > 0:
                resultat.append(num)
                compteur[num] -= 1

        return resultat


p = Solution()
print(p.intersect([4, 4, 9, 5], [9, 4, 9, 8, 4]))
