class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=1
        count={}
        for i in sorted(d):
            if i-1 in count:
                count[i]=count[i-1]+1
            else:
                count[i]=1
        if(list(count.values())==[]):
            return 0
        return max(count.values())

        