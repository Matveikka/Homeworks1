class Vehicle:
    __COLOR_VARIANTS = ['black', 'blue', 'red', 'green', 'white']
    def __init__(self, owner, _model, _color, _engine_power):
        Vehicle.owner = owner
        Vehicle._model = _model
        Vehicle._color = _color
        Vehicle._engine_power = _engine_power
    def get_model(self):
        return print(f'Модель: {self._model}')
    def get_horsepower(self):
        return print(f'Мощность двигателя: {self._engine_power}')
    def get_color(self):
        return print(f'Цвет: {self._color}')
    def print_info(self):
        return print(f'Модель: {self._model}, Мощность двигателя: {self._engine_power}, Цвет: {self._color}, Владелец: {self.owner} ')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            print(f'{self._model} перекрашена в {new_color} цвет')
            self._color = new_color
        if new_color.lower() not in self.__COLOR_VARIANTS:
            print(f'Нельзя сменить цвет на {new_color}')
    def owner (self, new_owner):
        owner = new_owner
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()