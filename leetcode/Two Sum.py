# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

test_nums = [i for i in range(25600) if i % 2 == 0]
test_nums[8009] = 1
test_target = 16021


# test_nums = [2, 7, 11, 15]
# test_target = 9

# test_nums = [-1,-2,-3,-4,-5]
# test_target = -8

# test_nums = [3, 2, 4]
# test_target = 6


# Мой Скрипт отрабатывает, но не проходит проверку по быстродействию. На данный момент я оптимизировал его насколько смог
# Отрабатывает большой список (>25000 индексов) за ~11 секунд
# class Solution:
#     def twoSum(self, nums, target):
#         # Укорачиваем лист
#         if len(nums) > 100:
#             test_list = []
#             for i, n in list(enumerate(nums)):
#                 if n <= target:
#                     test_list.append(i)
#             else:
#                 del nums[test_list[-1] + 1::]
#
#         for index, num in list(enumerate(nums)):
#             second_num = target - num
#             for index_2, num_2 in list(enumerate(nums)):
#                 if index != index_2 and index_2 >= index:
#                     if num_2 == second_num:
#                         return [index, index_2]
#         else:
#             raise Exception("No solution!")

# Скрипт из ответов на литкоде, используется система хэштаблицы
# Отрабатывает за долю секунды любой массив
def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    h = {}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]


# print(Solution().twoSum(test_nums, test_target))
print(two_sum(test_nums, test_target))
