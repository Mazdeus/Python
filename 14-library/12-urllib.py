from urllib.request import urlopen
import gzip

# Pengambilan konten
url = "http://python.org/"
response = urlopen(url)

# Memeriksa jika konten terkompresi
if response.info().get('Content-Encoding') == 'gzip':
    buf = gzip.GzipFile(fileobj=response)
    html = buf.read().decode('utf-8')
else:
    html = response.read().decode('utf-8')

# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)
