class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        if len(prices) == 2:
            return prices[1] - prices[0] if prices[1] > prices[0] else 0
        # states after Day 1
        canBuy = 0
        canSell = max(-prices[1], -prices[0])
        cooldown = prices[1] - prices[0]
        for i in range(2, len(prices):
            # states after Day i
            canBuy, canSell, cooldown =\
                max(canBuy, cooldown),\
                max(canSell, canBuy-prices[i]),\
                canSell + prices[i]
        return max(canBuy, cooldown)
