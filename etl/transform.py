import pandas as pd
from io import StringIO

def markdown_to_dataframe(markdown_path: str) -> pd.DataFrame:
    """
    Converte um arquivo Markdown (resposta do ChatGPT) em DataFrame.
    """
    with open(markdown_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()

    # Remove linha separadora tipo |----|----|
    linhas = markdown_text.strip().split('\n')
    linhas = [linha for linha in linhas if not all(c in "-| " for c in linha.strip())]
    markdown_limpo = '\n'.join(linhas)

    # Converte para DataFrame
    df = pd.read_csv(StringIO(markdown_limpo), sep='|', engine='python', skipinitialspace=True)
    df = df.loc[:, ~df.columns.str.contains("Unnamed")]
    df.columns = df.columns.str.strip()
    df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

    return df


def transform_google_trends(csv_path: str) -> pd.DataFrame:
    """
    Lê o CSV de tendências do Google e retorna um DataFrame limpo.
    """
    df = pd.read_csv(csv_path, parse_dates=["date"])

    # Garante consistência: renomeia colunas com underscore
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

    return df