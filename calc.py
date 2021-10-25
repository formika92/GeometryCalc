class Figure:
    """
    Базовый класс фигуры
    """
    title = 'Фигура'

    def __str__(self):
        return self.title

    def perimeter(self):
        """
        Расчет периметра фигуры
        """
        pass

    def square(self):
        """
        Расчет площади фигуры
        """
        pass

    def median(self):
        """
        Расчет медианы фигуры
        """
        pass

    def height(self):
        """
        Расчет высоты фигуры
        """
        pass

    def circumference(self):
        """
        Расчет длины окружности фигуры
        """
        pass

    def volume(self):
        """
        Расчет объема фигуры
        """
        pass


class FigureEnum:
    """
    Список названий фигур
    """

    СIRCLE = 1
    GUADRATE = 2
    RECTANGLE = 3
    TRAPEZOID = 4
    RHOMBUS = 5
    SPHERE = 6
    CUBE = 7
    PAPALLEPIPED = 8
    СYLINDER = 9
    CONE = 10

    VALUES = {
        1: 'Круг',
        2: 'Квадрат',
        3: 'Прямоугольник',
        4: 'Трапеция',
        5: 'Ромб',
        6: 'Сфера',
        7: 'Куб',
        8: 'Параллепипед',
        9: 'Цилиндр',
        10: 'Конус',
    }


class Сircle(Figure):
    """
    Класс круга
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.СIRCLE
    )
    # число Пи
    P = 3.14

    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2*self.P*self.radius


class Trapezoid(Figure):
    """
    Класс трапеции
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.TRAPEZOID
    )

    def __init__(self,
                 side_length_1,
                 side_length_2,
                 side_length_3,
                 side_length_4,
                 ):
        self.side_length_1 = side_length_1,
        self.side_length_2 = side_length_2,
        self.side_length_3 = side_length_3,
        self.side_length_4 = side_length_4,

    def perimeter(self):
        return self.side_length_1 + self.side_length_2 + self.side_length_3 + self.side_length_4  # noqa


class Rectangle(Trapezoid):
    """
    Класс прямоугольника
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.RECTANGLE
    )

    def __init__(self, side_length_1, side_length_2):
        self.side_length_1 = side_length_1
        self.side_length_2 = side_length_2
        self.side_length_3 = side_length_1
        self.side_length_4 = side_length_2


class Guadrate(Rectangle):
    """
    Класс квадрата
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.GUADRATE
    )

    def __init__(self, side_length: int):
        self.side_length_1 = side_length
        self.side_length_2 = side_length
        self.side_length_3 = side_length
        self.side_length_4 = side_length


class Rhombus(Figure):
    """
    Класс ромба
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.RHOMBUS
    )


class Sphere(Figure):
    """
    Класс сферы
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.SPHERE
    )


class Cube(Figure):
    """
    Класс куба
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.CUBE
    )


class Parallelepiped(Figure):
    """
    Класс параллепипеда
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.PAPALLEPIPED
    )


class Cylinder(Figure):
    """
    Класс цилиндра
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.СYLINDER
    )


class Cone(Figure):
    """
    Класс конуса
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.CONE
    )


class FigureClassesEnum(FigureEnum):
    """
    Список классов фигур
    """
    VALUES = {
        1: Сircle,
        2: Guadrate,
        3: Rectangle,
        4: Trapezoid,
        5: Rhombus,
        6: Sphere,
        7: Cube,
        8: Parallelepiped,
        9: Cylinder,
        10: Cone,
    }


class MethodsNamesEnums:
    """
    Список наименований методов
    """
    PERIMETER = 1
    SQUARE = 2
    MEDIAN = 3
    HEIGHT = 4
    CIRCUMFENETCE = 5
    VOLUME = 6

    VALUES = {
        1: 'Периметр',
        2: 'Площадь',
        3: 'Медиана',
        4: 'Длина окружности',
        5: 'Высота',
        6: 'Объем',
    }


class MethodsEnums(MethodsNamesEnums):
    """
    Список названий методов в классе
    """
    VALUES_LIST = {
        1: 'perimeter',
        2: 'square',
        3: 'median',
        4: 'circumference',
        5: 'height',
        6: 'volume',
    }


class Calc:
    """
    Класс калькулятора
    """
    title = 'Калькулятор'

    def __str__(self):
        return self.title

    @staticmethod
    def call_method(obj, name):
        """
        Вызывает метод класса по имени
        """
        return getattr(obj, name)()

    # @staticmethod
    # def list_methods(some_class):
    #     """
    #     Получает список методов класса
    #     """
    #     method_list = []
    #     for attribute in dir(some_class):
    #         attribute_value = getattr(some_class, attribute)
    #         if callable(attribute_value):
    #             if not attribute.startswith('__'):
    #                 method_list.append(attribute)
    #
    #     return method_list

    @staticmethod
    def validate(value):
        """
        Валидация введенных параметров
        """
        try:
            value = int(value)
            return value
        except TypeError:
            print('Вы ввели неверное значение, попробуйте еще')

    def input_parametrs(self, figure: int, method: str):
        """
        Ввод параметров
        """
        if figure == 1:
            radius = input('Введите радиус: ')
            radius = self.validate(radius)
            if radius:
                сircle = Сircle(radius=radius)
                return self.call_method(obj=сircle, name=method)
        if figure == 2:
            side_length = input('Введите длину стороны: ')
            side_length = self.validate(side_length)
            if side_length:
                guadrate = Guadrate(side_length=side_length)
                return self.call_method(obj=guadrate, name=method)
            
        if figure == 3:
            side_length_1 = input('Введите длину стороны 1: ')
            side_length_1 = self.validate(side_length_1)
            if side_length_1:
                side_length_2 = input('Введите длину стороны 2: ')
                side_length_2 = self.validate(side_length_2)
                if side_length_2:
                    rectangle = Rectangle(
                        side_length_1=side_length_1,
                        side_length_2=side_length_2,
                        )
                    return self.call_method(obj=rectangle, name=method)
            
        if figure == 4:
            side_length_1 = input('Введите длину стороны 1: ')
            side_length_1 = self.validate(side_length_1)
            if side_length_1:
                side_length_2 = input('Введите длину стороны 2: ')
                side_length_2 = self.validate(side_length_2)
                if side_length_2:
                    side_length_3 = input('Введите длину стороны 3: ')
                    side_length_3 = self.validate(side_length_2)
                    if side_length_3:
                        side_length_4 = input('Введите длину стороны 4: ')
                        side_length_4 = self.validate(side_length_4)
                        if side_length_4:
                            trapezoid = Trapezoid(
                                side_length_1=side_length_1,
                                side_length_2=side_length_2,
                                side_length_3=side_length_3,
                                side_length_4=side_length_4,
                                )
                            return self.call_method(obj=trapezoid, name=method)
        # TODO доделать
        # if figure == 5:
        #     side_length = input('Введите длину стороны: ')
        #     side_length = self.validate(side_length)
        #     if side_length:
        #         guadrate = Guadrate(side_length=side_length)
        #         return self.call_method(obj=guadrate, name=method)
        #
        # if figure == 6:
        #     side_length = input('Введите длину стороны: ')
        #     side_length = self.validate(side_length)
        #     if side_length:
        #         guadrate = Guadrate(side_length=side_length)
        #         return self.call_method(obj=guadrate, name=method)
        #
        # if figure == 7:
        #     side_length = input('Введите длину стороны: ')
        #     side_length = self.validate(side_length)
        #     if side_length:
        #         guadrate = Guadrate(side_length=side_length)
        #         return self.call_method(obj=guadrate, name=method)
        #
        # if figure == 8:
        #     side_length = input('Введите длину стороны: ')
        #     side_length = self.validate(side_length)
        #     if side_length:
        #         guadrate = Guadrate(side_length=side_length)
        #         return self.call_method(obj=guadrate, name=method)
        #
        # if figure == 9:
        #     side_length = input('Введите длину стороны: ')
        #     side_length = self.validate(side_length)
        #     if side_length:
        #         guadrate = Guadrate(side_length=side_length)
        #         return self.call_method(obj=guadrate, name=method)
        #
        # if figure == 10:
        #     side_length = input('Введите длину стороны: ')
        #     side_length = self.validate(side_length)
        #     if side_length:
        #         guadrate = Guadrate(side_length=side_length)
        #         return self.call_method(obj=guadrate, name=method)

    def run(self):
        """
        Запускает калькулятор
        """
        while True:

            figure = input(f'Выберите фигуру и введите соответствующую цифру {FigureEnum.VALUES}. '
                           f'Для выхода из программы выберите 0:')

            figure = self.validate(value=figure)
            if figure is None:
                continue
            if figure == 0:
                break

            #  TODO можно искать название класса фигуры и атрибуты,
            #   которые нужны для создания его экземпляра
            # # ищем по цифре класс фигуры
            # figure_class = FigureClassesEnum.VALUES.get(figure)

            # TODO сюда попадают родительские методы, 
            #  возможно, стоит в дочерних классах прописать 
            #  список методов наследника, 
            #  чтобы выводить только методы, переопределенные в наследнике
            method = input(f'Выберите параметр, '
                           f'который нужно рассчитать, '
                           f'и введите соответствующую цифру : '
                           f'{MethodsNamesEnums.VALUES}. ')

            # TODO сделать, чтобы пользователя
            #  отбрасывало к выбору метода, а не в самое начало
            method = self.validate(value=method)
            if method is None:
                continue
            # ищем по цифре название метода
            method = MethodsEnums.VALUES_LIST.get(method)

            result = self.input_parametrs(figure=figure, method=method)
            if result is None:
                print('Что-то пошло не так, '
                      'или расчет выбранного параметра '
                      'для выбранной фигуры еще не реализован')
                continue
            print(result)


Calc().run()
