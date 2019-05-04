class Solution(object):
    def is_toeplitz_matrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        cache = matrix[0][:-1]
        for r in range(1, len(matrix)):
            if matrix[r][1:] != cache:
                return False
            else:
                cache = matrix[r][:-1]
        return True


