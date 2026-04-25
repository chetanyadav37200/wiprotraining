from formulamethod import FM


class square(FM):
    def __init__(self, s):
        self.side= s

    def calculate_area(self):
        return self.side * self.side

    def calculate_parameter(self):
        return 4 * self.side