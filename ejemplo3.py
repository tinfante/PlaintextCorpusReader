import nltk


root_path = 'eptmk/'
re_fileids = r'.*\.txt'
re_word_tokenize = \
        r"""([A-Z]\.)+|i\.v\.|\$?\d+(\.\d+)?%?\$?|\w+(-\w+)*|\.+|[][}{><"'&%,:;!?()*+/=-]"""
my_word_tokenizer = nltk.tokenize.RegexpTokenizer(re_word_tokenize)


# Instanciar la clase PlaintextCorpusReader.
eptmk = nltk.corpus.PlaintextCorpusReader(root=root_path,
                                          fileids=re_fileids,
                                          word_tokenizer=my_word_tokenizer)


# Veamos como quedo la segmentacion por palabra para el texto complicado.
[w for w in eptmk.words(fileids='eptmk0002.txt')]

# Ya dijimos que i.v. es un token, que pasa con la segmentacion de oraciones?
[s for s in eptmk.sents(fileids='eptmk0002.txt')]
