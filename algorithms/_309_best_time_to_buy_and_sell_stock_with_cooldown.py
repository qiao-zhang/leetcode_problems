class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        canBuy, canSell, cooldown = 0, -prices[0], 0
        for price in prices:
            canBuy, canSell, cooldown =\
                max(canBuy, cooldown),\
                max(canBuy - price, canSell),\
                canSell + price
        return max(canBuy, cooldown)
