import pytest
from src.calculation import Calculation

class TestCalculation:
    calc = Calculation()


    @pytest.mark.parametrize("n1,n2,ex",[(5,5,10),(-5,-5,-10),(0,5,5)])

    def test_add(self,n1,n2,ex):
        res = self.calc.add(n1,n2)
        assert res == ex,'Addition Error'
    @pytest.mark.parametrize("n1,n2,ex",[(5,5,0),(-5,-5,0),(0,5,-5)])

    def test_sub(self,n1,n2,ex):
        res = self.calc.sub(n1,n2)
        assert res == ex, 'Subtraction Error'

    def test_mul(self):
        res = self.calc.mul(10, 5)
        assert res == 50, 'Multiplication Error'

    def test_div(self):
        res = self.calc.div(10, 5)
        assert res == 2, 'Division Error'
    @pytest.mark.skip
    def test_ne(self):
        assert self.calc.ne(10, 10) == True, 'Different numbers should return True'

    @pytest.mark.xfail(reason="Exception not handle there")
    def test_div1(self):
        #with pytest.raises(ZeroDivisionError):
        res=self.calc.div(0, 10)
        assert res== 0

