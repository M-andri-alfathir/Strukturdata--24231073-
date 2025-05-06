aku = {
    "nama": "M andri al fathir",}
# contoh jika 1 item
nama_dict = {
    "key": "value"
}

# contoh jika lebih dari 1 item
nama_dict = {
    "key1": "value",
    "key2": "value",
    "key3": "value"
}
# membuat dictionary
dict = {
    "nama"      : "M andri al fathir",
    "NIDN"      : 6285932677595,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@M-andri-alfathir",
        "twiter"    : '_',
        "instagram" : '-'
    }
}
# mengakses dict menggunakan key
print("Nama Saya adalah %s" % dict['nama'])
print("Akun Github saya %s" % dict['sosmed']['Github'])

# cara lainnya dengan menggunakan .get
print("NIDN Saya adalah %s" % dict.get('NIDN'))

nama_dict['kunci'] = 'Nilai_baru'
# Mengubah nilai item dictionary dict dengan key
dict['status'] = False

# Cek hasil perubahan
print(dict['status'])

# Mengubah nilai item dictionary dengan .update
dict.update({"sosmed" : {"twitter" : "@andrialfathir"}})

# cek hasil perubahan
print(dict['sosmed']['twitter'])

#menghapus item dictionary
# Menghapus menggunakan perintah del
del dict['status']

# cek hasil penghapusan data 
print(dict)

# Menghapus item menggunkan method pop()
dict.pop("sosmed")

# cek hasil penghapusan data 
print(dict)

dict.clear()

# membuat dictionary
mahasiswa = {
    "name" : "M andri al fathir"
}

# menambahkan nim
mahasiswa.update({
    "nidn" : "085932677595"
})

# melihat hasilnya
print(mahasiswa)

#Loping dictionary
# mencetak data pada dict secara berulang-ulang setiap key
for key in mahasiswa:
    print(key, mahasiswa[key])

# Atau:
for key, value in mahasiswa.items():
    print(f"{key}: {value}")