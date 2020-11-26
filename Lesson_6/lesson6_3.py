# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} - {self.position}'

    def get_total_income(self):
        return (f'Доход работника равен: оклад {self._income.get("wage")} + пермия {self._income.get("bonus")} = ' \
                f'{self._income.get("wage") + self._income.get("bonus")}')


work1 = Position('Иван', 'Иванов', 'программист', 20, 10)
work2 = Position('Петр', 'Петров', 'начальник', 40, 20)
print(work1.get_full_name())
print(work1.get_total_income())
print(work2.get_full_name())
print(work2.get_total_income())