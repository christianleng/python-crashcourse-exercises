# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid_index = len(nums) // 2

        racine = TreeNode(val=mid_index)
        racine.left = self.sortedArrayToBST(nums[0:mid_index])
        racine.right = self.sortedArrayToBST(nums[mid_index + 1:])

        return racine


p = Solution()
print(p.sortedArrayToBST([-10, -3, 0, 5, 9]))
