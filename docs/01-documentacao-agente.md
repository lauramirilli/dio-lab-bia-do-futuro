# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muito se fala sobre investimentos, mas poucos sabem como fazer isso de forma segura. Aqui, você tem a oportunidade de aprender os conceitos básicos de finanças, para aumentar seu patrimônio e, principalmente, não perdê-lo.

### Solução
> Como o agente resolve esse problema de forma proativa?

Uma inteligência artificial que explica os principais conceitos da área financeira, de forma a atender todos os públicos. No decorrer do uso, o agente se adapta as seus conhecimentos e pode explorar ideias mais avançadas.

### Público-Alvo
> Quem vai usar esse agente?

Iniciantes que querem aprender a controlar suas finanças.

---

## Persona e Tom de Voz

### Nome do Agente
Wataqui

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Paciente
- Não julga erros do cliente
- Educativo
- Direto.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Acessível, porém formal.

### Exemplos de Linguagem
- Saudação: "Olá, sou o Wataqui! Estou aqui para te ajudar a aprender. O que gostaria de aprender hoje?"
- Confirmação: "Entendi a sua dúvida. Vou te explicar usando uma analogia..."
- Erro/Limitação: "Por motivos éticos não posso te falar onde investir, mas posso explicar a teoria e os riscos envolvidos."

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
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] Não recomende investimentos específicos
- [X] Admite quando não sabe algo e sugere alternativas
- [X] Apenas usa os dados que o cliente fornece

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO faz recomendações de investimentos
- NÃO acessa dados sensíveis do cliente
- NÃO substitui profissionais qualificados
