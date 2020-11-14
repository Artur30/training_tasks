from typing import List


class Solution:
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    """
    # def reverse(self, x: int) -> int:
    #     sign_x = -1 if x < 0 else 1
    #     x = abs(x)
    #     array_numbers = []
    #     array_orders = []
    #     result = 0
    #
    #     while x != 0:
    #         array_numbers.append(x % 10)
    #         x = x // 10
    #         array_orders.append(1) if not array_orders else array_orders.append(array_orders[-1] * 10)
    #
    #     for i in range(len(array_numbers)):
    #         result += array_numbers[i] * array_orders[len(array_numbers) - 1 - i]
    #     result = result * sign_x
    #
    #     return result if -2 ** 31 <= result <= 2 ** 31 - 1 else 0

    def reverse(self, x: int) -> int:
        sign_x = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while x != 0:
            result = result * 10 + x % 10
            x = x // 10
        result *= sign_x

        return result if -2 ** 31 <= result <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
