# Перевернуть 32 битное число (Если перевернутое или не перевернутое число не 32 бита, то отдать 0)
# Уровень Medium

test_ints = [123, -123, 12300000, 1, 0]


class IntReversing:
    def reverse(self, x: int) -> int:
        # Проверяем входное число на 32ух битность
        if abs(x) > 2**31 and x != 2**31 - 1:
            return 0
        else:
            output_int = int("".join(list(reversed(str(x))) if x >= 0 else ["-"] + list(reversed(str(x)))[0:-1]))

            # Проверяем выходное число на 32ух битность
            if abs(output_int) < 2 ** 31 and output_int != 2**31 - 1:
                return int("".join(list(reversed(str(x))) if x >= 0 else ["-"] + list(reversed(str(x)))[0:-1]))
            else:
                return 0


def int_reversing_test(ints: list) -> list:
    result = []

    for _int in ints:
        a = IntReversing().reverse(_int)
        result.append(a)

    return result


print(list(int_reversing_test(test_ints)))

# https://leetcode.com/problems/reverse-integer/submissions/
# result:
# Success
# Details
# Runtime: 36 ms, faster than 75.39% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.9 MB, less than 66.58% of Python3 online submissions for Reverse Integer.