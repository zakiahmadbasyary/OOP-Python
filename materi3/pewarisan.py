class Civitas:
    nama =""
    jurusan =""

    def __init__(self, nama, id) :
        self.nama=nama
        self.id=id

    def info(self):
        print(f" nama:\t\t {self.nama} \n jurusan: \t {self.id}")

class Mahasiswa (Civitas):
    npm=""
    semester=""

    def __init__(self, nama, id,npm, semester):
        super().__init__(nama, id)
        self.npm=npm
        self.semester=semester
    
    def info(self):
        super().info()
        print(f"NPM:\t{self.npm} \nsemester:\t {self.semester} \n")
    
class Dosen(Civitas):
    nip=""
    matkul=""

    def __init__(self, nama, id, nip, matkul):
        super().__init__(nama, id)
        self.nip=nip
        self.matkul=matkul
    
    def info(self):
        super().info()
        print(f"NIP:\t{self.nip} \n Matkul:\t {self.matkul}\n")



# superclass
civitas1 =Civitas("joko","teknik informatika")
civitas1.info();

# subclass mahasiswa
mahasiswa1= Mahasiswa("zaki", "teknik elektro","2215061004", 4)
mahasiswa1.info()

# subclass dosen
dosen1= Dosen("rio", "teknik iformatika","2215061084", 4)
dosen1.info()
