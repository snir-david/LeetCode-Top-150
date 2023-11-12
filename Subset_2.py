# Given an integer array nums that may contain duplicates, return all
# possible subsets (the power set).

# The solution set must not contain duplicate subsets.Return the solution in any order.
class Solution(object):
    def subsetsWithDup(self, nums):
        solution = [[]]
        for i in range(0, len(nums)):
            if [nums[i]] not in solution:
                solution.append([nums[i]])
            for j in range(i + 1, len(nums) + 1):
                for k in range(j + 1, len(nums) + 1):
                    subset = [nums[i]]
                    subset.extend(nums[j:k])
                    subset.sort()
                    if subset not in solution:
                        solution.append(subset)
        solution.sort()
        return solution


if __name__ == '__main__':
    s = Solution()
    nums = [4, 4, 4, 1, 4]
    k = s.subsetsWithDup(nums)
    print(k)
