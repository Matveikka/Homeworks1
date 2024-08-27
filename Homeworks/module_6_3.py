class Horse:
    def __init__(self, x_distance, sound, y_distance):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__(y_distance, sound)
    def run(self, x_distance, dx):
        self.x_distance = x_distance + dx
class Eagle:
    def __init__(self, y_distance, sound):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
    def fly(self, y_distance, dy):
        self.y_distance = y_distance + dy
class Pegasus(Horse, Eagle):
    def __init__(self, x_distance, y_distance, sound):
        super().__init__(x_distance, y_distance, sound)
    def move(self, dx, dy):
        self.run(self.x_distance, dx)
        self.fly(self.y_distance, dy)
    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return print(pos)
    def voice(self):
        return print(f'{self.sound}')
p1 = Pegasus(0,0, 'Frrr')
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()