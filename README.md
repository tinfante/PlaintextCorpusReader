PlaintextCorpusReader
=====================

Ejemplos para cargar corpus propios en NLTK con PlaintextCorpusReader.
<br />
<br />

<strong>Argumentos para instanciar la clase PlaintextCorpusReader</strong>

root&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(obligatorio)<br />
fileids&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(obligatorio)<br />
word_tokenizer&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. WordPunctTokenizer() por defecto)<br />
sent_tokenizer&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. nltk.data.LazyLoader() por defecto)<br />
para_block_reader&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. read_blankline_block por defecto)<br />
encoding&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. None por defecto)<br />
<br />

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
<br />

<strong>Algunas funciones utiles</strong>

dir(__OBJECTO__)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;muestra nombres definidos para un objecto.<br />
repr(__OBJECTO__)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;muestra la representacion de un objecto con simbolos especiales. Especialmente util para cadenas de caracteres.<br />

