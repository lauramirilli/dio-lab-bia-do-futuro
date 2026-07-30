import json
import pandas as pd
import requests
import streamlit as st

# CONFIGURAÇÃO
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# CARREGAR DADOS
perfil = json.load(open('./data/perfil_investidor.json'))
produtos = json.load(open('./data/produtos_financeiros.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')


# MONTAR CONTEXTO
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# SYSTEM PROMPT
SYSTEM_PROMPT = """
Você é um agente financeiro inteligente chamado Wataqui especializado em explicar os principais conceitos da área financeira, de forma a atender todos os públicos. No decorrer do uso, você se adapta as seus conhecimentos e pode explorar ideias mais avançadas.
Seu objetivo é ajudar o cliente a atingir a sua meta, explicando como ele pode fazer isso.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Não forneça indicações de investimentos específicos
5. Garanta o entendimento do cliente
"""

# CHAMAR OLLAMA

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# INTERFACE
st.title("Wataqui, seu educador financeiro 🥸")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))