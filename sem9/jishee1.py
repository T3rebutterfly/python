class hun:
    def __init__(self, ovog, ner, nas):
        self.ovog = ovog
        self.ner = ner
        self.nas = nas
    def abcd(self):
        print(self.ovog, self.ner, self.nas)

n = hun("Болд", "Золоо", 36)
n.abcd()