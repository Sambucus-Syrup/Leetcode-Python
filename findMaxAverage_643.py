#2019/6/2
class Solution(object):
	def findMaxAverage(self,nums,k):
		lenN = len(nums)
		sum1 = sum(nums[:k])
		max_sum = sum1
		for i in range(1,lenN-k+1):
			sum1 = sum1 - nums[i-1] + nums[i+k-1]
			if sum1 > max_sum:
				max_sum = sum1
		return max_sum*1.0/k




solution = Solution()
print solution.findMaxAverage([1,12,-5,-6,50,3],4) #12.75







