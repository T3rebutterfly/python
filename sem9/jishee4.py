class hun:
    def __init__(self, ovog, ner, nas, elssenjil):
        self.ovog = ovog
        self.ner = ner
        self.nas = nas
        self.elssenjil = elssenjil
    def abcd(self):
        print(self.ovog, self.ner, self.nas, self.elssenjil)
class Oyutan(hun):
    def __init__(self, ovog, ner, nas, elssenjil):
        super().__init__(ovog, ner, nas, elssenjil)
n = Oyutan("Болд", "Золоо", 36, 2021)
n.abcd()