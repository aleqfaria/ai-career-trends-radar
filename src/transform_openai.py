import pandas as pd
from io import StringIO

def markdown_to_dataframe(markdown_text: str) -> pd.DataFrame:
    try:
        # Divide o conteúdo em linhas
        linhas = markdown_text.strip().split('\n')

        # Remove linhas que contêm só separadores de Markdown (pipes e traços)
        linhas_filtradas = [
            linha for linha in linhas
            if not all(c in "-| " for c in linha.strip())
        ]

        # Junta novamente as linhas limpas
        markdown_limpado = '\n'.join(linhas_filtradas)

        # Converte em DataFrame
        df = pd.read_csv(StringIO(markdown_limpado), sep='|', engine='python', skipinitialspace=True)

        # Remove colunas automáticas "Unnamed"
        df = df.loc[:, ~df.columns.str.contains("Unnamed")]

        # Limpa nomes de colunas e valores
        df.columns = df.columns.str.strip()
        df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

        return df

    except Exception as e:
        print(f"[Erro] Falha ao converter Markdown em DataFrame: {e}")
        return pd.DataFrame()