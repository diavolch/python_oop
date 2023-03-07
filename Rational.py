from fractions import Fraction
from Logger import Logger

class Rational:
    def returnRational(a) :
        a = Fraction(a.replace(' ', ''))
        Logger.logger(f"Рациональное число: {a} создано")
        return a