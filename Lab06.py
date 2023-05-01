#####
##### Ф.И: Ноурузи Мехди
##### ИСУ: 317306
##### группа: R3135
#####Номер варианта: 6
#####
#В код добавлен метод перегрузки.

class Shape:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_volume(self):
        return self.a * self.b * self.c

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        c = self.c + other.c
        return Shape(a, b, c)

class HollowBody(Shape):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def calculate_volume(self):
        a_new = self.a - self.d
        b_new = self.b - self.d
        c_new = self.c - self.d
        return a_new * b_new * c_new

class MultiShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def calculate_volume(self):
        volume = 0
        for shape in self.shapes:
            volume += shape.calculate_volume()
        return volume

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка ввода. Введите число.")

def main():
    print("Введите значения сторон фигуры:")
    a = get_float_input("A: ")
    b = get_float_input("B: ")
    c = get_float_input("C: ")
    
    shape = Shape(a, b, c)
    volume = shape.calculate_volume()
    print("Объем фигуры составляет: {:.2f}".format(volume))

    hollow_body = HollowBody(a, b, c, 1)
    volume = hollow_body.calculate_volume()
    print("Объем тела с внутренней полостью составляет: {:.2f}".format(volume))

    multi_shape = MultiShape([shape, hollow_body])
    volume = multi_shape.calculate_volume()
    print("Суммарный объем нескольких фигур: {:.2f}".format(volume))

if __name__ == '__main__':
    main()
