class Solution:
    def letterCombinations(self, digits: str):
        return self.string_combination(digits)

    def string_combination(self, digits):
        phone_dict = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        cmb = [''] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q in phone_dict[d]]
        return cmb

    def recursive_method(self, digits):
        """
        Build a hashmap first, for digit lookup. Then we define a recursive
        search function.

        For each digits, we call search on given digit recursively, until
        all the combination are built. The level of recursion is the number of
        digits. For example, '23' has level 2, '234' has level 3.

        Time complexity: O(3^N + 4^M), N is the number of digits have 3 letters, M is the number of
        digits have 4 letters.
        Space complexity: O(3^N + 4^M), need to save 3^N + 4^M results
        """
        if not digits:
            return []
        # Build hashmap
        phone_dict = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res = []

        def search(s, digits, level):
            # Recursion terminator
            if level == len(digits):
                res.append(s)
                return
            # Process logic
            letters = phone_dict[digits[level]]
            for j in range(len(letters)):
                search(s + letters[j], digits, level + 1)
        search('', digits, 0)
        return res
