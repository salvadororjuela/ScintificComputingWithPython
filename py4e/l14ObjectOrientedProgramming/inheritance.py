from wsgiref.validate import PartialIteratorWrapper
from multipleInstances import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Josua")
j.party()
j.six()
print(dir(j))