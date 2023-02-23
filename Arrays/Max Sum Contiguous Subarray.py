'''
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
Example Input
Input 1:
 A = [1, 2, 3, 4, -10]
Input 2:
 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Example Output
Output 1:
 10
Output 2:
 6
'''
class Solution:
    def maxSubarraySum(self,A):
        ans = -float('inf')
        sum = 0
        for num in A:
            sum += num
            ans = max(ans,sum)
            if sum < 0:
                sum = 0
        return ans
pythonDSA = Solution()
A = [1, 2, 3, 4, -10]
print (pythonDSA.maxSubarraySum(A))
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print (pythonDSA.maxSubarraySum(A))