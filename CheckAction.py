from Logger import Logger

class CheckAction:
    def checkAction(a,b,move):
        if move == '+':
            result = a + b
        elif move == '-':
            result = a - b
        elif move == '*':
            result = a * b
        elif move == '/':
            result = a / b
        Logger.logger(f"Результат дейтсвия: {result}")
        return result