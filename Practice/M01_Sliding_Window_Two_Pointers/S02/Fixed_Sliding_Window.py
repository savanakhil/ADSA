# Maximum Average Subarray 1
'''from typing import List 
def findMaxAverage(nums: List[int], k:int) -> float:
    max_sum = float("-inf")
    n = len(nums)
    for i in range(0,n-k+1):
        sub_sum = 0 
        for j in range(i, k+i):
            sub_sum += nums[j]
        max_sum = max(max_sum, sub_sum)
    return max_sum/k
nums = [1, 12,-5, -6, 50, 3]
k = 4 
print(findMaxAverage(nums,k))'''

# def findMaxAverage_Optimal(nums: List[int], k:int) -> float:
#     max_sum = sum(nums[0:k])
#     n = len(nums)
#     for i in range(0,n-k+1):
#         next_sum = max_sum - nums[i] + nums[k+i]
#         max_sum = max(next_sum, max_sum)
#     return max_sum/k
# nums = [1,12,-5,-6,50,3]
# k = 4 
# print(findMaxAverage_Optimal(nums,k))

# from typing import List
# def totalFruit(f: List[int]) -> int:
#     left, ans = 0,0 
#     freq = {}
#     for right in range(len(f)):
#         freq[f[right]] = freq.get(f[right],0) + 1
#         while len(freq) > 2:
#             freq[f[left]] -= 1
#             if freq[f[left]] == 0:
#                 del freq[f[left]]
#             left += 1 
#         ans = max(ans,right-left+1)
#     return ans
# fruits = [1,2,1]
# print(totalFruit(fruits))


def lengthOfLongestSubstring(s: str) -> int:
    left,ans = 0,0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1 
        seen.add(s[right])
        ans = max(ans,right-left+1)
    return ans
s = "abcabcbb"
print(lengthOfLongestSubstring(s))