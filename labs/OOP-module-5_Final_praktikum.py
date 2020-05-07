# # Модуль 5. Практическая работа

# ## Создание простого интерпретатора арифметических выражений

# ### Основное задание

# Выражения содержат только целые числа, операторы и круглые скобки.
# Допустимые операторы в выражении:

# +: сложение
# -: вычитание
# *: умножение
# /: деление
# ^: возведение в степень

# Операторы не имеют приоритетов, приоритеты задаются круглыми скобками.
# Для удобства единое выражение тоже заключено в скобки.

# Дополнительно 1
# Сделайте так, чтобы код работал при любом количестве пробелов.
# Заодно избавьтесь от первой и последней круглых скобок, что бы конечный пользователь о них не думал:
# interpreter = Interpreter('1 + ( ( 2 + 3 ) * ( 4 * 5 ) )')

# Дополнительно 2
# Измените конструктор, чтобы он мог принимать не только строку кода, но и файл с кодом.
# В файле каждое выражение должно располагаться на отдельной строке.
# В этом случае результатом выполнения кода должен быть список с результатами каждого выражения.
# Например, если содержимое файла выглядит так:
# 1 + ( ( 2 + 3 ) * ( 4 * 5 ) )
# 2 + ( ( 2 * 3 ) / ( 4 ^ 5 ) )
# то
# interpreter = Interpreter(file='code.txt')
# print(interpreter.execute()) # [101, 2]

# Дополнительно 3
# Добавьте метод _validate, который будет перед исполнением кода проверять его сбалансированность скобок.

# interpreter = Interpreter('(1+((2+3)*(4*5)))')
# print(interpreter.execute()) # 101
#
# interpreter = Interpreter('(2+((2*3)/(4^5)))')
# print(interpreter.execute()) # 2


import abc
import re


class InterpreterAbstract(abc.ABC):
    """Интерпретатор кода"""

    def __init__(self, code):
        """Принимает код"""
        self.code = code

    @abc.abstractmethod
    def execute(self):
        """Запускает механизм исполнения кода
        Возвращает результат исполнения кода"""
        pass

    @abc.abstractmethod
    def _parse(self):
        """Осуществляет парсинг кода.
        Вызывает _evaluate для исполнения выражений
        Возвращает результат исполнения кода в execute"""
        pass

    @abc.abstractmethod
    def _evaluate(self, code: str):
        """Осуществляет вычисление выражения
        Возвращает результат выражения в _parse"""
        pass

    @abc.abstractmethod
    def clean_code(self, s: str):
        """Проверяет введённое выражение на ошибки со скобками, пробелами, и "\n"
        Возвращает "чистую", обработанную строчку
        Возвращает ошибку, если есть проблемы со скобками"""
        pass


class Interpreter(InterpreterAbstract):
    def __init__(self, code="", file=""):
        super().__init__(code)

        self.file = file

    def execute(self):
        if not self.code and not self.file:
            return "Введите выражение!"
        elif self.code and self.file:
            return "Выберите что-то одно:\n либо решение одного выражения, либо решение файла!"

        if self.code:
            self.clean_code()
            return self._parse()

        if self.file:
            results_list = []

            with open(self.file, "r", encoding="utf-8") as txt_file:
                for line in txt_file.readlines():
                    results_list.append(self._parse(self.clean_code(line)))

            return results_list

    def _parse(self, inner_code=None):
        if not inner_code:
            work_code = self.code
        else:
            work_code = inner_code

        o_bracket_ind = 0
        c_bracket_ind = 0

        while "(" in work_code:
            for index, char in enumerate(work_code):

                if char == "(":
                    o_bracket_ind = index
                elif char == ")":
                    c_bracket_ind = index

                    expression = work_code[o_bracket_ind:c_bracket_ind + 1]
                    work_code = work_code.replace(f"{expression}", self._evaluate(expression))

                    # Для визуализации работы
                    # print(f"{expression=}. {work_code=}")

                    break

        return work_code

    def _evaluate(self, code: str):
        if "(" in code:
            code = code.replace("(", "")
            code = code.replace(")", "")

        operator = re.search(r"[\+\-\*\/\^]", code).group()
        code = code.split(operator)

        code[0] = int(code[0])
        code[1] = int(code[1])

        if operator == "+":
            return f"{code[0] + code[1]}"
        if operator == "-":
            return f"{code[0] - code[1]}"
        if operator == "*":
            return f"{code[0] * code[1]}"
        if operator == "/":
            return f"{code[0] // code[1]}"
        if operator == "^":
            return f"{code[0] ** code[1]}"

    def clean_code(self, code_line=None):
        code_for_check = self.code or code_line

        code_for_check = code_for_check.replace(" ", "")

        # Brackets and other signs checking
        brackets_stack = []
        signs_stack = []
        signs = "+-*/^"
        for element in code_for_check:
            if element == "(" or element == ")":
                if element == "(":
                    brackets_stack.append(1)
                elif element == ")":
                    if not brackets_stack:
                        raise Exception("'(' is missing.")
                    brackets_stack.pop()

            if element in signs:
                if signs_stack:
                    raise Exception("Troubles with '+-*/^'")
                signs_stack.append(element)
            else:
                if signs_stack:
                    signs_stack.pop()

        if brackets_stack:
            raise Exception("Troubles with '()'")

        if "n" in code_for_check:
            code_for_check = code_for_check.replace("\n", "")

        if code_for_check[0] != "(":
            code_for_check = "(" + code_for_check + ")"

        if self.code:
            self.code = code_for_check
        else:
            return code_for_check


interpreter = Interpreter(file="OOP-module-5_Final_praktikum.txt")
print(interpreter.execute())  # ['101', '2']

print(Interpreter("(1+((2+3)*(4*5)))").execute())  # 101
print(Interpreter("(2+((2*3)/(4^5)))").execute())  # 2
