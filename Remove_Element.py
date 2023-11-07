class Solution:
    def removeElement(self, nums, val: int) -> int:
        k = 0
        i = 0
        j = len(nums) - 1

        while i <= j and j >= 0:
            if nums[i] == val:
                k += 1
                while nums[j] == val and j != i:
                    k += 1
                    j -= 1
                nums[i] = nums[j]
                j -= 1
            i += 1
        return len(nums) - k


if __name__ == '__main__':
    s = Solution()
    nums = [3,3]
    val = 3
    k = s.removeElement(nums, val)
    print(nums , k)
