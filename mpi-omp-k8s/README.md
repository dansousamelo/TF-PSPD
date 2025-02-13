# MPI-OMP Space Exploration 🚀

## Descrição

Este projeto simula uma exploração espacial distribuída utilizando **MPI (Message Passing Interface)** e **OpenMP**. Cada sonda espacial (processo MPI) explora um planeta aleatório e coleta dados com múltiplas câmeras (threads OpenMP).

## Estrutura do Projeto

```
mpi-omp-space-exploration/
│── Dockerfile                   # Configuração para execução em contêiner
│── mpi-omp-deployment.yaml       # Arquivo de deployment para Kubernetes
│── README.md                     # Documentação do projeto
│── space_exploration.c            # Código-fonte principal
```

## Como Funciona 🛰️

- O código inicializa **MPI** para distribuir processos que representam sondas espaciais.
- Cada sonda escolhe aleatoriamente um planeta entre **Marte, Vênus, Júpiter, Saturno e Netuno**.
- **OpenMP** é utilizado para simular múltiplas câmeras coletando dados simultaneamente.
- As informações coletadas incluem:
  - **Temperatura**
  - **Níveis de radiação**
  - **Presença de minerais**
- Os dados são exibidos no terminal conforme cada sonda processa suas informações.

## Execução 🛠️

### 1. Compilar o código

```sh
mpicc -fopenmp -o space_exploration space_exploration.c
```

### 2. Executar localmente

```sh
mpirun -np 4 ./space_exploration
```

Onde `-np 4` indica o número de processos (sondas) a serem simulados.

### 3. Usando Docker

```sh
docker build -t mpi-omp-space-exploration .
docker run --rm mpi-omp-space-exploration
```

### 4. Usando Kubernetes

Se houver um cluster Kubernetes disponível, o deployment pode ser aplicado:

```sh
kubectl apply -f mpi-omp-deployment.yaml
```

## Tecnologias Utilizadas 🖥️

- **C (MPI + OpenMP)** para execução paralela
- **Docker** para conteinerização
- **Kubernetes** para orquestração

## Exemplo de Saída

```
🚀 Sonda 0 está explorando o planeta Marte! 🌍
📡 [Sonda 0 - Câmera 0] Planeta: Marte | Temp: -23.45°C | Radiação: 2.78 | Minerais: 45.89%
📡 [Sonda 0 - Câmera 1] Planeta: Marte | Temp: -12.30°C | Radiação: 3.45 | Minerais: 50.23%
...
```
