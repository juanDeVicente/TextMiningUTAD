import os
import nltk
from nltk.corpus import stopwords
import sys


def word_frequency(text, stopwords_language='english'):
    # sacamos el numero de veces que la palabra se utiliza sin stopwords a lo largo de todos los tweets
    # multiplicamos por 100 para que lo tengamos en porcentaje

    nltk.data.path.append(os.path.dirname(__file__) + '/nltk_data')
    if not isinstance(text, str) or not isinstance(stopwords_language, str):
        raise ValueError

    if text == '':
        return []

    text = text.strip()
    text = ' '.join(text.split())  # Quitamos todos los espacios extra entre palabras
    words = text.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "") \
        .replace("¿", "").replace("¡", "")
    # Los apostrofes son un problema, asi que hay que cambiar los signos de puntuacion a mano
    words = words.strip()

    if words == '':
        return []

    words = words.split(' ')  # Separamos por palabras

    words = [word.lower() for word in words if word.lower() not in stopwords.words(stopwords_language)]

    words_count = {}

    words_total = len(words)

    for key in words:
        words_count[key] = words_count.get(key, 0) + 1
        # get funciona tal que si existe la clave devuelve el valor, si no devuelve el segundo parametro

    if len(words_count) == 0:
        return []

    #map(words_count.items(), key=lambda x: x[1]/words_total)

    for key in words_count:
        words_count[key] = round((words_count[key] / words_total)*100, 1)

    return sorted(words_count.items(), key=lambda x: x[1], reverse=True)  # Ordenamos las palabras segun lo pedido


def main(args):
    """Main entry point allowing external calls
    Args:
      args ([str]): command line parameter list
    """


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    print(word_frequency('¿¿¿¿????? ¡¡¡¡ ???? !!!!! ... ,,,,'))
