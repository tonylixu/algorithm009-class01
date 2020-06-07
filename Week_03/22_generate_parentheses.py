def generate_parentheses_one(n):
    """
    Generate all the parentheses first, then use a validate function to filter
    valid combinations.

    Time complexity: O(2^2n) = O(2^n)
    Space complexity: O(n)
    """
    def helper(level, MAX, s):
        # Recursion terminator
        if level >= MAX:
            if validate(s):
                ans.append(s)
            return
        # Drill down
        helper(level + 1, MAX, s + '(')
        helper(level + 1, MAX, s + ')')

    ans = []
    helper(0, 2*n, '')
    return ans


def validate(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()
    return True if not stack else False


def generate_parentheses_two(n):
    """We only generate valid parentheses

    Time complexity: O(n)
    Space complexity; o(n)
    """

    def helper(left, right, n, s):
        # Recursion terminator
        if left == n and right == n:
            ans.append(s)
            return
        if left < n:
            helper(left + 1, right, n, s+'(')
        if left > right:
            helper(left, right+1, n, s + ')')

    ans = []
    helper(0, 0, n, '')
    return ans

if __name__ == '__main__':
    n = 3
    print(generate_parentheses_two(n))