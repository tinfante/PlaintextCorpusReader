import nltk


# Subdirectorio (del actual) con los archivos.
root_path = 'eptmk/'

# Expresion regular para los archivos a ser cargados.
re_fileids = r'.*\.txt'


eptmk = nltk.corpus.PlaintextCorpusReader(root=root_path,
                                          fileids=re_fileids)

# Proximas lineas solo muestran resultados dentro del promp interactivo.
# Si se ejecutan desde un script hay que anteponer un "print".

# Mostrar archivos del corpus.
eptmk.fileids()

# Mostrar primeras 100 palabras del corpus.
[w for w in eptmk.words()][:100]

# Mostrar primeras 10 oraciones del corpus.
[s for s in eptmk.sents()][:10]

# Veamos que pasa con el metodo paras() para mostrar parrafos.
# Mostramos los dos primeros parrafos. Tenemos un problema!
[p for p in eptmk.paras()][:2]


# Veamos la segmentacion de palabras y oraciones en un caso complicado.
# Primero veamos el texto crudo.
eptmk.raw(fileids='eptmk0002.txt')

# Se ve raro. Que es ese \n? Si no ponemos "print" nos tira el output de la
# funcion o metodo. Para que nos muestre una representacion mas humana
# ponemos "print" antes.
print eptmk.raw(fileids='eptmk0002.txt')

# OK. Ahora comparemos esto con la segmentacion de palabras.
[w for w in eptmk.words(fileids='eptmk0002.txt')]

# Ahora con la segmentacion de oraciones.
[s for s in eptmk.sents(fileids='eptmk0002.txt')]
