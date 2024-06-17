# Usar uma imagem base do OpenJDK
FROM openjdk:11-jdk-slim

# Instalar Python e Jupyter Notebook
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install jupyter && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar PySpark
RUN pip3 install pyspark

# Definir diretório de trabalho
WORKDIR /app

# Copiar o script Python para o contêiner (opcional)
COPY app.py /app/app.py

# Expor a porta do Jupyter Notebook
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
