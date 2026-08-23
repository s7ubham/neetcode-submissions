class Solution:
    def trap(self, heights: List[int]) -> int:
        ans=0
        prefix=[]
        suffix=[]
        for i in heights:
            prefix.append(max(ans,i))
            ans=max(ans,i)
        ans=0
        for j in heights[::-1]:
            suffix.append(max(ans,j))
            ans= max(ans,j)
        ans=0
        print(prefix)
        print(suffix)
        suffix=suffix[::-1]
        for i in range( len(heights)):
            ans += min(prefix[i],suffix[i])-heights[i]
        return ans

        
        