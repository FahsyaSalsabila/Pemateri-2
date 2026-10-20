"""
Simulasi Risiko Banjir Sederhana
Proyek pembelajaran berdasarkan materi HPC untuk menyelesaikan tantangan lokal.
Catatan: ambang risiko di bawah hanya contoh simulasi, bukan standar resmi.
"""

def klasifikasi_risiko(curah_hujan, tinggi_air):
    """Mengembalikan kategori risiko berdasarkan aturan simulasi."""
    if curah_hujan < 0 or tinggi_air < 0:
        raise ValueError("Nilai tidak boleh negatif.")

    # Aturan demonstrasi, perlu divalidasi sebelum penggunaan nyata.
    if curah_hujan >= 100 or tinggi_air >= 150:
        return "TINGGI", "Waspada. Pantau informasi resmi dan ikuti arahan petugas."
    elif curah_hujan >= 50 or tinggi_air >= 80:
        return "SEDANG", "Tetap waspada dan pantau perubahan hujan serta tinggi air."
    else:
        return "RENDAH", "Tetap pantau kondisi lingkungan dan informasi resmi."


def minta_angka(pesan):
    """Meminta input angka yang valid dari pengguna."""
    while True:
        try:
            nilai = float(input(pesan))
            if nilai < 0:
                print("Masukkan angka nol atau lebih.")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid. Masukkan angka, misalnya 45 atau 72.5.")


def main():
    print("=" * 48)
    print(" SIMULASI RISIKO BANJIR - WILAYAH BENGKULU")
    print("=" * 48)
    print("Masukkan data simulasi lingkungan.")
    print("Catatan: hasil bukan peringatan banjir resmi.\n")

    wilayah = input("Nama wilayah: ").strip() or "Wilayah tidak disebutkan"
    curah_hujan = minta_angka("Curah hujan (mm): ")
    tinggi_air = minta_angka("Tinggi air (cm): ")

    kategori, saran = klasifikasi_risiko(curah_hujan, tinggi_air)

    print("\n--- HASIL SIMULASI ---")
    print(f"Wilayah       : {wilayah}")
    print(f"Curah hujan   : {curah_hujan:.1f} mm")
    print(f"Tinggi air    : {tinggi_air:.1f} cm")
    print(f"Kategori risiko: {kategori}")
    print(f"Saran         : {saran}")
    print("\nGunakan data resmi dan arahan instansi terkait untuk keputusan nyata.")


if __name__ == "__main__":
    main()
