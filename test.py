class distance:

    def __init__(self,waarde_meter):
        self.waarde_meter = waarde_meter

    @staticmethod
    def meter(self, value):
        return value

    @staticmethod
    def milimeter(self, value):
        return value *1000

    @staticmethod
    def miles(self, value):
        return value / 1600

print(distance.miles(800))
print(distance.miles(700))