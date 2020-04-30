

from pyspark.sql import SparkSession

from EstimarPI import estimar_pi

def crear_sesion_spark():
    NUMERO_MAXIMO_CPUS = 3
    SPARK_MASTER = "local[" + str(NUMERO_MAXIMO_CPUS) + "]"

    return SparkSession \
        .builder \
        .master(SPARK_MASTER) \
        .appName("ContarPalabras") \
        .getOrCreate()


NUMERO_MAXIMO_CPUS = 3
SPARK_MASTER = "local["+str(NUMERO_MAXIMO_CPUS)+"]"


def estimar_pi_spark(calculos, numero_bloques):

    spark = crear_sesion_spark()

    calculos_por_bloque = int(calculos / numero_bloques)
    bloques = [calculos_por_bloque] * numero_bloques

    total = spark.sparkContext.parallelize(bloques, numero_bloques).map(estimar_pi).reduce(sumar)

    return total / numero_bloques


def sumar(a, b):
    return a + b

print(estimar_pi_spark(100*1000*1000, 3 ))