class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        result = 0
        max_diff = float("inf")
        nums.sort()
        for i in range (len(nums)-2):
            left = i +1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)
                if max_diff > diff:
                    max_diff = diff
                    result = total

                if total< target:
                    left+=1
                elif total>target:
                    right -=1
                else:
        
                    break
        return result
                    


        