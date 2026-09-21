class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, h = 0, len(matrix)
        mid1,mid2 = 0,0;

        while l <= h:
            mid1 = l + (h - l) // 2
            if mid1 >= len(matrix):
                return False

            if matrix[mid1][0] == target:
                return True

            if matrix[mid1][0] > target:
                h = mid1 - 1
            elif matrix[mid1][-1] < target:
                l = mid1 + 1
            else:
                break;

        l, h = 0,len(matrix[0])
        while l <= h:
            mid2 = l + (h - l) // 2
            if mid2 >= len(matrix[0]):
                return False

            if matrix[mid1][mid2] == target:
                return True

            elif matrix[mid1][mid2] < target:
                l = mid2+1
            else:
                h = mid2-1

        return False