PlaintextCorpusReader
=====================

Ejemplos para cargar corpus propios en NLTK con PlaintextCorpusReader.


<strong>Argumentos para instanciar la clase PlaintextCorpusReader</strong>

root                        (obligatorio)<br />
fileids                     (obligatorio)<br />
word_tokenizer              (opcional. WordPunctTokenizer() por defecto)<br />
sent_tokenizer              (opcional. nltk.data.LazyLoader() por defecto)<br />
para_block_reader           (opcional. read_blankline_block por defecto)<br />
encoding                    (opcional. None por defecto)<br />


<strong>Segmentadores incluidos en NLTK (ver nltk.tokenize)</strong>

WhitespaceTokenizer()<br />
SpaceTokenizer()<br />
LineTokenizer(blanklines='keep')<br />
LineTokenizer(blanklines='discard')<br />
TabTokenizer()<br />
RegexpTokenizer()<br />
    WordTokenizer()<br />
    WordPunctTokenizer()<br />
    BlanklineTokenizer()<br />
SExprTokenizer()<br />
PunktSentenceTokenizer()<br />
PunktWordTokenizer()<br />
TreebankWordTokenizer()<br />
