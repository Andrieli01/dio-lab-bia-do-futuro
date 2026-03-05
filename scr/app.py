import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "mistral"

# ========= CARREGAR DADOS =========
perfil = json.load(open('./data/perfil_investidor.json', encoding='utf-8'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json', encoding='utf-8'))

# limitar tamanho para evitar erro 500
transacoes = transacoes.head(5)
historico = historico.head(5)

# ========= PROMPT DO SISTEMA =========
SYSTEM_PROMPT = """
Você é a Hope, uma educadora financeira paciente e didática.

Objetivo: ajudar clientes a desenvolver o hábito de economizar e entender
opções simples de investimento como CDB, CDI e poupança.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se a pergunta estiver fora do tema finanças pessoais, diga que está fora do seu escopo
4. Nunca recomende investimentos específicos, apenas explique opções
5. Use linguagem simples e educativa
6. Sempre pergunte se o cliente entendeu
"""

# ========= CONTEXTO =========
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

# ========= FUNÇÃO PERGUNTAR =========
def perguntar(msg):

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

PERGUNTA DO CLIENTE:
{msg}

RESPOSTA DA HOPE:
"""

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        resposta.raise_for_status()
        dados = resposta.json()

        if "response" in dados:
            return dados["response"]

        return "Não consegui gerar uma resposta agora."

    except Exception as e:
        return f"Erro na conexão: {e}"

# ========= INTERFACE =========
st.title("💚 Hope - Sua Educadora Financeira")

if pergunta := st.chat_input("Faça uma pergunta sobre finanças..."):

    st.chat_message("user").write(pergunta)

    with st.spinner("Hope está pensando..."):
        resposta = perguntar(pergunta)

    st.chat_message("assistant").write(resposta)