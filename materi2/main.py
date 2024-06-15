class Animal:
    nama =""
    jenis =""
    pemilik=""

    def __init__(self, nama, jenis) :
        self.nama=nama
        self.jenis=jenis
    
    def __del__(self):
        print(f"{self.nama}  {self.jenis} dihapus")
    
    def perintah(self, perintah):
        print(f"{self.nama} lakukan {perintah}")
    
    def setPemilik(self, pemilik):
        self.pemilik=pemilik

animal1= Animal("Kucing", "mamalia")
animal1.perintah("duduk")
animal1.setPemilik("zaki")
print(f"{animal1.nama} ini dimiliki oleh {animal1.pemilik} ")
