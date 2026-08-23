class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        temp=[]
        print(nums)
        for i in range(len(nums)):
            target = -1*nums[i]
            left = i+1
            right = len(nums)-1
            
            while(left < right and ([nums[i],nums[left],nums[right]] not in temp) ):
                if (nums[left]+nums[right])< target:
                    print(nums[i],"Yo")
                    left+=1
                elif (nums[left]+nums[right])> target :
                    print(nums[i],"No")
                    right-=1
                else:
                    print(nums[i],"yes")
                    temp.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1    
                    right-=1
                    


        return temp



            
        