# Class Mahasiswa (Encapsulation)
class mahasiswa(object):

    def __init__(self, input_nama, input_npm, input_fakultas='Tidak Diketahui', input_jurusan='Tidak Diketahui'):
        self.nama = input_nama
        self.npm = input_npm
        self.fakultas = input_fakultas
        self.jurusan = input_jurusan
    
    def info_mahasiswa(self):
        print(f'Nama\t\t: {self.nama}\nNPM\t\t: {self.npm}\nFakultas\t: {self.fakultas}\nJurusan\t\t: {self.jurusan}\n')

    def ganti_nama(self, nama_baru):
        self.nama = nama_baru
        print('-'*5,'Nama Berhasil Diganti','-'*5,'\n')


# Inhertitence
class mahasiswa_2(object):

    def __init__(self, input_nama, input_npm):
        self.nama = input_nama
        self.npm = input_npm

class fakultas(mahasiswa_2):

    fakultas_saat_ini = ''

    def __init__(self, input_nama, input_npm, input_fakultas='Tidak Diketahui'):
        super().__init__(input_nama, input_npm)
        self.fakultas = input_fakultas
        fakultas_saat_ini = input_fakultas
    
    def pindah_fakultas(self, input_fakultas=fakultas_saat_ini):
        self.fakultas = input_fakultas
    
    def info_mahasiswa(self):
        print(f'Nama\t\t: {self.nama}\nNPM\t\t: {self.npm}\nFakultas\t: {self.fakultas}')


# Abstraction
from abc import abstractmethod, ABC
class Alat_Elektronik(ABC):

    @abstractmethod
    def identitas(self, input_nama, asal_negara='Tidak Diketahui'):
        pass
    def kegunaan(self, input_guna):
        pass
    def kelistrikan(self, voltase='-', ampere='-'):
        pass
    def info(self):
        pass

# Polymorphism
class Elektronik(object):
    def __init__(self, nama, asal='-', kode='-', volt='-', ampere='-'):
        self.nama = nama
        self.asal = asal
        self.kode = kode
        self.volt = volt
        self.ampere = ampere
    
    def info(self):
        print(f'Nama\t\t: {self.nama}\nAsal\t\t: {self.asal}\nKode\t\t: {self.kode}\nVoltase\t\t: {self.volt}\nAmpere\t\t: {self.ampere}')