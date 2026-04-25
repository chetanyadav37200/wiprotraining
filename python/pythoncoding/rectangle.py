from formulamethod import FM


class rectangle(FM):
    def __init__(self, l,b):
        self.lenght = l
        self.breath =b

    def calculate_area(self):
        return self.lenght * self.breath

    def calculate_parameter(self):
        return 2 * self.lenght + 2 * self.breath