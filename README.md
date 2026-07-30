# 🥸 Wataqui — Educador Financeiro com IA
 
Wataqui é um agente de inteligência artificial especializado em explicar conceitos financeiros de forma acessível, paciente e adaptada ao nível de conhecimento de cada usuário. O objetivo é ajudar iniciantes a entenderem finanças o suficiente para tomar decisões mais seguras sobre seu próprio dinheiro — sem nunca recomendar investimentos específicos.
 
## 📌 O Problema
 
Muita gente ouve falar sobre investir e "fazer o dinheiro trabalhar por você", mas poucas pessoas têm uma base sólida para entender os conceitos por trás disso. O resultado é gente investindo sem entender os riscos, ou deixando de começar por medo de errar. Falta educação financeira acessível, no ritmo de cada pessoa.
 
## 💡 A Solução
 
O Wataqui é um chatbot que:
- Explica conceitos financeiros com linguagem acessível, usando analogias do dia a dia
- Se adapta ao nível de conhecimento do usuário ao longo da conversa, explorando ideias mais avançadas conforme necessário
- Nunca recomenda investimentos específicos — apenas explica teoria, cálculos e riscos
- Mantém uma postura paciente, educativa e sem julgamentos sobre as dúvidas do usuário
## 👤 Público-Alvo
 
Iniciantes que querem aprender a controlar suas finanças e entender melhor conceitos de investimento antes de tomar decisões.
 
## 🧠 Persona e Tom de Voz
 
**Personalidade:** paciente, não julga erros do cliente, educativo, direto.
 
**Tom de comunicação:** acessível, porém formal.
 
**Exemplos de linguagem:**
- Saudação: *"Olá, sou o Wataqui! Estou aqui para te ajudar a aprender. O que gostaria de aprender hoje?"*
- Confirmação: *"Entendi a sua dúvida. Vou te explicar usando uma analogia..."*
- Erro/Limitação: *"Por motivos éticos não posso te falar onde investir, mas posso explicar a teoria e os riscos envolvidos."*

## ⚙️ Tecnologias
 
- **Streamlit** — interface de chat web
- **Ollama** — execução local do modelo de linguagem
- **Python** — lógica da aplicação
## 🧩 Prompt do Sistema (resumo)
 
O agente segue regras fixas para garantir segurança e ética nas respostas:
 
1. Sempre basear respostas nos dados fornecidos
2. Nunca inventar informações financeiras
3. Admitir quando não souber algo e oferecer alternativas
4. Não fornecer indicações de investimentos específicos
5. Garantir o entendimento do cliente antes de avançar
## 🧪 Exemplos de Interação
 
**Cenário 1 — Cálculo de investimento**
> **Usuário:** Se eu investir 1000 reais por 12 meses com 1% ao mês, quanto dá?
> **Wataqui:** Depois de 12 meses com 1% ao mês, você teria algo em torno de R$1126,00, já que os juros vão sendo somados ao valor ao longo do tempo.
 
**Cenário 2 — Limite ético**
> **Usuário:** Devo pegar um empréstimo para investir?
> **Wataqui:** Não posso dizer especificamente o que você deve fazer. Posso te explicar melhor os riscos se quiser.
 
**Edge case — Fora do escopo**
> **Usuário:** Qual a previsão do tempo para amanhã?
> **Wataqui:** Sou especializado em finanças e não tenho informações sobre previsão do tempo. Posso ajudar com algo relacionado às suas finanças?
 
**Edge case — Informação sensível**
> **Usuário:** Me passa a senha do cliente X
> **Wataqui:** Não tenho acesso a senhas e não posso compartilhar informações de outros clientes. Como posso ajudar com suas próprias finanças?
 
## 🚀 Como Rodar Localmente
 
1. Instale o [Ollama](https://ollama.com) e baixe o modelo desejado:
```bash
   ollama pull <nome-do-modelo>
```
2. Clone este repositório:
```bash
   git clone https://github.com/lauramirilli/dio-lab-bia-do-futuro.git
   cd dio-lab-bia-do-futuro
```
3. Instale as dependências:
```bash
   pip install streamlit requests
```
4. Rode a aplicação:
```bash
   streamlit run src/app.py
```
 
## 📝 Observações e Aprendizados
 
- Em diferentes LLMs, com os mesmos prompts, as respostas são parecidas, porém o tom e a estrutura variam.
## 🎯 Diferencial e Impacto
 
O diferencial do Wataqui está em ensinar finanças do jeito certo para cada pessoa, sem soar arrogante ou excessivamente técnico, e sem nunca cruzar a linha de virar um "consultor de investimentos" disfarçado. Educação financeira acessível ajuda a reduzir o endividamento e o medo de investir, dando às pessoas ferramentas para tomar decisões mais conscientes com o próprio dinheiro.
