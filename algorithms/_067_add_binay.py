class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        na = int('0b' + a, 0)
        nb = int('0b' + b, 0)
        return '{0:b}'.format(na + nb)
