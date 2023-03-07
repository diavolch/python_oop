from View import View
from Calc import Calc

class Presenter:
    def click():
        a,b,move = View.get_data()
        result = str(Calc.calcDigit(a,b,move))
        View.returnResult(result)