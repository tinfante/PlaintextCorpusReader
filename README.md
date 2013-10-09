PlaintextCorpusReader
=====================

Ejemplos para cargar corpus propios en NLTK con PlaintextCorpusReader.


Argumentos para instanciar la clase PlaintextCorpusReader
---------------------------------------------------------

root                        (obligatorio)
fileids                     (obligatorio)
word_tokenizer              (opcional. WordPunctTokenizer() por defecto)
sent_tokenizer              (opcional. nltk.data.LazyLoader() por defecto)
para_block_reader           (opcional. read_blankline_block por defecto)
encoding                    (opcional. None por defecto)
