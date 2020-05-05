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

# import abc
#
# class InterpreterAbstract(abc.ABC):
#     '''Интерпретатор кода'''
#     
#     def __init__(self, code):
#         '''Принимает код'''
#         self.code = code
#     
#     def execute(self):
#         '''Запускает механизм исполнения кода
#         Возвращает результат исполнения кода'''
#         return self._parse()
#         
#     @abc.abstractmethod
#     def _parse(self):
#         '''Осуществляет парсинг кода.
#         Вызывает _evaluate для исполнения выражений
#         Возвращает результат исполнения кода в excecute''' 
#         pass
#     
#     @abc.abstractmethod
#     def _evaluate(self, code):
#         '''Осуществляет вычисление выражения
#         Возвращает результат выражения в _parse'''      
#         pass


# interpreter = Interpreter('(1+((2+3)*(4*5)))')
# print(interpreter.execute()) # 101
# 
# interpreter = Interpreter('(2+((2*3)/(4^5)))')
# print(interpreter.execute()) # 2




import abc
import re
import math


class InterpreterAbstract(abc.ABC):
    """Интерпретатор кода"""

    def __init__(self, code: str):
        """Принимает код"""
        self.code = code

    def execute(self):
        """Запускает механизм исполнения кода
        Возвращает результат исполнения кода"""
        return self._parse()

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
    def _brackets_checking(self, s: str):
        """Проверяет введённое выражение на ошибки со скобками
        Возвращает ошибку, если есть проблемы"""
        pass


class Interpreter(InterpreterAbstract):
    def __init__(self, code: str):
        super().__init__(code)
        self._brackets_checking(self.code)

    def _brackets_checking(self, s: str):
        brackets_stack = []

        s.replace(" ", "")

        for element in s:
            if element == "(" or element == ")":
                if element == "(":
                    brackets_stack.append(1)
                elif element == ")":
                    if not brackets_stack:
                        raise Exception("'(' is missing.")
                    brackets_stack.pop()

        if brackets_stack:
            raise Exception("Troubles with '()'")

    def _parse(self):
        work_code = self.code

        o_bracket_ind = 0
        c_bracket_ind = 0

        while "(" in work_code:
            for index, char in enumerate(work_code):

                if char == "(":
                    o_bracket_ind = index
                elif char == ")":
                    c_bracket_ind = index

                    expression = work_code[o_bracket_ind:c_bracket_ind+1]
                    work_code = work_code.replace(f"{expression}", self._evaluate(expression))

                    # Для визуализации работы
                    print(f"{expression=}. {work_code=}")

                    break

        return work_code

    def _evaluate(self, code: str):
        if "(" in code:
            code = code.replace("(", "")
            code = code.replace(")", "")

        math_sign = re.search(r"[\+\-\*\/\^]", code).group()
        code = code.split(math_sign)

        code[0] = int(math.floor(float(code[0])))
        code[1] = int(math.floor(float(code[1])))

        if math_sign == "+":
            return f"{code[0] + code[1]}"
        if math_sign == "-":
            return f"{code[0] - code[1]}"
        if math_sign == "*":
            return f"{code[0] * code[1]}"
        if math_sign == "/":
            return f"{code[0] / code[1]}"
        if math_sign == "^":
            return f"{code[0] ** code[1]}"


interpreter = Interpreter("(266+((23*34)/(2^4)))")

print(interpreter.execute())
