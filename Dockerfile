# Usando a imagem oficial do Python
FROM python:3.10

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Variáveis de ambiente para evitar que o Python crie arquivos pyc
ENV PYTHONUNBUFFERED=1

# Copiando o arquivo de dependências para o contêiner
COPY requirements.txt /app/

# Instalando as dependências
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiando o restante do código para dentro do contêiner
COPY . /app/

# Definindo o PYTHONPATH para garantir que os módulos sejam reconhecidos
ENV PYTHONPATH=/app

# Expondo a porta que o Django irá rodar
EXPOSE 8000

# Definindo o comando para rodar o servidor com Daphne
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "av_project.asgi:application"]
