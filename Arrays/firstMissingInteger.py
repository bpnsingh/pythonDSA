'''
Given an unsorted integer array, A of size N. Find the first missing positive integer.
Note: Your algorithm should run in O(n) time and use constant space.
Input 1:
[1, 2, 0]
3
Input 2:
[3, 4, -1, 1]
2
Input 3:
[-8, -7, -6]
1
'''

class Solution:
    def firstMissingInteger(self,A:list):
        '''
        This solution we are going to use index of an array to mark the presence of
        numbers, by making them -ve. At last if any number is found positive, that's index
        should be answer. If not then answer should be N.
        '''
        N = len(A)
        #lets replace all negative and zero numbers with N, as these numbers can not be our answer.
        for i,num in enumerate(A):
            if num < 1:
                A[i] = N +1
        #lets mark array elements which respective indexes are present.
        for i in range(N):
            index = abs(A[i])
            if index >= 1 and index <= N:
                j = index -1
                A[j] = -1 * abs(A[j])

        for i in range(N):
            if A[i] < 0:
                pass
            else:
                return i+1
        return N+1

DSA = Solution()
A =  [3, 4, -1, 1]
print (DSA.firstMissingInteger(A))


