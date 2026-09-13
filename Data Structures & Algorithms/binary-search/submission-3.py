class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            if target<nums[l + ((r - l) // 2)]:
                r=l + ((r - l) // 2) -1
            elif target>nums[l + ((r - l) // 2)]:
                l=l + ((r - l) // 2) +1
            else:
                return l + ((r - l) // 2)
        return -1
            
    
    
        