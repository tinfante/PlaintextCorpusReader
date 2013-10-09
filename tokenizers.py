from nltk.tokenize import *


s = ('Good muffins\tcost $3.88\nin New York.  Please buy me\n'
     'two of them.\n\nThanks.')


# Output, representacion "humana" y literal.
s
print s
repr(s)
print repr(s)


# Segmenta en cualquier whitespace (' ', '\n', '\t', etc.)
WhitespaceTokenizer().tokenize(s)
# Igual a:
s.split()


# Segmenta solo con espacio en blanco ' '.
SpaceTokenizer().tokenize(s)
# Igual a:
s.split(' ')


# Segmenta en lineas nuevas '\n'. Mantiene lineas vacias.
LineTokenizer(blanklines='keep').tokenize(s)
# Igual a:
s.split('\n')


# Segmenta en lineas nuevas '\n'. Elimina lineas vacias.
LineTokenizer(blanklines='discard').tokenize(s)
# Igual a:
[l for l in s.split('\n') if l.strip()]


# Segmenta en tabs ('\t').
TabTokenizer().tokenize(s)
# Igual a:
s.split('\t')


# Segmenta usando expresiones regulares definidas por nosotros.
# Palabras con primera letra mayuscula:
re_tokenizer = RegexpTokenizer(r'[A-Z][a-z]+')
re_tokenizer.tokenize(s)

# Con una expresion regular mas comprensiva.
re_tokenizer = RegexpTokenizer(r'\w+|\$\d+(\.\d+)|\S+')
re_tokenizer.tokenize(s)

# O podemos especificar que haga matches sobre el separador.
re_tokenizer = RegexpTokenizer(r'\s+', gaps=True)
re_tokenizer.tokenize(s)

# Subclases de RegexpTokenizer.
# Usa r'\w+|[^\w\s]+':
WordPunctTokenizer().tokenize(s)

# Usa r'\s*\n\s*\n\s*'
BlanklineTokenizer().tokenize(s)

# O se pueden usar las funciones equivalentes:
word_tokenize(s)
wordpunct_tokenize(s)
blankline_tokenize(s)
# Y dar nuestra propia expresion regular:
regexp_tokenize(s, pattern='\w+|\$\d+(\.\d+)|\S+')


# PunktSentenceTokenizer segmenta oraciones usando un algoritmo no-supervisado
# que crea un modelo de abreviaciones y siglas, colocaciones, y palabras que
# empiezan oraciones.
# Kiss, Tibor and Strunk (2006): "Unsupervised Multilingual Sentence Boundary
# Detection", Computational Linguistics 32, pp. 485-525.

import nltk.data
text = """
Punkt knows that periods in Mr. Smith and Johann S. Bach do not mark sentence
boundaries.   And sometimes setences can start with non-capitalized words.
i is a good variable name.
"""

# Usemos el punkt sentence tokenizer previamente entrenado para el ingles que
# viene en nltk.data.
punkt_sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
print '\n----\n'.join(punkt_sent_tokenizer.tokenize(text.strip()))

# el modulo nltk.tokenize.punkt tambien define PunktWordTokenizer, que usa una
# serie de expresiones regulares para dividir palabras en tokens.
PunktWordTokenizer().tokenize(s)
