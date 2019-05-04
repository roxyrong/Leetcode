class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n in [-1, 0, 1]:
            return x ** n

        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        else:
            return self.myPow(x, n // 2) ** 2 * x



