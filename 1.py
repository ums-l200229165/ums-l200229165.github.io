from metaflow import FlowSpec, step

class ProsesPerkuliahanFlow(FlowSpec):

    @step
    def start(self):
        """Mulai proses perkuliahan"""
        self.nama = "Reza"
        self.npm = "123456789"
        self.spp_terbayar = False
        self.mata_kuliah = ["Pemrograman", "Matematika Diskrit", "Basis Data"]
        print(f"Mahasiswa {self.nama} memulai proses perkuliahan.")
        self.next(self.bayar_spp)

    @step
    def bayar_spp(self):
        """Bayar SPP"""
        self.spp_terbayar = True
        print(f"{self.nama} telah membayar SPP.")
        self.next(self.ikuti_perkuliahan)

    @step
    def ikuti_perkuliahan(self):
        """Mengikuti perkuliahan dan ujian"""
        if self.spp_terbayar:
            print(f"{self.nama} mengikuti perkuliahan untuk: {', '.join(self.mata_kuliah)}")
            self.nilai_akhir = {mk: nilai for mk, nilai in zip(self.mata_kuliah, [85, 78, 90])}
            
        else:
            print("SPP belum dibayar.")
            self.next(self.end)
        self.next(self.lihat_nilai_akhir)

    @step
    def lihat_nilai_akhir(self):
        """Menampilkan nilai akhir"""
        print(f"Nilai akhir {self.nama}:")
        for mk, nilai in self.nilai_akhir.items():
            print(f"{mk}: {nilai}")
        self.next(self.end)

    @step
    def end(self):
        """Akhir dari alur perkuliahan"""
        print("Proses perkuliahan selesai.")

if __name__ == "__main__":
    ProsesPerkuliahanFlow()