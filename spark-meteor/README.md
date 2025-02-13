# Spark Meteor Analysis 🌠

## Descrição

Este projeto realiza análise de meteoros usando **Apache Spark**. Ele lê um conjunto de dados contendo informações sobre meteoros, incluindo tamanho, velocidade e chance de impacto, e executa consultas para identificar os meteoros mais rápidos e os mais perigosos.

## Estrutura do Projeto

```
spark-meteor-analysis/
│── create_dataset.py       # Script para gerar um dataset de meteoros
│── Dockerfile              # Configuração para execução em contêiner
│── meteor_analysis.py      # Script principal para análise dos meteoros
│── meteors-example.csv     # Exemplo de dataset de meteoros
│── meteors.csv             # Dataset principal
│── spark-pv-pvc.yaml       # Configuração de volume persistente no Kubernetes
```

## Como Funciona ☄️

- **Apache Spark** é usado para processar os dados dos meteoros.
- O dataset `meteors.csv` é carregado como um DataFrame Spark.
- Os dados são convertidos para os tipos corretos (`float` para tamanho, velocidade e chance de impacto).
- São exibidos os meteoros:
  - **Mais rápidos**, ordenados pela coluna `speed_kmh`.
  - **Mais perigosos**, ordenados pela coluna `impact_chance`.

## Execução 🛠️

### 1. Executar localmente

Se você já possui o **Apache Spark** instalado:

```sh
python meteor_analysis.py
```

### 2. Usando Docker

```sh
docker build -t spark-meteor-analysis .
docker run --rm spark-meteor-analysis
```

### 3. Usando Kubernetes

Se estiver rodando em um cluster Kubernetes:

```sh
kubectl apply -f spark-pv-pvc.yaml
kubectl run spark-analysis --image=spark-meteor-analysis --restart=Never
```

## Tecnologias Utilizadas 🖥️

- **Apache Spark** para processamento distribuído
- **Python** como linguagem principal
- **Docker** para conteinerização
- **Kubernetes** para orquestração

## Exemplo de Saída

```
🌠 Meteoros Mais Rápidos:
+--------+---------+--------------+
|   Nome |size_km | speed_kmh    |
+--------+---------+--------------+
|MeteoroX|   1.23 | 75000.0      |
|MeteoroY|   2.10 | 68000.0      |
...

🔥 Meteoros Mais Perigosos:
+--------+--------------+
|   Nome |impact_chance|
+--------+--------------+
|MeteoroA|        0.98  |
|MeteoroB|        0.95  |
...
```
