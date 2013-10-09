PlaintextCorpusReader
=====================

Ejemplos para cargar corpus propios en NLTK con PlaintextCorpusReader.


<strong>Argumentos para instanciar la clase PlaintextCorpusReader</strong>

root&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(obligatorio)<br />
fileids&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(obligatorio)<br />
word_tokenizer&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. WordPunctTokenizer() por defecto)<br />
sent_tokenizer&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. nltk.data.LazyLoader() por defecto)<br />
para_block_reader&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. read_blankline_block por defecto)<br />
encoding&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. None por defecto)<br />


<strong>Segmentadores incluidos en NLTK (ver nltk.tokenize)</strong>

WhitespaceTokenizer()<br />
SpaceTokenizer()<br />
LineTokenizer(blanklines='keep')<br />
LineTokenizer(blanklines='discard')<br />
TabTokenizer()<br />
RegexpTokenizer()<br />
&nbsp;&nbsp;&nbsp;&nbsp;WordTokenizer()<br />
&nbsp;&nbsp;&nbsp;&nbsp;WordPunctTokenizer()<br />
&nbsp;&nbsp;&nbsp;&nbsp;BlanklineTokenizer()<br />
SExprTokenizer()<br />
PunktSentenceTokenizer()<br />
PunktWordTokenizer()<br />
TreebankWordTokenizer()<br />
