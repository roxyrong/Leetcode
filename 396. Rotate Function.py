class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        sumA = sum(A)
        B = [i for i in range(n)]
        nextRotate = sum(A[x] * B[x] for x in range(n))
        maxRotate = nextRotate
        for i in range(1, n):
            nextRotate = nextRotate + sumA - n * A.pop()
            if nextRotate > maxRotate:
                maxRotate = nextRotate
        return maxRotate