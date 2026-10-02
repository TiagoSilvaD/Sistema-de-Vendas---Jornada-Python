# TITULO - sistemas de vendas
# Secao Cadastrar Vendas    
    # campo data
    # campo vendedor 
    # campo de produto
    # campo quantidade
    # campo valor
    # botao cadastrar venda
# secao vendas cadastradas 
    # tabela com as vendas
# secao dashboard 
    # card/metrica 
    # grafico
    # grafico de pizza

import streamlit as st 
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# secao de cadastro de Vendas 
st.sidebar.write("## Cadastrar Vendas")


data = st.sidebar.date_input("Data")
vendedor =st.sidebar.selectbox("Vendedor", ["ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("produto", ["notebook", "celular", "fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1,)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda Cadastrada com Sucesso")

# secao de visualizar vendas 
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# secao de Dashboard
st.write("## Dashboard")
# card/metrica 
faturamento = tabela_vendas ["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# grafico
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# grafico de pizza
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2)