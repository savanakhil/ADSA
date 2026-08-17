# "(54) Spiral Traversal of a Matrix"
# from typing import List
# class Solution:
#     """
#     Problem: 54. Spiral Matrix
#     URL: https://leetcode.com/problems/spiral-matrix/
#     """
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         rows, cols = len(matrix), len(matrix[0])
#         left, right = 0, cols - 1
#         top, bottom = 0, rows - 1
#         res: List[int] = []
#         while top <= bottom and left <= right:
#             for col in range(left, right + 1):
#                 res.append(matrix[top][col])
#             top += 1

#             for row in range(top, bottom + 1):
#                 res.append(matrix[row][right])
#             right -= 1

#             if top <= bottom:
#                 for col in range(right, left - 1, -1):
#                     res.append(matrix[bottom][col])
#                 bottom -= 1

#             if left <= right:
#                 for row in range(bottom, top - 1, -1):
#                     res.append(matrix[row][left])
#                 left += 1

#         return res

# if __name__ == "__main__":
#     solution = Solution()
#     matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     print("Test Case 1 Output:", solution.spiralOrder(matrix1))
#     matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#     print("Test Case 2 Output:", solution.spiralOrder(matrix2))

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        res = [[0] * n for _ in range(n)]
        num = 1

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res[top][col] = num
                num += 1
            top += 1

            for row in range(top, bottom + 1):
                res[row][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res[bottom][col] = num
                    num += 1
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[row][left] = num
                    num += 1
                left += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    print("n = 3 Output:", solution.generateMatrix(3))
    print("n = 1 Output:", solution.generateMatrix(1))