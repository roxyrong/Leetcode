from collections import Counter


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = Counter(P)

        return int(sum(v * (v - 1) / 2 for v in count.values()))

