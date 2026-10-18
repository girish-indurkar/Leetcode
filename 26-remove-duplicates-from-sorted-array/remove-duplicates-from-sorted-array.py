class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 1
        k = 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                continue
            else:
                nums[i+1] = nums[j]
                i+=1
                j+=1
                k+=1
        return k

        # tc = O(n)
        # SC = O(1)