Folder yang isinya boleh diedit:
1. classes = berisi file class dari setiap tabel
2. config = file local.env berisi koneksi database
3. forms = berisi file py tampilan window untuk memanggil file ui (design)
4. panel = berisi file py untuk memanggil file py dari folder form
5. ui = berisi file ui (design)
6. icons = berisi file gambar (png)

Langkah praktikum:
1. Siapkan tabel di postgresql berikut isinya
2. Buat sebuah class untuk tabel tsb beri nama: Namatabel.py
   cth: Mahasiswa.py (nama sebuah class sengaja huruf awalnya kapital)
3. Desain Form untuk tabel tersebut di Qt Designer
   simpan hasilnya dgn nama : namatabel.ui
   cth: mahasiswa.ui
4. Buat file py untuk memanggil file ui, beri nama : frmNamatabel.py
   cth: frmMahasiswa.py (nama file ini sengaja diawali dengan frm diikuti nama tabelnya 
   dgn diawali nama tabel huruf kapital)
5. Buat file panel untuk memanggil file frmNamatabel.py beri nama: 
   NamatabelPanel.py
   cth: MahasiswaPanel.py
6. Copy ke-4 file diatas dgn ketentuan sbg berikut:
   Nama File      	    Nama Folder
   Mahasiswa.py  	         classes
   mahasiswa.ui		      ui
   frmMahasiswa.py	      forms
   MahasiswaPanel.py	      panel
7. Koneksi database
   Edit file: config/local.env
8. Edit file: forms/MainWindow.py untuk menambahkan tombol
   pada Ribbon Menu
9. Test Run:
   jalankan file : main.py

