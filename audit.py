import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
if not api_key:
    print("API Key not found.")
    exit(1)

genai.configure(api_key=api_key)
# Using the best available Gemini Pro model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

prompt = f"""
Por favor, aja como um auditor de código sênior de frontend e backend.
O usuário relatou: "há coisas obsoletas não excluídas e erros no meu painel (HTML/JS/CSS)."

Aqui está o código atual do `index.html`:
```html
{html_content}
```

Objetivo da auditoria:
1. Buscar resquícios de funções, variáveis globais ou configurações antigas que não são mais necessárias após a conversão para arquivo "Static Single Page" onde os dados são servidos do python.
2. Identificar quaisquer erros de sintaxe (HTML não fechado, JS corrompido, erros lógicos em Chart.js, etc.).
3. Detectar lixo de layout inútil ou divs duplicadas/inacabadas (ex: configurações de API antiga que ficaram na UI).

Responda em modo texto claro com a lista dos defeitos e as linhas aproximadas ou as funções/variáveis para que eu possa excluí-los/remendá-los imediatamente. Seja extremamente analítico e técnico.
"""

print("Iniciando auditoria via Gemini API...")
try:
    response = model.generate_content(prompt)
    with open("audit_report.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Auditoria concluída com sucesso! (Salvo em audit_report.txt)")
except Exception as e:
    print(f"Erro ao chamar API: {e}")
