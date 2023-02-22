'''
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Input 1:

A = [0, 1, 0, 2]
Input 2:

A = [1, 2]
Output 1:1
Output 2:0
'''
class Solution:
    def trap(self,A:list):
        # Idea here is to first calulate the max boundaries of wall, which can be calulated by
        # left max and right max arrays
        N = len(A)
        leftMax = [0]*N
        rightMax= [0]*N
        #lets populate it
        for i in range(1,N):
            leftMax[i] = max(leftMax[i-1],A[i-1])
        for i in range(N-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],A[i+1])

        #rain trapped is minimum of wall boundary - hight of wall
        total_water_trapped = 0
        for left,right,height in zip(leftMax,rightMax,A):
            dimension = min(left,right)
            water_trapped = dimension - height
            if water_trapped > 0:
                total_water_trapped += water_trapped
        return  total_water_trapped

pyhtonDSA = Solution()
A = [0, 1, 0, 2]
print (pyhtonDSA.trap(A))

