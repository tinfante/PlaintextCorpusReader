import nltk
import cPickle

root_path = 'eptmk/'
re_fileids = r'.*\.txt'
re_word_tokenize = \
        r"""([A-Z]\.)+|i\.v\.|\$?\d+(\.\d+)?%?\$?|\w+(-\w+)*|\.+|[][}{><"'&%,:;!?()*+/=-]"""
my_word_tokenizer = nltk.tokenize.RegexpTokenizer(re_word_tokenize)


# Ahora podemos cargar nuestro segmentador de oraciones previamente entrenado.
pickled_sent_tkn = open('sent_tokenizer.pickle', 'rb')
my_sent_tokenizer = cPickle.load(pickled_sent_tkn)


# Que mas? Definamos la segmentacion de parrafos.
para_segment = nltk.corpus.reader.util.read_line_block


# Por ultimo, definamos la codificacion de texto de nuestro corpus. Nos
# transforma nuestras cadenas de caracteres simples (str) a cadenas
# unicode. No es realmente necesario para este corpus, pero si trabajan con
# textos en castellano es necesario ya que las letras con acentos se
# encuentran fuera del rango ASCII.
corpus_encoding = 'utf-8'


# Instanciar la clase PlaintextCorpusReader.
eptmk = nltk.corpus.PlaintextCorpusReader(root=root_path,
                                          fileids=re_fileids,
                                          word_tokenizer=my_word_tokenizer,
                                          sent_tokenizer=my_sent_tokenizer,
                                          para_block_reader=para_segment,
                                          encoding=corpus_encoding)


# Veamos como queda la segmentacion de parrafos.
[p for p in eptmk.paras(fileids='eptmk0002.txt')]
