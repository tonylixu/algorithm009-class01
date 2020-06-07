class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        What is ugly number?
            The ugly number sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...
        because every number can only be divided by 2, 3 and 5.

        One way to look at the sequence is to split the sequence to three groups:
        1. 1x2, 2x2, 3x2, 4x2, 5x2, ...
        2. 1x3, 2x3, 3x3, 4x3, 5x3, ...
        3. 1x5, 2x5, 3x5, 4x5, 5x5, ...
        we can find that every subsequence is the ugly-sequencce itself
        (1, 2, 3, 4, 5, ...) that multiply 2, 3 and 5.
        Now if you look at the original sequence again:
        1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ...
        it can be rewritten as:
        1, 1x2, 1x3, 2x2, 1x5, 2x3, 2x4, 3x3, 2x5, 3x4, 3x5, ...

        To calculate what's after 15, you can just traverse the sequence 1, ...15, until
        you find such p1, p3, p5 that p1*2, p3*3 and p5*5 is just bigger than 15. In this
        case, p1=8, p3=6 and p5=4.

        Since p1*2 is 16, we add 16 into the sequence, and p1++, we do the same for p3 and
        p5, until we find the nth ugly number.

        For every step, we choose the smallest one, and move one step after, including
        nums with same value.

        Time complexity: O(N), since we need to generate N ugly numbers
        Space complexity: O(N), N[] to hold N ugly numbers
        """
        ugly = [0] * n
        ugly[0] = 1
        p1 = p3 = p5 = 0
        for i in range(1, n):
            # Choose the smallest one from subsequence
            temp = [ugly[p1] * 2, ugly[p3] * 3, ugly[p5] * 5]
            ugly[i] = min(temp)
            if ugly[i] == temp[0]: p1 += 1
            if ugly[i] == temp[1]: p3 += 1
            if ugly[i] == temp[2]: p5 += 1
        return ugly[-1]
