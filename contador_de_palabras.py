import re
import unidecode

def cargar_texto(filename):
    with open(filename, encoding="utf8") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    f.close()
    return lines


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
        "[0-9]+|" +
        "\s", texto)
    result = [individual_word for individual_word in result if len(individual_word) > 0]
    return result


def limpiar_acentos(texto):
    return unidecode.unidecode(texto)


def contador_de_palabras(lineas_texto):
    lista_txt_all = []
    for i in lineas_texto:
        lista_txt_all = lista_txt_all + partidor_palabras(limpiar_acentos(i))
    return len(lista_txt_all)



# filename = "el_quijote.txt"
filename = "texto_prueba.txt"

lines = cargar_texto(filename)
n_palabras = contador_de_palabras(lines)
print(n_palabras)
