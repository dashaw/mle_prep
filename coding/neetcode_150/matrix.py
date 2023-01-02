class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        https://leetcode.com/problems/diagonal-traverse
        ### Examples
        * there are m + n - 1 diagonals
        * iterate through them via [r+1,c-1]
        * in some cases we need to reverse this, so use another empty array

        O(n*m)
        """
        # init vars
        n, m = len(mat), len(mat[0])
        num_diags = m + n - 1
        res = []

        for d in range(num_diags):
            foo_res = []

            r, c = 0 if d < m else d - m + 1, d if d < m else m - 1

            while r < n and c > -1:
                foo_res.append(mat[r][c])
                r += 1
                c -= 1

            if d%2==0:
                foo_res = foo_res[::-1]

            for i in foo_res:
                res.append(i)

        return res



    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # init vars
        m = len(matrix)
        n = len(matrix[0])

        """
        https://leetcode.com/problems/toeplitz-matrix/
        [[1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]]

        r = 0, c = [0,1,2]
        matrix[0][0] == matrix[1][1]?
        matrix[0][1] == matrix[1][2]?
        matrix[0][2] == matrix[1][3]?

        r = 1, c = [0,1,2]
        matrix[1][0] == matrix[2][1]?
        matrix[1][1] == matrix[2][2]
        matrix[1][2] == matrix[2][3]?
        """

        for r in range(m-1):
            for c in range(n-1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        return True
