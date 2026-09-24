def diagonalSort(mat):
   rows = len(mat)
   cols = len(mat[0])

   for start_col in range(cols):
      diagonal = []
      i, j = 0, start_col

      while i < rows and j < cols:
         diagonal.append(mat[i][j])
         i += 1
         j += 1
      diagonal.sort()

      i, j = 0, start_col
      k = 0
      while i < rows and j < cols:
         mat[i][j] = diagonal[k]
         i += 1
         j += 1
         k += 1

   for start_row in range(1, rows):
      diagonal = []
      i, j = start_row, 0

      while i < rows and j < cols:
         diagonal.append(mat[i][j])
         i += 1
         j += 1

      diagonal.sort()

      i, j = start_row, 0
      k = 0
      while i < rows and j < cols:
         mat[i][j] = diagonal[k]
         i += 1
         j += 1
         k += 1
   return mat


if __name__ == '__main__':
   m, n = map(int, input().split())
   mat = []

   for i in range(m):
      mat.append(list(map(int, input().split())))
   print(diagonalSort(mat))