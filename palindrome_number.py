from typing import List


class Solution:
    """
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
    Follow up: Could you solve it without converting the integer to a string?
    """
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False

        result = 0
        x_copy = x
        while x != 0:
            result = result * 10 + x % 10
            x //= 10
        return result == x_copy


if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome(120))
