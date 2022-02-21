# Уровень Easy
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for index1, num1 in enumerate(nums):
            finding_num = target - num1

            for index2, num2 in enumerate(nums[index1:]):
                if index1 == index2:
                    continue
                if num2 == finding_num:
                    return [index1, index2]


checkList = [1, 4, 55, 6, 7]
target = 10

a = Solution().twoSum(checkList, target)
print(a)


# Success
# Details
# Runtime: 6656 ms, faster than 7.50% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 64.16% of Python3 online submissions for Two Sum.