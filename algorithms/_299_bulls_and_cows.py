from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sec = Counter(secret)
        gus = Counter(guess)
        bulls = 0
        cows = sum((gus & sec).values())
        for i, l in enumerate(secret):
            if l == guess[i]:
                bulls += 1
        cows -= bulls
        return '{0:d}A{1:d}B'.format(bulls, cows)
