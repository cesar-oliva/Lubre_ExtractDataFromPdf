import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import pandas as pd
import numpy as np



#ruta de archivo
filename = './document/202210-2453688-VISA DEBIT.pdf' 
#abrir para lectrura.
pdfFileObj = open(filename,'rb')
#se analiza el archivo
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#paginas a analizar
num_pages = pdfReader.numPages
count = 0
text = ""
#leer cada pagina
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
#valido los datos si existen
if text != "":
   text = text
#si no existen los datos los extraigo
else:
   text = textract.process(fileurl, method='tesseract', language='esp')

lines = text.split('\n')
#print(lines)

len(lines)

index_rv = []

for line in lines:
    if re.findall(r'\bVENTAS C/DESCUENTO CONTADO\b', line):
        index_rv.append(1)
    else:
        index_rv.append(0)

index_rv = [i for i, s in enumerate(index_rv) if s==1 in index_rv]



print(index_rv)

result = []
for i in index_rv:
    stock = lines[i:i+1]
    #indice_c = cadena.index('c')
    stock = stock[0].split(' $ ') + stock[1:]
    result.append(stock)
    
df = pd.DataFrame(result, columns = ['Descripcion','Importe'])

print(df)
