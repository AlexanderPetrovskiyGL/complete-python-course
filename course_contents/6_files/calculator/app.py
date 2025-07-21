from addition import Addition

class Calculator:

    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, -num2)

    @classmethod
    def multiply(cls, num1, num2):
        multiply_result = num1

        for i in range(1, num2):
            multiply_result = cls.add(multiply_result, num1)
            i = cls.add(i, 1)
        return multiply_result

    @classmethod
    def divide(cls, num1, num2):
        divide_result = 0
        while num1 >= num2:
            num1 = cls.add(num1, -num2)
            divide_result = cls.add(divide_result, 1)
        return divide_result

