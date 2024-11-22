class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        self.fee = fee
        yes = 0-prices[0]
        no = 0
        for p in prices:
            next_yes = max(yes, no - p)
            next_no = max(no, yes+p-fee)
            yes = next_yes
            no = next_no
            

        return no
            
            
