class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0] * len(temperatures)
        n=len(temperatures)
        for i in range(len(temperatures)-2,-1,-1):
            j=i+1
            while j<n and temperatures[j]<=temperatures[i]:
                if result[j]==0:
                    j=n
                    break
                j+=result[j]
            if j<n:
                result[i]=j-i
        return result


        
        


        