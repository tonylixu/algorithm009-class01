def stack_method(s):
    # Itreate through the string, and use a stack to record
    # left bracket
    # For each "(", we push into stack
    #     - If the current stack length >= 1, this is not the left outer bracket,
    #       we add into result
    # For each ")", we pop the stack
    #     - If the stack length >= 1, this is not the right outer bracket,
    #       we add into the result
    # Time complexity: O(N)
    # Space complexity: O(N)
    result = ''
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            if len(stack) > 1:
                result += '('
        else:
            stack.pop()
            if len(stack) >= 1:
                result += ')'
    return result


def counter_method(s):
    """We use a counter to count the total occurrence of '(' and ')'.
    For example, '(())', counter = 0
    1. '(', counter = 1, index = 0
    2. '(', counter = 2, index = 1
    3. ')', counter = 1, index = 2
    4. ')', counter = 0, index = 3
    So whenever counter becomes 0, we reached the outmost bracket, then we simply just add
    the sub string between 0 and index to resutl

    Time complexity: O(N)
    Space complexity: O(N)
    """
    res = ''
    counter, start_pointer = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            counter += 1
        else:
            counter -= 1

        if counter == 0:
            res += s[start_pointer:i]
            start_pointer = i+1
    return res


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        return counter_method(S)

# s = "(()())(())(()(()))"
# print(stack_method(s))