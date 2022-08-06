"""Задача: написати функцію сalculator для двух операндів .

   Деталі:
            * функція приймає три аргумента - лівий операнд, оператор, правий операнд
            * функція повинна повернути результат операції над операндами
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * calculate(2, "+", 2) -> повертає 4
            * calculate("hello world!", "*", 2) -> повертає "hello world!hello world!"
            * calculate(10, ")", 10) -> повертає None
"""

def calculate(first_operand, sign, second_operand):
        if sign == '+':
                return first_operand + second_operand
        elif sign == '-':
                return first_operand - second_operand
        elif sign == '*':
                return first_operand * second_operand
        elif sign == '/':
                return first_operand / second_operand
        else:
                return None

print(calculate(12, "+", 2))
print(calculate("any text as example", "*", 2))
print(calculate("any text as example", "+", '3'))
print(calculate(10, ")", 10))
print(calculate(10, "/", 10))