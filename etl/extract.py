from pytrends.request import TrendReq
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI
from io import StringIO
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
# Carrega variáveis de ambiente
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Inicializa o cliente OpenAI
client = OpenAI(api_key=api_key)

def extract_google_trends(output_path: str = "data/google_trends_ai_jobs.csv"):
    pytrends = TrendReq(hl="en-US", tz=360)

    keywords = [
        "data engineer", "data engineering", "big data engineer", 
        "ai engineer", "machine learning"
    ]

    pytrends.build_payload(keywords, cat=0, timeframe="today 12-m", geo="US", gprop="")
    data = pytrends.interest_over_time()

    if "isPartial" in data.columns:
        data = data.drop(columns="isPartial")

    print("[Google Trends] Dados extraídos:")
    print(data.head())

    data.to_csv(output_path)
    return data

def extract_chatgpt_insights(output_path: str = "data/insights_openai_raw.md"):
    prompt = """
    Liste as 10 profissões emergentes mais promissoras em Inteligência Artificial para os próximos 3 anos. 
    Para cada profissão, inclua:
    - Nome do cargo
    - Breve descrição
    - Principais habilidades exigidas
    - Tecnologias mais utilizadas
    - Setores com maior demanda

    Responda no formato de tabela Markdown.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000
    )

    markdown_text = response.choices[0].message.content

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)

    print("[OpenAI] Markdown salvo em:", output_path)
    return output_path