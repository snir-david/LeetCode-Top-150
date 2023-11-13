def validationCheck(string):
    if string == '':
        return False
    if int(string[0]) == 0:
        return False
    if int(string) > 26 or int(string) < 1:
        return False
    return True


class Solution(object):

    def helper(self, curr_num, rest_string):
        if len(rest_string) == 0 and validationCheck(curr_num):
            return 1
        elif len(rest_string) == 1:
            if validationCheck(curr_num) and validationCheck(rest_string):
                return 1
        if validationCheck(curr_num):
            return self.helper(rest_string[0:2], rest_string[2:]) + self.helper(rest_string[0], rest_string[1:])
        else:
            return 0

    def numDecodings(self, s):
        if len(s) == 1:
            if validationCheck(s):
                return 1
            else:
                return 0
        return self.helper(s[0], s[1:]) + self.helper(s[0:2], s[2:])


if __name__ == '__main__':
    s = Solution()
    num = "11062"
    k = s.numDecodings("111111111111111111111111111111111111111111111")
    print(k)
