"""
Contoh tindakan menambahkan Argument yang bersifat 
opsional/tidak wajib dengan menggunakan ArgParse adalah berikut.
"""
# import argparse
 
# parser = argparse.ArgumentParser()
# parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
# args = parser.parse_args()
 
# if args.output:
#    print("Halo, ini merupakan sebuah output dari panggildicoding.py")

"""
Kita juga bisa membuat argumennya bersifat wajib. 
Modifikasi berkas panggildicoding.py menjadi seperti berikut.
"""

import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
args = parser.parse_args()
 
print("Terima kasih telah menggunakan panggildicoding.py, "+args.nama)