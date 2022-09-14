class Solution:
    def sortedSquares(self, nums: list) -> list:
        import math
        if len(nums) <= 1:
            nums = [int(math.pow(i, 2)) for i in nums]
            return nums
        else:
            pivot = nums[len(nums) // 2]
            left = [i for i in nums if i < pivot]
            mid = [i for i in nums if i==pivot]
            right = [i for i in nums if i > pivot]
            return self.sortedSquares(left) + mid + self.sortedSquares(right)
        

if __name__=='__main__':
    cl = Solution()
    print(cl.sortedSquares([-4,-1,0,3,10]))

