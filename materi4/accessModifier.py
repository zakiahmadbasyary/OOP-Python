#public
class Mahasiswa:
    def __init__(self,nama,npm):
        self.nama=nama
        self.npm=npm
    
    def info(self):
        print(f"Nama: {self.nama}, NPM: {self.npm}")
    

#protected
class Dosen:
    def __init__(self,nama,nip) :
        self._nama=nama
        self._nip=nip
    
    def info(self):
        print(f"Nama Dosen: {self._nama}, NIP: {self._nip}")


#Private
class Matakuliah:
    def __init__(self, nama, kode) :
        self.__nama=nama
        self.__kode=kode
    
    def info(self):
        print(f"Nama Matakuliah: {self.__nama}, Kode: {self.__kode}")

mahasiswa1=Mahasiswa("zaki","2215061004")
print(mahasiswa1.nama)
mahasiswa1.info()

dosen1= Dosen("Rio", "193430434024")
print(dosen1._nama)
dosen1.info()

mataKuliah1=Matakuliah("Logika", "inf2432423")
print(mataKuliah1.__nama)
mataKuliah1.info()