from typing import List


class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Time complexity : O(n)
    Space complexity : O(n)
    """
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hash_tbl = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            j = hash_tbl.get(target - nums[i])
            if j and i != j:
                return [i, j]


if __name__ == '__main__':
    s = Solution()
    print(s.two_sum([3, 2, 4], 6))
