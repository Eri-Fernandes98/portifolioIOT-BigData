FROM python:3.9-slim

WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Porta para o Streamlit
EXPOSE 8501

# Comando para executar o app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]