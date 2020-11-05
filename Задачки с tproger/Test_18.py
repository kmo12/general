# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
# Задача 18
# Посчитайте, сколько раз символ встречается в строке.

main_stroke = "Посчитайте, сколько раз символ встречается в строке."
main_char = "а"


def reference_solution(main_stroke_inner, main_char_inner):
    return main_stroke_inner.count(f"{main_char_inner}")


def first_solution(main_stroke_inner, main_char_inner):
    counter = 0
    for char in main_stroke_inner:
        if char == main_char_inner:
            counter += 1
    return counter


def second_solution(main_stroke_inner, main_char_inner):
    chars_amount_before_replace = len(main_stroke_inner)
    main_stroke_inner = main_stroke_inner.replace(f"{main_char_inner}", "")

    return chars_amount_before_replace - len(main_stroke_inner)


def third_solution(main_stroke_inner, main_char_inner):
    for index, char in enumerate(main_stroke_inner):
        if char != main_char_inner:
            main_stroke_inner = main_stroke_inner.replace(f"{main_stroke_inner[index]}", "0")
        else:
            continue
    else:
        main_stroke_inner = main_stroke_inner.replace("0", "")

    return len(main_stroke_inner)


def all_solutions(main_stroke_inner, main_char_inner):
    solutions = (
        reference_solution,
        first_solution,
        second_solution,
        third_solution,
    )
    for solution in solutions:
        solution_result = solution(main_stroke_inner, main_char_inner)
        print(f"{solution.__name__}: {solution_result}")


all_solutions(main_stroke, main_char)
