# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    """"атрибуты"""

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    """методы"""

    def go(self):
        return f'{self.name} едит'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул на право'

    def turn_lift(self):
        return f'{self.name} повернул на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость такси {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимого для такси '
        else:
            return f'Скорость {self.name} не превышает допустимое'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость спец.техники {self.name} состовляет {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} спец.техники выше допустимого'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицейского управления'
        else:
            return f'{self.name} не из полицейского управления'


honda = SportCar(100, 'White', 'Honda', False)
opel = TownCar(35, 'Yellow', 'Opel', False)
uaz = WorkCar(70, 'Black', 'UAZ', True)
porsche = PoliceCar(120, 'Silver', 'Porsche', True)
print(uaz.turn_lift())
print(f'Когда {opel.turn_right()}, тогда {honda.stop()}')
print(f'{uaz.go()} со скоростью: {uaz.show_speed()}')
print(f'{uaz.name} его цвет {uaz.color}')
print(f'{honda.name} это машина полиции? {honda.is_police}')
print(f'{uaz.name} это машина полиции? {uaz.is_police}')
print(honda.show_speed())
print(opel.show_speed())
print(porsche.police())
print(porsche.show_speed())