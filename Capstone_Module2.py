membership_list = [
    {
        "nama": "Basic",
        "harga_bulanan": 200000
    },
    {
        "nama": "Premium",
        "harga_bulanan": 350000
    },
    {
        "nama": "VIP",
        "harga_bulanan": 500000
    }
]

members = [
    {
        "id_member": "M001",
        "nama": "Andi Saputra",
        "jenis_kelamin": "Laki-laki",
        "No Handphone": "081234567801",
        "alamat": "Tebet",
        "membership": "BASIC",
        "durasi": 1,
        "harga": 200000
    },
    {
        "id_member": "M002",
        "nama": "Budi Santoso",
        "jenis_kelamin": "Laki-laki",
        "No Handphone": "081234567802",
        "alamat": "Pancoran",
        "membership": "PREMIUM",
        "durasi": 6,
        "harga": 2100000
    },
    {
        "id_member": "M003",
        "nama": "Siti Aminah",
        "jenis_kelamin": "Perempuan",
        "No Handphone": "081234567803",
        "alamat": "Kuningan",
        "membership": "VIP",
        "durasi": 12,
        "harga": 6000000
    },
    {
        "id_member": "M004",
        "nama": "Rizky Pratama",
        "jenis_kelamin": "Laki-laki",
        "No Handphone": "081234567804",
        "alamat": "Manggarai",
        "membership": "BASIC",
        "durasi": 3,
        "harga": 600000
    },
    {
        "id_member": "M005",
        "nama": "Dinda Lestari",
        "jenis_kelamin": "Perempuan",
        "No Handphone": "081234567805",
        "alamat": "Cilandak",
        "membership": "PREMIUM",
        "durasi": 3,
        "harga": 1050000
    },
    {
        "id_member": "M006",
        "nama": "Fajar Ramadhan",
        "jenis_kelamin": "Laki-laki",
        "No Handphone": "081234567806",
        "alamat": "Pasar Minggu",
        "membership": "VIP",
        "durasi": 6,
        "harga": 3000000
    },
    {
        "id_member": "M007",
        "nama": "Ayu Permatasari",
        "jenis_kelamin": "Perempuan",
        "No Handphone": "081234567807",
        "alamat": "Depok",
        "membership": "BASIC",
        "durasi": 6,
        "harga": 1200000
    },
    {
        "id_member": "M008",
        "nama": "Dimas Wijaya",
        "jenis_kelamin": "Laki-laki",
        "No Handphone": "081234567808",
        "alamat": "Bekasi",
        "membership": "PREMIUM",
        "durasi": 12,
        "harga": 4200000
    },
    {
        "id_member": "M009",
        "nama": "Nadia Putri",
        "jenis_kelamin": "Perempuan",
        "No Handphone": "081234567809",
        "alamat": "Kemang",
        "membership": "VIP",
        "durasi": 3,
        "harga": 1500000
    },
    {
        "id_member": "M010",
        "nama": "Arif Hidayat",
        "jenis_kelamin": "Laki-laki",
        "No Handphone": "081234567810",
        "alamat": "Bintaro",
        "membership": "BASIC",
        "durasi": 12,
        "harga": 2400000
    },
    {
        "id_member": "M011",
        "nama": "Maya Sari",
        "jenis_kelamin": "Perempuan",
        "No Handphone": "081234567811",
        "alamat": "Cipete",
        "membership": "PREMIUM",
        "durasi": 1,
        "harga": 350000
    },
    {
        "id_member": "M012",
        "nama": "Yoga Pranata",
        "jenis_kelamin": "Laki-laki",
        "No Handphone": "081234567812",
        "alamat": "Rawamangun",
        "membership": "VIP",
        "durasi": 12,
        "harga": 6000000
    },
]

def menu_utama():
    menu_member = int(input('''
    ========================================
    |         MEMBER GYM MANAGEMENT        |
    ========================================
    |                                      |
    |    1. Data Member                    |
    |    2. Tambah Member                  |
    |    3. Update Member                  |
    |    4. Filter Member                  |
    |    5. Sorting Member                 |
    |    6. Hapus Member                   |
    |    7. Keluar                         |
    |                                      |
    ========================================
    Pilih Menu: '''))
    return menu_member
    

def menu_data_member():
    menu_report = int(input('''
    ================================================
    |                  DATA MEMBER                 |
    ================================================
    |                                              |
    |    1. Lihat Semua Member                     |
    |    2. Cari Member Berdasarkan ID             |
    |    3. Cari Member Berdasarkan Nama           |
    |    4. Cari Member Berdasarkan No. Handphone  |
    |    5. Kembali                                |
    |                                              |      
    ================================================
    Pilih Menu : '''))
    return menu_report

def display_member():
    for member in members:
        print(f"""
    ID Member       : {member["id_member"]}
    Nama            : {member["nama"]}
    Jenis Kelamin   : {member["jenis_kelamin"]}
    No. Handphone   : {member["No Handphone"]}
    Alamat          : {member["alamat"]}
    Membership      : {member["membership"]}
    Durasi          : {member["durasi"]} Bulan
    Harga           : Rp.{member["harga"]:,}
    --------------------------------------------
    """)
    print(f'''
    -> Total Member : {len(members)}
    ---------------------''')

def display_cari_member(member):
    print(f"""
    ID Member       : {member["id_member"]}
    Nama            : {member["nama"]}
    Jenis Kelamin   : {member["jenis_kelamin"]}
    No. Handphone   : {member["No Handphone"]}
    Alamat          : {member["alamat"]}
    Membership      : {member["membership"]}
    Durasi          : {member["durasi"]} Bulan
    Harga           : Rp.{member["harga"]:,}
    --------------------------------------------
    """)

def display_menu_tambah():
    menu_tambah = int(input('''
    ========================================
    |            TAMBAH MEMBER             |
    ========================================
    |                                      |
    |    1. Isi Data Member                |
    |    2. Kembali                        |
    |                                      |
    ========================================
    Pilih Menu: '''))
    return menu_tambah

def display_membership(): 
    print(f'''
    ========================================
    |              MEMBERSHIP              |
    ========================================

     - {membership_list[0]["nama"]}\t = Rp.{membership_list[0]["harga_bulanan"]:,}/Bulan
     - {membership_list[1]["nama"]}\t = Rp.{membership_list[1]["harga_bulanan"]:,}/Bulan
     - {membership_list[2]["nama"]}\t = Rp.{membership_list[2]["harga_bulanan"]:,}/Bulan
                
    ========================================''')

def display_menu_update():
    menu_update = int(input('''
    ========================================
    |             UPDATE MEMBER            |
    ========================================
    |                                      |
    |    1. Ubah Data Member               |
    |    2. Kembali                        |
    |                                      |
    ========================================
    Pilih Menu: '''))
    return menu_update

def display_menu_konfirmasi():
    menu_konfirmasi = int(input('''
    Apakah Mau lanjut update data ? 
    
    1. Iya
    2. Tidak
    
    Pilih Angka Menu (1 atau 2) : '''))
    return menu_konfirmasi

def display_updated_data(member):                             
    print(f"""
    ==== Data Berhasil Diupdate ====

    ID Member       : {member["id_member"]}
    Nama            : {member["nama"]}
    Jenis Kelamin   : {member["jenis_kelamin"]}
    No. Handphone   : {member["No Handphone"]}
    Alamat          : {member["alamat"]}
    Membership      : {member["membership"]}
    Durasi          : {member["durasi"]} Bulan
    Harga           : Rp.{member["harga"]:,}

    --------------------------------------------
    """)

def display_menu_filter():
    menu_filter = int(input('''
    ========================================
    |            FILTER MEMBER             |
    ========================================

    1. Filter berdasarkan Membership
    2. Filter berdasarkan Jenis Kelamin
    3. Filter berdasarkan Durasi
    4. Filter berdasarkan Harga
    5. Kembali

    ========================================
    Pilih Menu : '''))
    return menu_filter

def display_membership_filter(member):
    print(f"""
    ID Member       : {member["id_member"]}
    Nama            : {member["nama"]}
    Jenis Kelamin   : {member["jenis_kelamin"]}
    No. Handphone   : {member["No Handphone"]}
    Alamat          : {member["alamat"]}
    Membership      : {member["membership"]}
    Durasi          : {member["durasi"]} Bulan
    Harga           : Rp.{member["harga"]:,}
    --------------------------------------------
    """)

def display_menu_sorting():
    menu_sorting = int(input('''
    ========================================
    |            SORTING MEMBER            |
    ========================================
    |                                      |
    |   1. Nama A - Z                      |
    |   2. Nama Z - A                      |
    |   3. Harga Terendah - Tertinggi      |
    |   4. Harga Tertinggi - Terendah      |
    |   5. Durasi Terpendek - Terpanjang   |
    |   6. Durasi Terpanjang - Terpendek   |
    |   7. Kembali                         |
    |                                      |
    ========================================
    Pilih Menu (1-7): '''))
    return menu_sorting

def display_hasil_sorted(hasil_sorted):
    for member in hasil_sorted:
        print(f"""
    ID Member       : {member["id_member"]}
    Nama            : {member["nama"]}
    Jenis Kelamin   : {member["jenis_kelamin"]}
    No. Handphone   : {member["No Handphone"]}
    Alamat          : {member["alamat"]}
    Membership      : {member["membership"]}
    Durasi          : {member["durasi"]} Bulan
    Harga           : Rp.{member["harga"]:,}
    --------------------------------------------
    """)   

def sudah_sortir(data_collection, kolom, kebalik=False):
    hasil_sorted = data_collection.copy()
    hasil_sorted.sort(key = lambda x:x [kolom],reverse = kebalik)
    display_hasil_sorted(hasil_sorted)

def display_menu_hapus():
    menu_hapus = int(input('''
    ========================================
    |             DELETE MEMBER            |
    ========================================
    |                                      |
    |    1. Hapus Data Member              |
    |    2. Kembali                        |
    |                                      |
    ========================================
    Pilih Angka Menu (1 atau 2) : '''))
    return menu_hapus   

def display_hapus_member(member):
                    
    print(f"""
    ========= Data Yang Akan Dihapus =========
    ID Member       : {member["id_member"]}
    Nama            : {member["nama"]}
    Jenis Kelamin   : {member["jenis_kelamin"]}
    No. Handphone   : {member["No Handphone"]}
    Alamat          : {member["alamat"]}
    Membership      : {member["membership"]}
    Durasi          : {member["durasi"]} Bulan
    Harga           : Rp.{member["harga"]:,}
    --------------------------------------------
    """)     

while True:

    menu_member = menu_utama()
#====================================================== Menu 1
    if menu_member == 1:

        while True:

            menu_report = menu_data_member()

            if menu_report == 1:
                if len(members) == 0:                   
                    print('''              
    === Tidak Ada Data Member/Data Member Tidak Tersedia ===
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ''')
                else:                  
                    display_member()

            elif menu_report == 2:
                id_dicari = input('''
    -> Masukkan ID Member yang dicari : ''')

                for member in members:
                    if member["id_member"].upper() == id_dicari.upper():
                        display_cari_member(member)
                        break
                else:
                    print('''
    === ID Member Tidak Ditemukan/ID Member Tidak Tersedia ===
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ''')

            elif menu_report == 3:
                nama_dicari = input('''
    Masukkan Nama member yang dicari : ''')
                
                for member in members:
                    if nama_dicari.lower() in member["nama"].lower():
                        display_cari_member(member)
                        break
                else:
                    print(f'''
    -> Member Dengan Nama ('{nama_dicari}') Tidak Ditemukan/Tidak Tersedia xxx
    ''')

            elif menu_report == 4:
                no_dicari = input('''
    Masukkan No.Handphone 10-13 Digit : ''')

                for member in members:
                    if member["No Handphone"] == no_dicari:
                        display_cari_member(member)
                        break
                else:            
                    print('''
    Member Dengan No Handphone ini Tidak Ditemukan''')

            elif menu_report == 5:
                break

#========================================================= Menu 2                                                
    elif menu_member == 2:

        member = {}

        while True:

            menu_tambah = display_menu_tambah()

            if menu_tambah == 1:
                id_member =input('''
    Masukkan ID Member (Diawali dengan 'M') : ''')

                for i in members:
                    if i['id_member'] == id_member:
                        print('''
    -> ID Member sudah digunakan! Silahkan Masukkan ID Member yang lain.
    ''')                
                        break
                else:            
                    print(f'''
    -> ID Member {id_member} Tersedia, Melanjutkan pengisian Data Member
    ''')
                    member["id_member"] = id_member
                    
                    nama = input('''
    Nama : ''')
                    member["nama"] = nama

                    while True:
                        jenis_kelamin = input('''
    Jenis Kelamin (Laki-laki/Perempuan) : ''').capitalize()
                        if jenis_kelamin == "Laki-laki" or jenis_kelamin == "Perempuan":
                            break
                        else:
                            print('''
    Input tidak valid, silahkan input (Laki-laki/Perempuan)''')
                    member["jenis_kelamin"] = jenis_kelamin
                
                    no_hp = input('''
    Nomor Handphone 10-13 Digit : ''')
                    member["No Handphone"] = no_hp
                
                    alamat = input('''
    Alamat : ''')
                    member["alamat"] = alamat

                    display_membership()
                    while True:
                        membership = input('''
    Membership (Basic/Premium/VIP) : ''').upper()
                        if membership == "BASIC" or membership == "PREMIUM" or membership == "VIP":
                            break
                        else:
                            print('''
    Opsi tidak tersedia, Silahkan input (Basic/Premium/VIP) ''')
                    member["membership"] = membership

                    durasi = int(input('''
    Berapa bulan : '''))
                    member["durasi"] = durasi

                    for i in membership_list:
                        if i["nama"].upper() == membership:
                            harga = i["harga_bulanan"]*durasi
                            break
                    member["harga"] = harga



                    print(f'''
    ========================================
    |           DATA MEMBER BARU           |
    ========================================

        ID Member     : {id_member}                                  
        Nama          : {nama}                        
        Jenis Kelamin : {jenis_kelamin}
        No. Handphone : {no_hp}
        Alamat        : {alamat}                   
        Membership    : {membership}
        Durasi        : {durasi} Bulan
        Harga         : Rp.{harga:,} 
                
    ========================================''')
                
                    while True:
                        print(f'''
    Apakah Data Sudah Benar dan Mau Disimpan?

    1. Iya
    2. Edit Data
    3. Tidak
    ''')
                        konfirmasi = int(input('''
    Pilih Menu : '''))
                
                        if konfirmasi == 1:
                            members.append(member)
                            print('''
    === Selamat Data berhasil disimpan ===''')
                            break

                        elif konfirmasi == 2:
                            while True:
                                edit_data = int(input(f'''
    ========================================
    |           EDIT DATA MEMBER           |
    ========================================

        1.Nama            : {member["nama"]}
        2.Jenis Kelamin   : {member["jenis_kelamin"]}
        3.No. Handphone   : {member["No Handphone"]}
        4.Alamat          : {member["alamat"]}
        5.Membership      : {member["membership"]}
        6.Durasi          : {member["durasi"]} Bulan
          Harga           : Rp.{member['harga']:,}

        7.Kembali         

    ========================================
        Pilih : '''))   
                        
                                if edit_data == 1:
                                    nama_baru = input('''
    Masukkan Nama : ''')
                                    member["nama"] = nama_baru
                                

                                elif edit_data == 2:
                                    while True:
                                        jenis_kelamin_edit = input('''
    Jenis Kelamin (Laki-laki/Perempuan) : ''').capitalize()
                                        if jenis_kelamin_edit == "Laki-laki" or jenis_kelamin_edit == "Perempuan":
                                            member["jenis_kelamin"] = jenis_kelamin_edit
                                            break
                                        else:
                                            print('''
    Input tidak valid, silahkan input (Laki-laki/Perempuan)''')
                                        

                                elif edit_data == 3:
                                    no_hp_baru = input('''
    Nomor Handphone 10-13 Digit : ''')
                                    member["No Handphone"] = no_hp_baru
                                    

                                elif edit_data == 4:
                                    alamat_baru = input('''
    Alamat : ''')
                                    member["alamat"] = alamat_baru

                                elif edit_data == 5:
                                    while True:
                                        membership_edit = input('''
    Membership (Basic/Premium/VIP) : ''').upper()
                                        if membership_edit == "BASIC" or membership_edit == "PREMIUM" or membership_edit == "VIP":
                                            member["membership"] = membership_edit

                                            for i in membership_list:
                                                if i["nama"].upper() == membership_edit:
                                                    harga = i["harga_bulanan"]
                                                    break

                                            member["harga"] = harga * member["durasi"]
                                            break
                                        else:
                                            print("Opsi tidak tersedia, Silahkan input (Basic/Premium/VIP) ")
                                            

                                elif edit_data == 6:
                                    durasi_baru = int(input('''
    Berapa Bulan : '''))
                                    member["durasi"] = durasi_baru

                                    for i in membership_list:
                                        if i["nama"].upper() == member["membership"]:
                                            harga = i["harga_bulanan"]
                                            break

                                    member["harga"] = harga * member["durasi"]
                                
                                elif edit_data == 7:
                                    break
                                            
                        elif konfirmasi == 3:
                            break

            elif menu_tambah == 2:
                break

#========================================================= Menu 3
    elif menu_member == 3:
        while True:
            menu_update = display_menu_update()

            if menu_update == 1:  
                id_dicari = input('''
    Masukkan Id member : ''')

                for member in members:
                    if member["id_member"] == id_dicari:
                        display_cari_member(member)
                        break
                else:
                    print('''
    -> ID Member Tidak Tersedia/Tidak Ditemukan''')
                    continue  

                menu_konfirmasi = display_menu_konfirmasi()

                if menu_konfirmasi == 1:
                    while True:
                        menu_update = int(input('''
    ========================================
    Apa yang ingin Diubah ?

    1. Nama
    2. Jenis Kelamin
    3. No. Handphone
    4. Alamat
    5. Membership
    6. Durasi
    
    7. Kembali
    ========================================
    Pilih Angka Menu (1-7) : '''))
                        
                        if menu_update == 1:
                            update_nama = input('''
    Masukkan nama baru : ''')

                            menu_konfirmasi = display_menu_konfirmasi()
                    
                            if menu_konfirmasi == 1:
                                member["nama"] = update_nama

                                display_updated_data(member)

                                break

                            elif menu_konfirmasi == 2:
                                break

                        elif menu_update == 2:

                            while True:
                                update_jenis_kelamin = input('''
    Jenis Kelamin (Laki-laki/Perempuan) : ''')
                                if update_jenis_kelamin == "Laki-laki" or update_jenis_kelamin == "Perempuan":
                                    break
                                else:
                                    print('''
    Input tidak valid, silahkan input (Laki-laki/Perempuan)''')

                            menu_konfirmasi = display_menu_konfirmasi()
                    
                            if menu_konfirmasi == 1:
                                member["jenis_kelamin"] = update_jenis_kelamin

                                display_updated_data(member)
                                break
                            elif menu_konfirmasi == 2:
                                break

                        elif menu_update == 3:

                            update_no_hp = input('''
    Masukkan Nomor Handphone baru : ''')

                            menu_konfirmasi = display_menu_konfirmasi()
                    
                            if menu_konfirmasi == 1:
                                member["No Handphone"] = update_no_hp

                                display_updated_data(member)
                                break
                            elif menu_konfirmasi == 2:
                                break
                            
                        elif menu_update == 4:

                            update_alamat = input('''
    Masukkan alamat baru : ''')

                            menu_konfirmasi = display_menu_konfirmasi()
                    
                            if menu_konfirmasi == 1:
                                member["alamat"] = update_alamat

                                display_updated_data(member)
                                break
                            elif menu_konfirmasi == 2:
                                break

                        elif menu_update == 5:
                            # while True:
                                update_membership = input('''
    Membership (Basic/Premium/VIP) : ''').upper()
                                
                                menu_konfirmasi = display_menu_konfirmasi()
                    
                                if menu_konfirmasi == 1:
                                    if update_membership == "BASIC" or update_membership == "PREMIUM" or update_membership == "VIP":
                                        member["membership"] = update_membership   
                                    else:
                                        print('''
    Opsi tidak tersedia, Silahkan input (Basic/Premium/VIP) ''')

                                    for i in membership_list:
                                        if i["nama"].upper() == update_membership:
                                            harga_bulanan = i["harga_bulanan"]
                                            break

                                    member["harga"] = harga_bulanan*member["durasi"]

                                    display_updated_data(member)
                                    break
                                elif menu_konfirmasi == 2:
                                    break

                        elif menu_update == 6:
                            update_durasi = int(input('''
    Masukkan Durasi : '''))
                            
                            menu_konfirmasi = display_menu_konfirmasi()
                    
                            if menu_konfirmasi == 1:
                                member["durasi"] = update_durasi

                                for i in membership_list:
                                    if i["nama"].upper() == member["membership"]:
                                        harga_bulanan = i["harga_bulanan"]
                                        break

                                member["harga"] = update_durasi*harga_bulanan
                                
                                display_updated_data(member)
                                break
                            elif menu_konfirmasi == 2:
                                break

                        elif menu_update == 7:
                                break

                elif menu_konfirmasi == 2:
                    continue
            elif menu_update == 2:
                break  

#========================================================= Menu 4
    elif menu_member == 4:
            while True:
                menu_filter = display_menu_filter()
                
                if menu_filter == 1:
                    membership_filter = int(input('''

    Pilih Membership :
    1. Basic
    2. Premium
    3. VIP

    Pilih : '''))
                
                    if membership_filter == 1:
                        for member in members:
                            if member['membership'] == 'BASIC':
                                display_membership_filter(member)
                                            
                    elif membership_filter == 2:
                        for member in members:
                            if member['membership'] == 'PREMIUM':
                                display_membership_filter(member)

                    elif membership_filter == 3:
                        for member in members:
                            if member['membership'] == 'VIP':
                                display_membership_filter(member)
 
                if menu_filter == 2:
                    jenis_kelamin_filter = int(input('''

    Pilih Jenis Kelamin :
    1. Laki-laki
    2. Perempuan

    Pilih : '''))
                    if jenis_kelamin_filter == 1:
                        for member in members:
                            if member['jenis_kelamin'] == 'Laki-laki':
                                display_membership_filter(member)

                    elif jenis_kelamin_filter == 2:
                        for member in members:
                            if member['jenis_kelamin'] == 'Perempuan':
                                display_membership_filter(member)

                if menu_filter == 3:
                    durasi_filter = int(input('''

    1. Kurang dari 3 Bulan
    2. 3 - 5 Bulan
    3. 6 - 11 Bulan
    4. 12 Bulan+

    Pilih (1-4) : '''))
                            
                    if durasi_filter == 1:
                        for member in members:
                            if member['durasi'] < 3:
                                display_membership_filter(member)
                            
                    elif durasi_filter == 2:
                        for member in members:
                            if member['durasi'] >= 3 and member['durasi'] <= 5:
                                display_membership_filter(member)

                    elif durasi_filter == 3:
                        for member in members:
                            if member['durasi'] >= 6 and member['durasi'] <= 11:
                                display_membership_filter(member)

                    elif durasi_filter == 4:
                        for member in members:
                            if member['durasi'] >= 12:
                                display_membership_filter(member)

                if menu_filter == 4:
                        harga_filter = int(input('''

    1. Di Bawah Rp500.000 
    2. Rp500.000 - Rp1.000.000 
    3. Rp1.000.001 - Rp2.000.000 
    4. Di Atas Rp2.000.000 

    Pilih Angka Menu (1-4) : '''))
                        if harga_filter == 1:
                            for member in members:
                                if member['harga'] < 500000:
                                    display_membership_filter(member)
                            
                        elif harga_filter == 2:
                            for member in members:
                                if member['harga'] >= 500000 and member['harga'] <= 1000000:
                                    display_membership_filter(member)

                        elif harga_filter == 3:
                            for member in members:
                                if member['harga'] > 1000000 and member['harga'] <= 2000000:
                                    display_membership_filter(member)

                        elif harga_filter == 4:
                            for member in members:
                                if member['harga'] > 2000000:
                                    display_membership_filter(member)
                        else:
                            print(f'''
    -> Input Salah, Masukkan Angka Menu (1-4)''')

                elif menu_filter == 5:
                    break

#========================================================= Menu 5
    elif menu_member == 5:
        while True:  
            menu_sorting = display_menu_sorting()
            
            if menu_sorting == 1:
                sudah_sortir(members, "nama")

            elif menu_sorting == 2:
                sudah_sortir(members, "nama", True)

            elif menu_sorting == 3:
                sudah_sortir(members, "harga")
                
            elif menu_sorting == 4:
                sudah_sortir(members, "harga", True)

            elif menu_sorting == 5:
                sudah_sortir(members, "durasi")

            elif menu_sorting == 6:
                sudah_sortir(members, "harga", True)

            elif menu_sorting == 7:
                break    

#========================================================= Menu 6
    elif menu_member == 6:
        while True:
            menu_hapus = display_menu_hapus()
            
            if menu_hapus == 1:  
                
                id_dicari = input('''
    Masukkan Id member : ''')

                for member in members:
                    if member["id_member"] == id_dicari:
                        display_hapus_member(member)
                        break
                else:
                    print('''
    -> ID Member Tidak Tersedia/Tidak Ditemukan''')
                    continue            

                hapus_member = int(input('''
    Apakah anda yakin ingin menghapus data member ini? 
    
    1. Iya
    2. Tidak

    Pilih : '''))
                if hapus_member == 1:
                    members.remove(member)
                    print('''
    === Member berhasil dihapus ===''')
                    break
                elif hapus_member == 2: 
                    break

            elif menu_hapus == 2:
                break 

#========================================================= Menu 6 
    elif menu_member == 7:
            exit_program = int(input(f'''
    Apakah anda yakin ingin Keluar/Exit dari program ini?
    
    1. Iya
    2. Tidak

    Pilih angka Menu (1 atau 2 ) : '''))
                    
            if exit_program == 1:
                print('''
    =============================
    |   Bye, Sampai jumpa lagi  |
    =============================
        ''')    
                menu_member = False
                break
                    
            else:
                continue

