class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res = r
        while l<=r:
            k=l+(r-l)//2

            if self.calsum(piles,k)<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res




    def calsum(self,piles,k):
        ans=0
        for i in piles:
            if i%k !=0:
                ans+=i//k +1
            else:
                ans+=i//k
        return ans


        