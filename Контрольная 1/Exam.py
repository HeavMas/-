#Билет - 4
class PcheloSlon():
    def __init__(self, Pchelo, slon):
        self.Pchelo = Pchelo
        self.slon = slon
    def fly(self):
        if self.Pchelo >= self.slon:
            return True
        else:
            return False
    def trumpet(self):
        if self.slon >= self.Pchelo:
            return 'tu-tu-doo-doo'
        else:
            return 'wzzzzzzzzzzz'
    def eat(self, meal, value):
        if meal == 'nectar' and (self.slon - value > 0) and (self.slon < 100 and self.slon + value < 100):
            self.slon -= value
            print(f"Часть слона была уменьшена на {value} едениц")
            self.Pchelo += value
            print(f"Часть пчелы была увеличина на {value} едениц")
        else:
            print('Неполучилось добавить пчелу')
        if meal == 'grass' and (self.Pchelo - value > 0) and (self.Pchelo + value < 100):
            self.Pchelo -= value
            print(f"Часть пчелы была уменьшена на {value} едениц")
            self.slon += value
            print(f"Часть слона была увеличина на {value} едениц")
        else:
            print('Неполучилось добавить слона')
    def get_parts(self):
        print(f"Часть пчелы:{self.Pchelo} , Часть слона: {self.slon}")

FirstPS = PcheloSlon(60, 40)
print(FirstPS.fly())
print(FirstPS.trumpet())
FirstPS.eat('nectar', 10)
FirstPS.get_parts()
FirstPS.eat('grass', 25)
FirstPS.get_parts()