from pyspark.sql import SparkSession
import logging

# Configurando logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Iniciando a sessão Spark")
try:
    spark = SparkSession.builder.appName("DataFrame Example").getOrCreate()
    logger.info("Sessão Spark iniciada com sucesso")
except Exception as e:
    logger.error(f"Erro ao iniciar a sessão Spark: {e}")

data = [("James", "Smith", "USA", "CA"), ("Anna", "Rose", "USA", "NY")]
columns = ["FirstName", "LastName", "Country", "State"]

try:
    df = spark.createDataFrame(data, schema=columns)
    logger.info("DataFrame criado com sucesso")
except Exception as e:
    logger.error(f"Erro ao criar DataFrame: {e}")

try:
    df.show()
    logger.info("DataFrame exibido com sucesso")
except Exception as e:
    logger.error(f"Erro ao exibir DataFrame: {e}")

try:
    df.createOrReplaceTempView("people")
    logger.info("View temporária criada com sucesso")
except Exception as e:
    logger.error(f"Erro ao criar view temporária: {e}")

try:
    sqlDF = spark.sql("SELECT * FROM people WHERE State = 'CA'")
    logger.info("Consulta SQL executada com sucesso")
except Exception as e:
    logger.error(f"Erro ao executar consulta SQL: {e}")

try:
    sqlDF.show()
    logger.info("Resultado da consulta exibido com sucesso")
except Exception as e:
    logger.error(f"Erro ao exibir resultado da consulta: {e}")
