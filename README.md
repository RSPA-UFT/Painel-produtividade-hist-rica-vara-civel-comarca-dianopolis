# Painel de Produtividade Histórica e IA Estratégica
**Vara Cível e da Fazenda Pública - Comarca de Dianópolis/TO**

Este projeto é um painel de gestão gerencial desenvolvido para o acompanhamento tático e estratégico das métricas processuais da Comarca de Dianópolis (Tribunal de Justiça do Estado do Tocantins - TJTO).

A plataforma unifica visualização de dados via `Chart.js`, Teoria das Filas e modelagem estatística profunda para extrair tendências, gargalos e safras (taxa de congestionamento).

## Estrutura Híbrida do Painel
1. **Frontend Público/Estático (`index.html`)**: Permite hospedagem rápida (Ex: _GitHub Pages_) sem comprometer segurança. Adota estritamente os padrões de Identidade Visual do portal do TJTO.
2. **Backend Local de IA (`server.py`)**: Script em Python desenhado para processamento local de dados (CSV/Excel). Realiza a "ponte" segura entre os dados fechados do gabinete e o modelo de Linguagem Gemini 1.5 Pro da Google. Produz sínteses descritivas e análises de correlação entre métricas processuais diretamente em formato HTML pronto para inserção no painel público.

## Módulos do Sistema
O dashboard é estruturado de forma amigável ao corpo de servidores leigos em ciência de dados e está setorizado em quatro pilares fundamentais:
- **📊 Visão Geral**: Relatório de indicadores primários do ano corrente, superávits e índices comparativos de Acervo e Audiências (Lei Distribuídos x Julgados x Baixados).
- **⏳ Fluxo e Gargalos**: Análise do "Tempo de Espera" (Lei de Little) e capacidade produtiva instalada.
- **🤖 IA Estratégica**: Síntese textual limpa, montada pelo LLM conectado à base histórica de produtividade. Retira do Juiz o peso inferencial manual para entregar diagnósticos imediatos de gargalos setoriais.
- **🧪 Laboratório Técnico**: Bastidores das inferências estocásticas que regem o painel, consolidando todas as provas estatísticas rigorosas utilizadas no projeto.
  - Sazonalidade (Kruskal-Wallis).
  - Correlação (R de Pearson).
  - Tendência de Curto Prazo (Série de Taylor e Regressão Múltipla OLS).
  - Controle de Qualidade de Produção Diária (Cartas de Shewhart).

## Como utilizar a IA Localmente
1. Garanta a criação do ambiente `venv` com as bibliotecas: `pip install fastapi uvicorn google-generativeai pydantic python-dotenv`
2. Construa seu arquivo `.env` na raiz informando a API do Google Studio: `GEMINI_API_KEY=sua_chave`
3. A inicialização da suíte de predição ocorre executando: `python server.py`.

---
*Idealização e Desenvolvimento:* **Rodrigo Perez Araújo** — Juiz de Direito e Diretor do Foro.
