def recursive_method(n):
    if n < 10:
        return n
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return recursive_method(total)


def loop_method(n):
    if n < 10:
        return n
    total = n
    while total >= 10:
        n = total
        temp = 0
        while n != 0:
            temp += n % 10
            n //= 10
        total = temp
    return total


def module_9_method(n):
    """Number n can be written in
    F(n) = n - 9*m
    For example:
    F(24) = 24 - 9*2 = 6

    Time complexity: O(1)
    Space complexity: O(1)
    """
    if n == 0:
        return n
    return n % 9 or 9


class Solution:
    def addDigits(self, num: int) -> int:
        return module_9_method(num)
