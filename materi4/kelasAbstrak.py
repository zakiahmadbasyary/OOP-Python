from abc import ABC, abstractmethod

class Civitas(ABC):
    @abstractmethod
    def info(self):
        pass
    
class Mahasiswa(Civitas):
    def info(self):
        print("Aku adalah Mahasiswa")
        
class Dosen(Civitas):
    def info(self):
        print("Aku adalah Dosen")
        
mahasiswa1= Mahasiswa()
mahasiswa1.info()

dosen1=Dosen()
dosen1.info()
