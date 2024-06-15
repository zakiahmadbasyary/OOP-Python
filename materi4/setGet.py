class Mahasiwa:
    def __init__(self, nama, npm):
        self.__nama = nama
        self.__npm = npm
        
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama= nama
        
    def get_npm(self):
        return self.__npm
    
    def set_npm(self, npm):
        self.__npm= npm
        
mahasiswa1=Mahasiwa("zaki", "2215061004")
print(mahasiswa1.get_nama())
mahasiswa1.set_nama("Zaki Ahmad Basyary")
print(mahasiswa1.get_nama())
print(mahasiswa1.get_npm())
mahasiswa1.set_nama("2215061001")
print(mahasiswa1.get_npm())