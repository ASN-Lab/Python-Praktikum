print("<--------------------------------------------------- Week 13-Python Python Classes & Objects ---------------------------------------------------->")
print("""
Class dan Object di Python:

Dalam pemrograman Python, class dan object adalah konsep dasar dalam pemrograman berorientasi objek (OOP). Berikut adalah penjelasan singkat tentang class dan object di Python:

Class:
- Class adalah blueprint atau cetakan untuk membuat object.
- Class dapat diibaratkan sebagai sebuah rencana atau desain untuk membuat object.
- Class dapat memiliki atribut (data) dan metode (fungsi).

Object:
- Object adalah instance dari sebuah class.
- Object memiliki atribut dan metode yang sama dengan class-nya.
- Object dapat memiliki nilai atribut yang berbeda dengan object lainnya.

Contoh:
class Mobil:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        print(f"Merk: {self.merk}, Tahun: {self.tahun}")

mobil1 = Mobil("Toyota", 2020)
mobil2 = Mobil("Honda", 2019)

mobil1.info()
mobil2.info()

Dalam contoh di atas, Mobil adalah class dan mobil1 serta mobil2 adalah object dari class Mobil.
""")

# Weekly Exercise
print("<---------------------------------------------------------------- Weekly Exercise --------------------------------------------------------------->")
print("Exercise 1" + "\n" + "Membuat Class dan Object pada sebuah kasus di dunia nyata:" + "\n")

print("Kasus:" + "\n\n" + """Seorang penjual alat tulis menjual 10 bolpoint, 10 pensil dan 10 penghapus. 1 biji bolpoint harganya Rp. 2000, 1 biji pensil harganya Rp. 1.000 dan 1 penghapus harganya Rp. 500.""" + "\n")

class AlatTulis:
    def __init__(self, nama, stok, harga_satuan):
        self.nama = nama
        self.stok = stok
        self.harga_satuan = harga_satuan
        self.harga = self.stok * self.harga_satuan
        self.total_harga = 0

    # Setter
    def set_nama(self, nama):
        self.nama = nama

    def set_stok(self, stok):
        self.stok = stok
        self.harga = self.stok * self.harga_satuan

    def set_harga_satuan(self, harga_satuan):
        self.harga_satuan = harga_satuan
        self.harga = self.stok * self.harga_satuan

    def set_total_harga(self, total_harga):
        self.total_harga = total_harga

    # Getter
    def get_nama(self):
        return self.nama

    def get_stok(self):
        return self.stok

    def get_harga_satuan(self):
        return self.harga_satuan

    def get_harga(self):
        return self.harga

    def get_total_harga(self):
        return self.total_harga

    # Setter Getter
    def set_get_nama(self, nama=None):
        if nama is not None:
            self.nama = nama
        return self.nama

    def set_get_stok(self, stok=None):
        if stok is not None:
            self.stok = stok
            self.harga = self.stok * self.harga_satuan
        return self.stok

    def set_get_harga_satuan(self, harga_satuan=None):
        if harga_satuan is not None:
            self.harga_satuan = harga_satuan
            self.harga = self.stok * self.harga_satuan
        return self.harga_satuan

    def set_get_harga(self, harga=None):
        if harga is not None:
            self.harga = harga
        return self.harga

    def set_get_total_harga(self, total_harga=None):
        if total_harga is not None:
            self.total_harga = total_harga
        return self.total_harga

    def tampilkan_hasil(self):
        print(f"Nama         : {self.nama}")
        print(f"Stok         : {self.stok}")
        print(f"Harga Satuan : Rp. {self.harga_satuan}")
        print(f"Harga        : Rp. {self.harga}")
        print(f"Total Harga  : Rp. {self.total_harga}" + "\n")

bolpoint = AlatTulis("Bolpoint", 10, 2000)
pensil = AlatTulis("Pensil", 10, 1000)
penghapus = AlatTulis("Penghapus", 10, 500)

print("Class:")
print("""
class AlatTulis:
    def __init__(self, nama, stok, harga_satuan):
        self.nama = nama
        self.stok = stok
        self.harga_satuan = harga_satuan
        self.harga = self.stok * self.harga_satuan
        self.total_harga = 0
""")

print("1. Method untuk memasukkan (Setter) nama, stok, harga satuan, dan harga:")
print("""
    def set_nama(self, nama):
        self.nama = nama

    def set_stok(self, stok):
        self.stok = stok
        self.harga = self.stok * self.harga_satuan

    def set_harga_satuan(self, harga_satuan):
        self.harga_satuan = harga_satuan
        self.harga = self.stok * self.harga_satuan

    def set_total_harga(self, total_harga):
        self.total_harga = total_harga
""")
print("Output Setter:")
bolpoint.tampilkan_hasil()

print("2. Method untuk menampilkan (Getter) nama, stok, harga satuan, dan harga:")
print("""
    def get_nama(self):
        return self.nama

    def get_stok(self):
        return self.stok

    def get_harga_satuan(self):
        return self.harga_satuan

    def get_harga(self):
        return self.harga

    def get_total_harga(self):
        return self.total_harga
""")
print("Output Getter:")
pensil.tampilkan_hasil()

print("3. Method total harga (Setter, Getter) untuk mengeloloa transaksi penjualan:")
print("""
def set_get_nama(self, nama=None):
        if nama is not None:
            self.nama = nama
        return self.nama

    def set_get_stok(self, stok=None):
        if stok is not None:
            self.stok = stok
            self.harga = self.stok * self.harga_satuan
        return self.stok

    def set_get_harga_satuan(self, harga_satuan=None):
        if harga_satuan is not None:
            self.harga_satuan = harga_satuan
            self.harga = self.stok * self.harga_satuan
        return self.harga_satuan

    def set_get_harga(self, harga=None):
        if harga is not None:
            self.harga = harga
        return self.harga

    def set_get_total_harga(self, total_harga=None):
        if total_harga is not None:
            self.total_harga = total_harga
        return self.total_harga

    def tampilkan_hasil(self):
        print(f"Nama         : {self.nama}")
        print(f"Stok         : {self.stok}")
        print(f"Harga Satuan : Rp. {self.harga_satuan}")
        print(f"Harga        : Rp. {self.harga}")
        print(f"Total Harga  : Rp. {self.total_harga}" + "\n")

bolpoint = AlatTulis("Bolpoint", 10, 2000)
pensil = AlatTulis("Pensil", 10, 1000)
penghapus = AlatTulis("Penghapus", 10, 500)
""")
print("Output Setter, Getter:")
penghapus.tampilkan_hasil()