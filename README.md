# BigData - at3

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white"/>
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Apache%20Spark-FDEE21?style=for-the-badge&logo=apachespark&logoColor=black"/>
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white"/>
  <img src="https://img.shields.io/github/license/wectornanime/safezone-mobile.svg?style=for-the-badge" />
  <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/>
</div>

### Tópicos

:small_blue_diamond: [Descrição do projeto](#descrição-do-projeto-)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos-)

:small_blue_diamond: [Como rodar a aplicação](#como-rodar-a-aplicação-️)

:small_blue_diamond: [Link do dataset](https://www.kaggle.com/datasets/bordanova/2023-us-civil-flights-delay-meteo-and-aircraft)

## Descrição do projeto 📝

O projeto constitui em uma análise exploratória em um dataset do Kaggle realizado como atividade da faculdade de Análise e desenvolvimento de sistemas na cadeira de BigData.

## Pré-requisitos ✅

:warning: [Docker](https://www.docker.com/)

## Como rodar a aplicação 🕹️

### Clone o projeto

Primeiro faça o clone do projeto com o seguinte comando:

```
git clone https://github.com/Wectornanime/big-data-at3.git
```

### Crie a imagem docker

Depois, acesse a pasta onde o projeto foi clonado, e crie a imagem docker com o seguinte comando:

```
docker build -t pyspark-app .
```

### Inicie o container Docker

Para rodar a aplicação será necessário executar o container, execute o comando de acordo com o seu sistema operacional:

- Linux/Mac

```
docker run -p 8888:8888 -v $(pwd):/app pyspark-app
```

- Windows(CMD)

```
docker run -p 8888:8888 -v %cd%:/app pyspark-app
```

- Windows(Powershell)

```
docker run -p 8888:8888 -v ${PWD}:/app pyspark-app
```

> Após executar o comando, você deve ver a saída indicando que o Jupyter Notebook foi iniciado. A saída incluirá algo como:
> ```
> To access the notebook, open this file in a browser:
>     file:///root/.local/share/jupyter/runtime/nbserver-1-open.html
> Or copy and paste one of these URLs:
>     http://0.0.0.0:8888/?token=YOUR_TOKEN_HERE
> ```

### Execute o Jupyter

Você pode executar o Jupyter pelo VsCode

#### Instale as extensões necessárias

- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

#### Conecte o notebook com o container

Com o jupyter aberto, mude o kernel para o container docker

## Licença ⚖️

The [MIT License](./LICENSE) (MIT)

Copyright :copyright: 2024
