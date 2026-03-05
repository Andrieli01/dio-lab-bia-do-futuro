# Passo a Passo de Execução
##Setup do  Ollama
'''bash
#1.Instalar Ollama (ollama.com)
#2.Baixar um modelo leve
ollama run mitral
#3.Testar se funciona
ollama run mistral
'''
##Codigo completo
Todo o código completo está no arquivo 'app.py',


'''

##Como Rodar
'''bash
#1.Instalar dependencias
pip install streamlit pandas requests
#2.Garantir que o Ollama está rodando 
ollama serve
#3.Rodar o app
streamlit run.\src\app.py
'''



## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

