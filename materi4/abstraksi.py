from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Lingkaran(Bentuk):
    def __init__(self, r):
        self.r = r
        
    def luas(self):
        return 3.14 * self.r ** 2
    
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
        
    def luas(self):
        return self.sisi ** 2
    
lingkaran1 = Lingkaran(5)
persegi1 = Persegi(10)

print(lingkaran1.luas())  # output: 78.5
print(persegi1.luas())    # output: 100
