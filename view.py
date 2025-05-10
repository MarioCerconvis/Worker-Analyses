import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import answers as ans

# Configuração da página
st.set_page_config(page_title="Análise de Colaboradores", page_icon="📊", layout="wide")
sns.set_style("whitegrid")

st.title("📊 Análise de Colaboradores - IEL")

# Carregamento dos dados
a1 = pd.DataFrame(ans.biggest_salaries())
a2 = pd.DataFrame(ans.lowest_salaries())
a3 = pd.DataFrame(ans.unique_jobs()[0])
a4 = pd.DataFrame(ans.avg_sal_per_role(), columns=["Cargo", "Salário Médio"])
a5 = pd.DataFrame(ans.highest_salaries_employees(), columns=["Nome", "Cargo", "Salário"])

# Métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Maior Salário", f"R$ {a1.iloc[0,0]:,.2f}")
col2.metric("Menor Salário", f"R$ {a2.iloc[0,0]:,.2f}")
col3.metric("Quantidade de Cargos", f"{len(a3)}")

# Abas de navegação
tab1, tab2, tab3 = st.tabs(["📋 Tabelas", "📈 Visuais", "⬇️ Relatório Excel"])

# === TABELAS ===
with tab1:
    st.subheader("Cargos Registrados")
    st.dataframe(a3, use_container_width=True)

    st.subheader("Top 5 Maiores Salários")
    st.dataframe(a1, use_container_width=True)

    st.subheader("Top 5 Menores Salários")
    st.dataframe(a2, use_container_width=True)

    st.subheader("Média Salarial por Cargo")
    st.dataframe(a4, use_container_width=True)

    st.subheader("Colaboradores com Maior Salário por Cargo")
    st.dataframe(a5, use_container_width=True)

# === GRÁFICOS ===
with tab2:
    st.subheader("Média Salarial por Cargo")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=a4, x="Salário Médio", y="Cargo", palette="Blues_d", ax=ax1)
    ax1.set_title("Média Salarial por Cargo")
    ax1.set_xlabel("Salário Médio (R$)")
    ax1.set_ylabel("Cargo")
    st.pyplot(fig1)

    st.subheader("Colaboradores com Maior Salário por Cargo")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=a5, x="Salário", y="Nome", hue="Cargo", dodge=False, ax=ax2)
    ax2.set_title("Funcionários com Maior Salário")
    ax2.set_xlabel("Salário (R$)")
    ax2.set_ylabel("Colaborador")
    st.pyplot(fig2)

# === EXPORTAÇÃO ===
with tab3:
    st.subheader("Exportar Análise Completa (Excel)")

    def gerar_excel():
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            a1.to_excel(writer, index=False, sheet_name='Maiores Salários')
            a2.to_excel(writer, index=False, sheet_name='Menores Salários')
            a3.to_excel(writer, index=False, sheet_name='Cargos')
            a4.to_excel(writer, index=False, sheet_name='Média por Cargo')
            a5.to_excel(writer, index=False, sheet_name='Top por Cargo')
        output.seek(0)
        return output

    excel_file = gerar_excel()
    st.download_button(
        label="📥 Baixar Relatório em Excel",
        data=excel_file,
        file_name='analise_colaboradores.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
