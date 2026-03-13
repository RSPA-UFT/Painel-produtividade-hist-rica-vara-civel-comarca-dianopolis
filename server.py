import os
import json
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Painel de Produtividade Judicial - Backend")

# Setup Gemini
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("WARNING: GOOGLE_API_KEY not found in .env file")
else:
    genai.configure(api_key=api_key)

# Initialize templates
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/analyze")
async def analyze_data(data: dict):
    if not os.getenv("GOOGLE_API_KEY"):
        raise HTTPException(status_code=500, detail="Gemini API Key not configured.")
    
    try:
        # Construct the prompt
        prompt = f"""
        Como um Especialista em Ciência de Dados Aplicada ao Direito e Gestão Judiciária, 
        analise os dados de produtividade abaixo para uma Vara Cível e de Fazenda Pública.
        
        OBJETIVO: Fornecer uma SÍNTESE GERENCIAL EXTRUTURADA. 
        REGRAS CRÍTICAS: 
        1. NÃO recomende ações ou providências (o magistrado decidirá as ações).
        2. Foque em identificar padrões, tendências, anomalias e gargalos técnicos.
        3. Use linguagem técnica de gestão (indicadores, fluxos, Teoria das Filas).
        4. Destaque pontos de atenção onde os dados mostram desvios de estabilidade.
        
        DADOS:
        {json.dumps(data, indent=2)}
        
        6. O tom deve ser de consultoria estratégica para um magistrado.
        7. Responda em Português Brasileiro.
        """
        
        response = model.generate_content(prompt)
        return {"analysis": response.text}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
