'''
WAP to whcih take input of Q queries of L and R , Return true id subarray is
non decreasing and false otherwise.
input : [ 1,4,4,7,6,8,2,10,20,21] [[1,3],[3,6],[6,9]]
output:
[ 1,4,4,7,6,8,2,10,20,21]
  [0,1,2,3,4,5,6,7,8,9]
output : [4,4,7] True
[6,8,2,10]  False


Steps:
prefix_array = [0,0,0,0,1,0,1,0,0,0]
psum =  [0,0,0,0,1,1,2]
prefix_array = [0, 0, 0, 0, 0, 1, 1, 2, 2, 2]
[1,3] = psum[R] - psum[L-1]
'''

class Solution:
    def nonDecreasingSubarray(self,A:list,B: list):
        prefix_array = [0]
        N = len(A)
        for i in range(1,N):
            if A[i] >= A[i-1]:
                prefix_array.append(0)
            else:
                prefix_array.append(1)
        psum = [0]*N
        for i in range(1,N):
            psum[i] = psum[i-1] + prefix_array[i]
        for L,R in B:
            if psum[R] - psum[L-1] >= 1:
                print("{0}-{1}--> False".format(L,R))
            else:
                print("{0}-{1}--> True".format(L,R))


pythonDSA = Solution()
A=[ 1,4,4,7,6,8,2,10,20,21]
B=[[1,3],[3,6],[6,9]]
pythonDSA.nonDecreasingSubarray(A,B)
