class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn=prices[0]
        ans=0
        for i in prices:
            ans=max(ans,i-minn)
            minn=min(i,minn)
        return ans
        