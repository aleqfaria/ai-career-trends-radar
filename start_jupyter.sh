#!/bin/bash

# Caminho para o ambiente virtual (ajustado para 'venv' dentro da pasta atual)
ENV_DIR="./venv"

# Verifica se o ambiente virtual já está ativado
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Ambiente virtual já está ativado."
else
    echo "Ativando o ambiente virtual..."
    source "$ENV_DIR/bin/activate"
fi

# Inicia o Jupyter Notebook
echo "Iniciando Jupyter Notebook..."
jupyter notebook --no-browser --ip=127.0.0.1
