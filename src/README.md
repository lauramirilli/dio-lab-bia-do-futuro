# Passo a Passo de Execução

## Setup do Ollama

```bash
# Instalar Ollama (ollama.com)
# Baixar um modelo leve
ollama pull gpt-oss

# Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas requests

# Garantir que Ollama está rodando
ollama serve

# Rodar o app
streamlit run .\src\app.py
```
