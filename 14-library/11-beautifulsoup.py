from urllib.request import urlopen
from bs4 import BeautifulSoup
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

# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Mencetak judul halaman
print(soup.title)
