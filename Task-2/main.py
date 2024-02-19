"""
Николаю требуется проверить,
возможно ли из представленных отрезков условной длины сформировать треугольник. 
Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– Ура, можно построить треугольник!;
– С отрицательными числами ничего не выйдет!;
– Нужно вводить только числа!;
– Жаль, но из этого треугольник не сделать.
"""


class TriangleChecker:
    def __init__(self, first_value: int, second_value: int, third_value: int):
        self.__first_rib = first_value
        self.__second_rib = second_value
        self.__third_rib = third_value
    

    def is_triangle(self):
        if (
            isinstance(self.__first_rib, int)
            and isinstance(self.__second_rib, int)
            and isinstance(self.__third_rib, int)
        ):
            if self.__first_rib > 0 and self.__second_rib > 0 and self.__third_rib > 0:
                max_rib = max(self.__first_rib, self.__second_rib, self.__third_rib)
                match max_rib:
                    case self.__first_rib:
                        res = self.__second_rib + self.__third_rib
                        if res > max_rib:
                            print("Ура, можно построить треугольник!")
                        else:
                            print("Жаль, но из этого треугольник не сделать")

                    case self.__second_rib:
                        res = self.__first_rib + self.__third_rib
                        if res > max_rib:
                            print("Ура, можно построить треугольник!")
                        else:
                            print("Жаль, но из этого треугольник не сделать")

                    case self.__third_rib:
                        res = self.__first_rib + self.__second_rib
                        if res > max_rib:
                            print("Ура, можно построить треугольник!")
                        else:
                            print("Жаль, но из этого треугольник не сделать")
            else:
                print("С отрицательными числами ничего не выйдет!")
        else:
            print("Нужно вводить только числа!")


if __name__ == "__main__":
    # 1) Можно построить
    triangle = TriangleChecker(60, 30, 80)
    triangle.is_triangle()
    # 2) Нельзя построить
    triangle = TriangleChecker(10, 90, 80)
    triangle.is_triangle()
    # 3) Отрицательные числа
    triangle = TriangleChecker(60, -30, 80)
    triangle.is_triangle()
    # 4) Не правильный тип данных
    triangle = TriangleChecker(60, "Hello", 80)
    triangle.is_triangle()

# OUTPUT
"""
1) Ура, можно построить треугольник!
2) Жаль, но из этого треугольник не сделать
3) С отрицательными числами ничего не выйдет!
4) Нужно вводить только числа!
"""
