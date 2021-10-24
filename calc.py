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

        def name_method():
            return 'Периметр'

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


class Guadrate(Figure):
    """
    Класс квадрата
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.GUADRATE
    )


class Rectangle(Figure):
    """
    Класс прямоугольника
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.RECTANGLE
    )


class Trapezoid(Figure):
    """
    Класс трапеции
    """
    title = FigureEnum.VALUES.get(
        FigureEnum.TRAPEZOID
    )


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

    {
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
    VALUES = {
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

    @staticmethod
    def list_methods(some_class):
        """
        Получает список методов класса
        """
        method_list = []
        for attribute in dir(some_class):
            attribute_value = getattr(some_class, attribute)
            if callable(attribute_value):
                if not attribute.startswith('__'):
                    method_list.append(attribute)

        return method_list

    def run(self):
        """
        Запускает калькулятор
        """
        # list_title_figure = {k: v for k, v in FigureEnum.__dict__.items() if not k.startswith('__')}

        while True:

            figure = input(f'Выберите фигуру и введите соответствующую цифру {FigureEnum.VALUES}. '
                           f'Для выхода из программы выберите 0:')
            try:
                figure = int(figure)
            except TypeError:
                print('Вы ввели неверное значение, попробуйте еще')
                continue

            if figure == 0:
                break

            # ищем по цифре класс фигуры

            figure_class = FigureClassesEnum.VALUES.get(figure)
            methods = self.list_methods(figure_class)
            for method in methods:
                print(method)
            return methods


Calc().run()
