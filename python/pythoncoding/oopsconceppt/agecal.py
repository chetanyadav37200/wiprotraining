from oopsconceppt.myegeexceptio import AgeExeption


class AgeCalculation:
    def voting_age_check(selfself,age):
        if age<18:
            raise AgeExeption('Not Eligible to vote...')
        else:
            return True

    def pansion_age_check(selfself, age):
        if age < 60:
            raise AgeExeption('Not Eligible to get pansion...')
        else:
            return True