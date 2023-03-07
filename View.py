from Logger import Logger

class View:
    def get_data():
        a = input('Введите первое число: ')
        Logger.logger(f"Число: {a} введено")
        b = input('Введите второе число: ')
        Logger.logger(f"Число: {b} введено")
        move = input('Введите необходимое действие над числами(/,*,+,-): ')
        Logger.logger(f"Выбрано действие: {move}")
        return a, b, move
    def returnResult(result):
        print("Результат: " + result)