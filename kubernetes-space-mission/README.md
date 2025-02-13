# Kubernetes Space Mission 🚀

## Descrição

Este projeto simula uma missão espacial utilizando microsserviços e Kubernetes. Ele é composto por três principais componentes:

1. **Control Center**: O centro de controle da missão, responsável por monitoramento e recebimento de dados.
2. **Data Processor**: Um processador de dados que periodicamente verifica o status da missão.
3. **Explorer**: Um explorador espacial que envia coordenadas e status para o centro de controle.

## Estrutura do Projeto

```
kubernetes-space-mission/
│── app/
│   │── control_center.py  # Servidor Flask gerenciando a missão
│   │── data_processor.py  # Consulta periódica do status da missão
│   │── explorer.py        # Simula um explorador enviando dados
│── deployment/           # Configurações do Kubernetes (não fornecido)
│── dockerfiles/
│   │── Dockerfile.control_center
│   │── Dockerfile.data_processor
│   │── Dockerfile.explorer
│   │── requirements.txt
│── README.md
```

## Como Funciona 🛰️

### 1. Control Center (`control_center.py`)

- API REST em Flask para gerenciar a missão.
- Expõe endpoints:
  - `/` - Verifica se o servidor está rodando.
  - `/metrics` - Exibe métricas do Prometheus.
  - `/status` - Retorna o status da missão.

### 2. Data Processor (`data_processor.py`)

- Periodicamente faz requisições ao Control Center para buscar o status da missão.
- Exibe logs do status atual.

### 3. Explorer (`explorer.py`)

- Periodicamente envia dados para o Control Center.
- Dados enviados incluem ID do explorador, coordenadas e status.

## Execução 🛠️

1. **Usando Docker**:

   ```sh
   docker build -t control-center -f dockerfiles/Dockerfile.control_center .
   docker build -t data-processor -f dockerfiles/Dockerfile.data_processor .
   docker build -t explorer -f dockerfiles/Dockerfile.explorer .

   docker run -d -p 5000:5000 --name control-center control-center
   docker run -d --name data-processor data-processor
   docker run -d --name explorer explorer
   ```

2. **Usando Kubernetes** (se os manifests estiverem disponíveis):
   ```sh
   kubectl apply -f deployment/
   ```

## Tecnologias Utilizadas 🖥️

- Python (Flask, Requests)
- Prometheus para monitoramento
- Docker para conteinerização
- Kubernetes para orquestração (opcional)
