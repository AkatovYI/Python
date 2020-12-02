# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplNum:
    def __init__(self, comp):
        self.comp = comp

    def __add__(self, other):
        return complex(self.comp.real + other.comp.real, self.comp.imag + other.comp.imag)

    def __mul__(self, other):
        return complex((self.comp.real * other.comp.real) + (self.comp.imag * other.comp.imag * (-1)),
                       (self.comp.real * other.comp.imag) + (self.comp.imag * other.comp.real))


x = complex(1, -2)
y = complex(-2, 3)
print(x, y)
# print(x.real, x.imag)
# print(y.real, y.imag)
x_1 = ComplNum(x)
y_1 = ComplNum(y)
print(x_1 + y_1)
print(x_1 * y_1)
