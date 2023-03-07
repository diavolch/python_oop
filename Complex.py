from Logger import Logger
from Digit import Digit

class Complex():
    def returnComplex(a) :
        a = complex(a.replace(' ', ''))
        Logger.logger(f"Комплексное число: {a} создано")
        return a
    