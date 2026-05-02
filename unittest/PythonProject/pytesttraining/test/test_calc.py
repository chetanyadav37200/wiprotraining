from src.calculation import Calculation


class TestCalc:
    calc=Calculation()

    def test_area_of_square(self):
        res=self.calc.are_of_square(10)
        assert res==100 ,'Are is wrong'

    def test_parameter_of_rec(self):
        res=self.calc.parameter_of_rec(10,5)
        assert res==30 ,'parameter is wrong'
