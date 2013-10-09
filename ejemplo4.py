import nltk
import os
import cPickle

root_path = 'eptmk/'
re_fileids = r'.*\.txt'
re_word_tokenize = \
        r"""([A-Z]\.)+|i\.v\.|\$?\d+(\.\d+)?%?\$?|\w+(-\w+)*|\.+|[][}{><"'&%,:;!?()*+/=-]"""
my_word_tokenizer = nltk.tokenize.RegexpTokenizer(re_word_tokenize)


# El tokenizador previamente entrenado no reconoce nuestras siglas. Tendremos
# que entrenar nuestro propio segmentador sobre el corpus.
raw_corpus = []
for archivo in sorted(os.listdir(root_path)):
    with open(root_path + archivo, 'r') as texto:
        raw_corpus.append(texto.read().strip())
raw_corpus = ' '.join(raw_corpus)
my_sent_tokenizer = nltk.tokenize.PunktSentenceTokenizer(train_text=raw_corpus)


# Es conveniente guardar nuestro segmentador de oraciones entrenado sobre
# nuestro corpus para usarlo en el futuro. Asi no tenemos que entrenarlo cada
# vez que lo queramos usar, ya que esto se puede demorar. Para esto usaremos
# la libreria cPickle, que nos permite serializar objectos de Python y
# salvarlos al disco.
with open('sent_tokenizer.pickle', 'wb') as arch:
    cPickle.dump(my_sent_tokenizer, arch, -1)


# Instanciar la clase PlaintextCorpusReader.
eptmk = nltk.corpus.PlaintextCorpusReader(root=root_path,
                                          fileids=re_fileids,
                                          word_tokenizer=my_word_tokenizer,
                                          sent_tokenizer=my_sent_tokenizer)


# Veamos como queda la segmentacion de oraciones.
[s for s in eptmk.sents(fileids='eptmk0002.txt')]
