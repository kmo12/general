# Дано положительное число. Найти сумму его цифр
# Если дано не число, вернуть "Не число"

# Тесты:
# if digit == 25
#   return 7
#
# if digit == 0
#   return 0
#
# if digit == "Число"
#   return "Не число"
#
# if digit == {"1": 1, "2": 2}
#   return "Не число"


def sum_of_nums_in_digits(digit_param):
    sum_of_nums = 0
    list_of_nums = str(digit_param)

    if isinstance(digit_param, int):
        for i in list_of_nums:
            sum_of_nums += int(i)
        else:
            return sum_of_nums
    else:
        return "Не число"


digit = 25

print(sum_of_nums_in_digits(digit))

digit = {"1": 1, "2": 2}

print(sum_of_nums_in_digits(digit))