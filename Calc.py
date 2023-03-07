from Rational import Rational
from Complex import Complex
from CheckAction import CheckAction
import Digit

class Calc(Digit):

    def calcDigit(a,b,move):
        if 'j' in a:
            a = Complex.returnComplex(a)
            b = Complex.returnComplex(b)
        else:
            a = Rational.returnRational(a)
            b = Rational.returnRational(b)
        result = CheckAction.checkAction(a,b,move)
        return result