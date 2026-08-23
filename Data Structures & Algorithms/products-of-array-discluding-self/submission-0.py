class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        for i in nums:
            prefix.append(prefix[-1]*i)
        for j in nums[::-1]:
            suffix.append(suffix[-1]*j)
        prefix=prefix[:-1]
        suffix=suffix[:-1]
        return [prefix[i]*suffix[::-1][i] for i in range(len(prefix))]