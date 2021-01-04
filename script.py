from typing import List


# 含有重复元素，结果要去重
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 3):
            # 跳过重复的a
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # 跳过重复的b
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, n - 1
                while lo < hi:
                    tmp = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if tmp == target:
                        ans.append([nums[i], nums[j], nums[lo], nums[hi]])
                    # 偏大要减小
                    if tmp >= target:
                        hi -= 1
                        # 跳过重复的hi
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                    # 偏小要增大
                    if tmp <= target:
                        lo += 1
                        # 跳过重复的lo
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
        return ans


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
