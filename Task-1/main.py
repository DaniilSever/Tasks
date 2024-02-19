"""
Создайте класс Soda (для определения типа газированной воды), 
принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).

В этом классе реализуйте метод show_my_drink(), 
выводящий на печать Газировка и {ДОБАВКА} в случае наличия добавки, 
а иначе отобразится следующая фраза: Обычная газировка.

"""


class Soda:
    def __init__(self, supplement: str = None):
        if isinstance(supplement, str):
            self.__supplement = supplement
        else:
            self.__supplement = None

    def show_my_drink(self):
        if self.__supplement is None:
            print("Обычная газировка")
        else:
            print(f"Газировка с добавкой '{self.__supplement}'")


if __name__ == "__main__":
    # 1) Обычная Газировка
    drink = Soda()
    drink.show_my_drink()
    # 2) Газировка с добавкой
    drink = Soda("Кокосовое молоко")
    drink.show_my_drink()

# OUTPUT
"""
1) Обычная газировка
2) Газировка с добавкой 'Кокосовое молоко'
"""
