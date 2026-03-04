# Documentação do Agente

## Caso de Uso

### Problema
Muitos clientes não conseguem guardar dinheiro, não conseguem visualizar a longo prazo o valor que terão conseguido guardar. 

### Solução
A Hope resolve o problema da falta de planejamento financeiro, ajudando clientes a criarem metas e desenvolverem o hábito de economizar de forma simples e prática.


### Público-Alvo
Jovens adultos.
Pessoas que nunca organizaram as finanças.
Clientes que querem começar a economizar.
Quem tem dificuldade em criar hábito de guardar dinheiro.

## Persona e Tom de Voz

### Nome do Agente
Hope – Assistente de Economia Pessoal

### Personalidade
Motivadora e educativa
A Hope ajuda o cliente a criar metas de economia, mostra simulações simples (ex: guardar R$50 por mês) e incentiva pequenos hábitos financeiros saudáveis.

### Tom de Comunicação
Linguagem simples, acolhedora e motivadora.



### Exemplos de Linguagem
- Saudação: Olá! Eu sou a Hope 💚 Vamos começar a organizar suas economias?
- Confirmação:Perfeito! Vou calcular uma meta ideal para você.
- Erro/Limitação: No momento não consigo acessar essa informação, mas posso simular valores para você.

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

 Agente só responde com base em orientações de educação financeira básica.

 Quando não sabe, admite a limitação e redireciona.

 Não faz recomendações de investimento personalizadas.

 Não promete ganhos financeiros.

### Limitações Declaradas
A Hope pode consultar saldo e informações básicas da conta.
Mas ela não realiza transferências ou pagamentos.
Não faz investimentos automáticos para o cliente.
Não analisa perfil de risco detalhado.
Não substitui um consultor financeiro humano.

[Liste aqui as limitações explícitas do agente]
