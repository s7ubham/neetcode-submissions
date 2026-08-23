class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={} #{1:1,2:2,3:3}
        final=[[] for i in range(len(nums))]
        print(final)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in d:
            print(d)
            final[d[j]-1].append(j)
        result=[]
        for kk in final[::-1]:
            if kk!=[]:
                result.extend(kk)
        return result[:k]
            