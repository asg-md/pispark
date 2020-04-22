import re
import unidecode
import pandas as pd

# def cargar_texto(filename):
#     with open(filename, encoding="utf8") as f:
#         lines = f.readlines()
#         lines = [x.strip() for x in lines]
#     f.close()
#     return lines

def cargar_texto(filename):
    with open(filename, mode = 'r', encoding="utf8") as fichero:
        return fichero.read()


def partidor_palabras(texto):
    result = re.split(
        "[.]|" +
        "[,]|" +
        "[:]|" +
        "[;]|" +
        "[-]|" +
        "[–]|" +
        "[_]|" +
        "[{]|" +
        "[}]|" +
        "[']|" +
        "[¡]|" +
        "[!]|" +
        "[¿]|" +
        "[?]|" +
        "[(]|" +
        "[)]|" +
        "[>]|" +
        "[<]|" +
        "[#]|" +
        "[&]|" +
        "[/]|" +
        "[\]]|" +
        "[\[]|" +
        "[“]|" +
        "[\"]|" +
        "[”]" +
        "[”]" +
        "[\n]" +
        "[0-9]+|" +
        "\s", texto)
    result = [individual_word for individual_word in result if len(individual_word) > 0]
    return result


def limpiar_acentos(texto):
    return unidecode.unidecode(texto)

PALABRAS_stopwordsspanish = None
def cargar_stopwordsspanish():
    global PALABRAS_stopwordsspanish
    if PALABRAS_stopwordsspanish == None:
        filename = "stopwordsspanish.txt"
        stopwords_l = cargar_texto(filename)
        PALABRAS_stopwordsspanish = partidor_palabras(limpiar_acentos(stopwords_l).upper())
    return PALABRAS_stopwordsspanish

def contar_words(texto_limpio_partido):
    stopwords_limpio_partido = cargar_stopwordsspanish()
    cuenta_df = pd.DataFrame({'Palabras': list(filter(lambda elem: elem not in stopwords_limpio_partido, texto_limpio_partido)), 'Repeticiones':  1})
    tabla_final = cuenta_df.groupby(by='Palabras').agg({'Repeticiones': 'count'}).reset_index().sort_values(by=['Repeticiones'], ascending=False)
    return tabla_final.reset_index()[['Palabras','Repeticiones']].values.tolist()

filename = "el_quijote.txt"
# filename = "texto_prueba.txt"

lines = cargar_texto(filename)
texto_limpio_partido = partidor_palabras(limpiar_acentos(lines).upper())
contar_words_df = contar_words(texto_limpio_partido)

# contar_words_df
print(contar_words_df)

# kkk
