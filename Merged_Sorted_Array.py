class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        # edge cases
        if m == 0:
            for idx in range(0, n):
                nums1[idx] = nums2[idx]
            return
        if n == 0:
            return
        # normal cases
        i = 0
        j = 0
        k = 0
        cond = True
        nums1_copy = nums1.copy()
        while cond:
            if nums1_copy[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
            else:
                nums1[k] = nums1_copy[i]
                i += 1
            k += 1
            if i >= m and j < n:
                while k < (m + n) and j < n:
                    nums1[k] = nums2[j]
                    k += 1
                    j += 1
                cond = False
            if j >= n and i < m:
                while k < (m + n) and i < m:
                    nums1[k] = nums1_copy[i]
                    k += 1
                    i += 1
                cond = False


if __name__ == '__main__':
    nums1 = [0,0,0,0,0]
    nums2 = [1,2,3,4,5]
    m = 0
    n = 5
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)


# Improvements -
# 1. edge cases need to be covers (including return)
# 2. boundries check - MUST