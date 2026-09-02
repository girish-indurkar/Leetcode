class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        i = 0

        while i < len(nums) - 1:
            j = i + 1

            while j < len(nums) - 1:
                if nums[i] + nums[i+1] == nums[j] + nums[j+1]:
                    return True

                j += 1

            i += 1

        return False