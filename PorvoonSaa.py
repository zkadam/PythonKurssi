

import http.client

conn=http.client.HTTPSConnection("www.ilmatieteenlaitos.fi")
conn.request("GET", "/saa/porvoo")
vastaus=conn.getresponse()
html=str(vastaus.read())


indeksi = html.index('<span class="temperature-')

alku=indeksi+47
loppu=alku+3
lämpötila=html[alku:loppu]
# print(lämpötila)
if lämpötila[2]=="\\":
   lämpötila=lämpötila[0:2]
print(f"Lämpötila Porvoossa: {lämpötila} astetta.")