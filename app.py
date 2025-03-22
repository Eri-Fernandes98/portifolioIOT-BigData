import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuração do banco de dados Supabase
DB_URL = "postgresql://postgres:Pm3uTf4ULYZ5XBNo@db.zhadrlbzktdchvbroduw.supabase.co:5432/postgres"
engine = create_engine(DB_URL)

# Função para carregar dados do banco de dados
def load_data(view_name):
    try:
        with engine.connect() as conn:
            df = pd.read_sql(f"SELECT * FROM {view_name}", conn)
            return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados da view {view_name}: {e}")
        return pd.DataFrame()

# Título do dashboard
st.title("Dashboard de Temperaturas IoT")

# Gráfico 1: Média de temperatura por dispositivo
st.header("Média de Temperatura por Dispositivo")
df_avg_temp = load_data("avg_temp_por_dispositivo")
st.write("Dados carregados - Média de Temperatura por Dispositivo:", df_avg_temp)  # Depuração

if not df_avg_temp.empty:
    fig1 = px.bar(df_avg_temp, x="device_id", y="avg_temp", title="Média de Temperatura por Dispositivo")
    st.plotly_chart(fig1)
else:
    st.warning("Nenhum dado disponível para 'avg_temp_por_dispositivo'.")

# Gráfico 2: Contagem de leituras por hora
st.header("Leituras por Hora do Dia")
df_leituras_hora = load_data("leituras_por_hora")
st.write("Dados carregados - Leituras por Hora:", df_leituras_hora)  # Depuração

if not df_leituras_hora.empty:
    fig2 = px.line(df_leituras_hora, x="hora", y="contagem", title="Leituras por Hora")
    st.plotly_chart(fig2)
else:
    st.warning("Nenhum dado disponível para 'leituras_por_hora'.")

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header("Temperaturas Máximas e Mínimas por Dia")
df_temp_max_min = load_data("temp_max_min_por_dia")
st.write("Dados carregados - Temperaturas Máx/Mín:", df_temp_max_min)  # Depuração

if not df_temp_max_min.empty:
    df_temp_max_min["data"] = pd.to_datetime(df_temp_max_min["data"])  # Converter para datetime
    fig3 = px.line(df_temp_max_min, x="data", y=["temp_max", "temp_min"], title="Temperaturas Máximas e Mínimas")
    st.plotly_chart(fig3)
else:
    st.warning("Nenhum dado disponível para 'temp_max_min_por_dia'.")


