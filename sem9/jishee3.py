class hun:
    def __init__(self, ovog, ner, nas):
        self.ovog = ovog
        self.ner = ner
        self.nas = nas
    def abcd(self):
        print(self.ovog, self.ner, self.nas)
class Oyutan(hun):
    def __init__(self, ovog, ner, nas):
        super().__init__(ovog, ner, nas)
n = Oyutan("Болд", "Золоо", 36)
n.abcd()