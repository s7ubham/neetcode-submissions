class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans=0
        for i, j in enumerate(heights) :
            start=i
            while stack and stack[-1][1]>j:
                
                temp,t2=stack.pop()
                ans = max(ans, t2*(i-temp))
                start=temp
            stack.append([start,j])
        for i,j in stack:
            ans=max(ans,(len(heights)-i)*j)
        return ans