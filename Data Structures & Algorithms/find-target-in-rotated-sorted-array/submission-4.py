class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
    # find the pivot

        l=0
        r=len(nums)-1
        mid = 0
        while l<r:
            mid = l + (r-l)//2

            if nums[mid]<nums[r]:
                r=mid
            else:
                l =mid +1
        print(f"Mid is {l}")
        ans1= self.binarysearch(nums[:l],target)
        ans2= self.binarysearch(nums[l:],target)
        print(f"Ans1 is {ans1}")
        if ans1 !=-1:
            return ans1
        elif ans2!=-1:
            return l +ans2
        return -1
        

    #if target <pivot bs left side
    
    #else search right
    def binarysearch(self,array,target):
        l=0
        r=len(array)-1

        while l<=r:
            mid= l+ (r-l)//2

            if array[mid]>target:
                r=mid-1
            elif array[mid]<target:

                l=mid+1
            else:
                return mid
        return -1

        