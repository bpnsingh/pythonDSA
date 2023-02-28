'''
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.
A = [3, 2, 1, 3]
output = 1 as for number 2 there are 2 numberes greater than it.
A = [1, 1, 3, 3]
for 1 , 2
for 3 , 0
so output = -1
'''

'''
Brute Force , for every number check count of number greater than it.
worst case o(n^2)
Better approach:
sort array, and keep on continue on duplicate number, now for the last number
check that number against remaining length of an array.
'''
class Solution:
    def solve(self,A):
        A.sort()
        N = len(A)


        for i in range(N-1):
            if A[i] == A[i+1]:
                continue
            if A[i] == N-i-1:
                return 1
        if A[-1] == 0:#edge case
            return 1
        return -1
pythonDSA = Solution()
A = [3, 2, 1, 3]
print (pythonDSA.solve(A))
A = [1, 1, 3, 3]
print (pythonDSA.solve(A))