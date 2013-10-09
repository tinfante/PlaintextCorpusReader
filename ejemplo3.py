import nltk


root_path = 'eptmk/'
re_fileids = r'.*\.txt'
re_word_tokenize = \
        r"""([A-Z]\.)+|i\.v\.|\$?\d+(\.\d+)?%?\$?|\w+(-\w+)*|\.+|[][}{><"'&%,:;!?()*+/=-]"""
my_word_tokenizer = nltk.tokenize.RegexpTokenizer(re_word_tokenize)

# Definamos una instancia para segmentar oraciones.
my_sent_tokenizer = nltk.tokenize.PunktSentenceTokenizer()


# Instanciar la clase PlaintextCorpusReader.
eptmk = nltk.corpus.PlaintextCorpusReader(root=root_path,
                                          fileids=re_fileids,
                                          word_tokenizer=my_word_tokenizer,
                                          sent_tokenizer=my_sent_tokenizer)


# Veamos como queda la segmentacion de oraciones.
[s for s in eptmk.sents(fileids='eptmk0002.txt')]
