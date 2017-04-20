class Solution(object):

    def hammingDistance(self, x, y):

        """

        :type x: int

        :type y: int

        :rtype: int

        """

        for i in range(1):

            ham = bin(x^y)

        return ham.count('1')
