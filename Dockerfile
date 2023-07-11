# Imagem base
FROM python:3.10

# Diretório de trabalho
WORKDIR /super_teaching

# Copiar os arquivos do projeto para o diretório de trabalho
COPY . .

# Instalar as dependências do projeto
COPY requirements.txt .
RUN pip install -r requirements.txt

# Executar migrações do banco de dados
RUN python manage.py migrate

# Expôr a porta utilizada pelo servidor do Django
EXPOSE 7000

# Comando para iniciar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]