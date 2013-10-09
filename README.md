PlaintextCorpusReader
=====================

Ejemplos para cargar corpus propios en NLTK con PlaintextCorpusReader.
<br />
<br />

<b>Argumentos para instanciar la clase PlaintextCorpusReader</b>

root&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(obligatorio - directorio con archivos)<br />
fileids&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(obligatorio - regexp para archivos que cargar)<br />
word_tokenizer&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. WordPunctTokenizer() por defecto - segmentador de palabras)<br />
sent_tokenizer&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. nltk.data.LazyLoader() por defecto - segmentado de oraciones)<br />
para_block_reader&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. read_blankline_block por defecto - segmentador de parrafos)<br />
encoding&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(opcional. None por defecto - codificacion de los textos)<br />
<br />

<b>Segmentadores incluidos en NLTK</b>

Muchas de estas clases tienen una funcion equivalente.<br />
<code>dir(nltk.tokenize)</code> para detalles.<br />

WhitespaceTokenizer()<br />
SpaceTokenizer()<br />
LineTokenizer(blanklines='keep')<br />
LineTokenizer(blanklines='discard')<br />
TabTokenizer()<br />
RegexpTokenizer()<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WordTokenizer()<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;WordPunctTokenizer()<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;BlanklineTokenizer()<br />
SExprTokenizer()<br />
PunktSentenceTokenizer()<br />
PunktWordTokenizer()<br />
TreebankWordTokenizer()<br />
<br />

<b>Algunas funciones utiles</b>

<code>dir(<i>OBJECTO</i>)</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;muestra nombres definidos para un objecto.<br />
<code>repr(<i>OBJECTO</i>)</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;representa un objecto literalmente. Especialmente util para cadenas de caracteres.<br />
<code>help(<i>OBJECTO</i>)</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;muestra documentacion para objecto.<br />
<code>import inspect; print inspect.getsource(<i>OBJECTO</i>)</code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;muestra codigo fuente para objecto.
