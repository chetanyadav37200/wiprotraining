class college:
    def __init__(self,ccode,cnsme,ccity):
        self._coolcode=ccode
        self._collname=cnsme
        self._collcity=ccity

    def welcomr_msg(self):
        print("Welcome To the College")

    def display_college_detail(self):
        print(f"college code: {self._coolcode} \ncollege name {self._collname} \ncollege city {self._collcity}")
