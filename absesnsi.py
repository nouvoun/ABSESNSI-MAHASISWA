import csv
from datetime import datetime

FILENAME = 'absensi_siswa_guru.csv'

def menu():
    print("=== Program Absensi Siswa dan Guru ===")
    print("1. Tambah Absensi")
    print("2. Lihat Absensi")
    print("3. Hapus Absensi")
    print("4. Keluar")
    choice = input("Pilih menu: ")
    return choice

def tambah_absensi():
    nama = input("Masukkan nama: ")
    peran = input("Masukkan peran (Siswa/Guru): ")
    tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, peran, tanggal])
    print("Absensi berhasil ditambahkan.")

def lihat_absensi():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            print("=== Data Absensi ===")
            for row in reader:
                print(f"Nama: {row[0]}, Peran: {row[1]}, Tanggal: {row[2]}")
    except FileNotFoundError:
        print("Belum ada data absensi.")

def hapus_absensi():
    new_rows = []
    nama = input("Masukkan nama yang ingin dihapus: ")
    peran = input("Masukkan peran yang ingin dihapus (Siswa/Guru): ")
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != nama or row[1] != peran:
                    new_rows.append(row)
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
        print("Absensi berhasil dihapus.")
    except FileNotFoundError:
        print("Belum ada data absensi.")

def main():
    while True:
        choice = menu()
        if choice == '1':
            tambah_absensi()
        elif choice == '2':
            lihat_absensi()
        elif choice == '3':
            hapus_absensi()
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
