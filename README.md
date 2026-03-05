💚 Hope — Educadora Financeira com IA Generativa
A Hope nasceu da ideia de que educação financeira precisa ser acessível. Ela não é um chatbot de recomendações — é uma agente que conversa, explica e acompanha o cliente no seu ritmo, com base no seu perfil real.

Sobre a Hope
A Hope é uma educadora financeira construída com IA generativa. Ela parte do contexto de cada cliente — patrimônio, objetivos, transações recentes e histórico de atendimentos — para ter conversas que fazem sentido de verdade. Explica conceitos como CDB, CDI e poupança de forma simples, sem jargão e sem pressa.
Ela não recomenda investimentos. Ela educa.

Como funciona
O agente roda localmente com o modelo Mistral via Ollama e usa Streamlit como interface de chat. A cada conversa, o contexto do cliente é montado dinamicamente a partir dos dados em /data, garantindo respostas personalizadas e dentro do escopo financeiro.
Um system prompt com regras claras define os limites da Hope: ela nunca inventa informações, nunca sai do tema e sempre verifica se o cliente entendeu.

Estrutura do repositório
dio-lab-bia-do-futuro/
│
├── data/
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   └── produtos_financeiros.json
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── src/
│   └── app.py
│
└── assets/

Como executar
Pré-requisitos: Python 3.10+ e Ollama instalado.
bashpip install -r requirements.txt
ollama run mistral
streamlit run src/app.py

Documentação
ArquivoConteúdo01-documentacao-agente.mdPersona, caso de uso e arquitetura02-base-conhecimento.mdEstratégia de dados03-prompts.mdSystem prompt e exemplos de interação04-metricas.mdAvaliação e métricas de qualidade05-pitch.mdRoteiro do pitch

Stack

Streamlit — interface do chat
Ollama + Mistral — LLM local
Pandas — leitura e contexto dos dados
Python 3.10+
