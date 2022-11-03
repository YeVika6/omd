class Color:
    # Task 1: напечатать красную точку
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'{Color.START};{self.red};{self.green};{self.blue};{Color.MOD}●{Color.END};{Color.MOD}'

    # Task 2: сравниваем 2 цвета
    def __eq__(self, other):
        return self.red == other.red\
            and self.green == other.green\
            and self.blue == other.blue

    def __hash__(self) -> int: # Нужно сравнить по hash-у! (Вообще и без него работает)
        return hash((self.red, self.green, self.blue))

    # Task 3: смешивание цветов
    def __add__(self, other):
        if not isinstance(other, Color):
            raise ArithmeticError('Element should be Color')
        return Color(min(self.red + other.red, 255),
                     min(self.green + other.green, 255),
                     min(self.blue + other.blue, 255))

    # Task 4: оставить в списке только уникальные цвета, НУЖЕН HASH!
    def get_unique_colors(self, colors: list):
        pass

    @staticmethod
    def brightness(color, c):
        c1 = - 256 * (1 - c)
        f = (259 * (c1 + 255)) / (255 * (259 - c1))
        lr = int(f * ((color) - 128) + 128)
        return lr

    # Task 5: уменьшение контраста
    def __mul__(self, c: float):
        return Color(Color.brightness(self.red, c), Color.brightness(self.green, c), Color.brightness(self.blue, c))

    __rmul__ = __mul__


def main():
    # Task 1
    print('Задание 1')
    red = Color(255, 0, 0)
    print(red)

    # Task 2
    print('Задание 2')
    red1 = Color(255, 0, 0)
    red2 = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red == green)
    print(red1 == red2)
    print(id(red1))
    print(id(red2))

    # Task 3
    print('Задание 3')
    print(red + green)

    # Task 4
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    colors_list = [orange1, red, green, orange2]
    color_set = set(colors_list)
    print('Задание 4')
    print(color_set)

    # Task 5
    print('Задание 5')
    print(orange1)
    print(0.1 * orange1)


if __name__ == '__main__':
    main()