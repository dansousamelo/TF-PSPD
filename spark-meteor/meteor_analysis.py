from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc

spark = SparkSession.builder.appName("MeteorAnalysis").getOrCreate()

df = spark.read.option("header", "true").csv("/mnt/data/meteors.csv")

df = df.withColumn("size_km", col("size_km").cast("float")) \
       .withColumn("speed_kmh", col("speed_kmh").cast("float")) \
       .withColumn("impact_chance", col("impact_chance").cast("float"))

# 🚀 1. Meteoros mais rápidos
print("\n🌠 Meteoros Mais Rápidos:")
df.orderBy(desc("speed_kmh")).show()

# 🚀 2. Meteoros mais perigosos (com maior chance de impacto)
print("\n☄️ Meteoros Mais Perigosos:")
df.orderBy(desc("impact_chance")).show()

# 🚀 3. Localização dos Meteoros (quantos foram detectados por país)
print("\n🌍 Contagem de Meteoros por País:")
df.groupBy("location").count().orderBy(desc("count")).show()

# 🚀 4. Estatísticas gerais sobre meteoros
print("\n📊 Estatísticas sobre Meteoros:")
df.describe(["size_km", "speed_kmh", "impact_chance"]).show()

# 🚀 5. Identificar Meteoros que são maiores que 5 km
print("\n🛰️ Meteoros Gigantes (> 5 km):")
df.filter(col("size_km") > 5).show()

# 🚀 6. Criar um alerta para Meteoros que são muito rápidos e grandes
print("\n🚨 ALERTA: Meteoros Potencialmente Perigosos (Tamanho > 3km e Velocidade > 50.000 km/h)")
df.filter((col("size_km") > 3) & (col("speed_kmh") > 50000)).show()

spark.stop()
