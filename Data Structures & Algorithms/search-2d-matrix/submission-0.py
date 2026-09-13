class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row =0
        col = len(matrix)-1

        while row<=col:

            mid=row + (col-row)//2
            if target>matrix[mid][-1]:
                row= mid+1
            elif target<matrix[mid][0]:
                col = mid-1
            else:
                break
        print([row,col])
        if row>col:
            print(1111)
            return False
        l,r=0,len(matrix[0])-1
        
        macrow=(row+col)//2

        while l<=r:

            mid=l + (r-l)//2
            if target>matrix[macrow][mid]:
                l= mid+1
            elif target<matrix[macrow][mid]:
                r = mid-1
            else:
                return True
        return False
        
        
        
        


        
        