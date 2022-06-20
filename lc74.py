class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix) * len(matrix[0])
        l = 0
        while l != r:
            k = (l+r) // 2
            if matrix[k // len(matrix[0])][k % len(matrix[0])] == target:
                return True
            elif matrix[k // len(matrix[0])][k % len(matrix[0])] < target:
                l = k+1
            else:
                r = k
        return False
