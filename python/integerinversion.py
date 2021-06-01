# https://leetcode-cn.com/problems/reverse-integer/solution/ (给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0)
def reverse_force(x) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0

print(reverse_force(123))
