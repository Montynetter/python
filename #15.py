class Soda:
    def __init__(self, addition):
        if isinstance(addition, str):
            self.addition = addition
        else:
            self.addition = None

    def show_my_drink(self):
        if self.addition:
            print(f'Газировка и {self.addition}')
        else:
            print('Обычная газировка')


can1 = Soda('ваниль')
can2 = Soda('')
can1.show_my_drink()
can2.show_my_drink()

