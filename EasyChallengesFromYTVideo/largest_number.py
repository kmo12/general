# Дано целое число some_digit. Вернуть наибольшее число,
# содержащее ровно some_digit цифр.

# Тесты
# if some_digit == 3
#   return 999
#
# if some_digit == 7
#   return 9999999
#
# if some_digit == 1
#   return 9


# Неоптимизированный и костыльный способ, который просто будет работать:
# def largest_number(digit):
#     nines = []
#     for i in range(0, digit):
#         nines.append(9)
#
#     result = ""
#     for i in nines:
#         result += str(i)
#
#     return result

def largest_number(digit):
    return (10 ** digit) - 1


some_digit = 7

print(largest_number(some_digit))
