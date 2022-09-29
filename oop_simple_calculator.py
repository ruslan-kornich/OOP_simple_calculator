class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __convert_types(value_str):
        if isinstance(value_str, str):
            if "." in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def parse(self, expression):
        packed_values = tuple(expression.split(' '))
        if len(packed_values) < 3:
            print('Wrong indentation, check your expression')
            return 0, 0, '+'
        first_value, operator, second_value = packed_values
        return self.__convert_types(first_value), self.__convert_types(second_value), operator


class Core:
    def __init__(self):
        self._parcer = Parser()
        self._functions = {
            '+': lambda first_value, second_value: first_value + second_value,
            '-': lambda first_value, second_value: first_value - second_value,
            '/': lambda first_value, second_value: first_value / second_value,
            '*': lambda first_value, second_value: first_value * second_value
        }

    def calculate(self, expression):
        first_value, second_value, operator = self._parcer.parse(expression)
        result = self._functions.get(operator)(first_value, second_value)
        return result


class Interface:
    def __init__(self):
        self._core = Core()

    def run_calculator(self):
        while True:
            print("Enter your expression: eg. '2 + 2'")
            expression = input()
            result = self._core.calculate(expression)
            print(f"Result : {result}")
            print("*" * 10)


if __name__ == '__main__':
    calculator = Interface()
    calculator.run_calculator()
