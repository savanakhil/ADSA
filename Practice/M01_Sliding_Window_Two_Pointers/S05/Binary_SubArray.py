# from typing import List
# def longestSubarray(nums: List[int]) -> int:
#     left = 0 
#     zero = 0
#     max_len = 0 
#     for right in range(len(nums)):
#         if nums[right] == 0:
#             zero += 1
#         while zero > 1:
#             if nums[left] == 0:
#                 zero -= 1 
#             left += 1
#         max_len = max(max_len, right - left)
#     return max_len
# nums = [0,1,1,1,0,1,1,0,1]
# print(longestSubarray(nums))

from ast import List
def longestOnes(nums: List[int], k: int) -> int:
    left = 0 
    zero = 0 
    max_len = 0 
    for right in range(len(nums)):
        if nums[right] == 0 :
            zero += 1 
        while zero > k:
            if nums[left] == 0:
                zero -= 1 
            left += 1 
        max_len = max(max_len, right - left + 1)
    return max_len 
nums = [0,1,1,1,0,1,1,0,1]
k = 2
print(longestOnes(nums, k))