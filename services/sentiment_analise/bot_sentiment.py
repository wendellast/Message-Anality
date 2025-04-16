import json

import requests


def analisar_sentimento(texto):
    """
    Envia um texto para análise de sentimento na API local e retorna apenas o texto da resposta.

    Args:
        texto (str): O texto a ser analisado.

    Returns:
        str: A mensagem de resposta da análise de sentimento.
    """
    # URL do endpoint local
    url = "https://hublast.com/agente-ia/analise-message/"

    # Preparando os dados para envio
    payload = {
        "text": texto
    }

    # Configurando headers
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Fazendo a requisição POST
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        # Verificando se a requisição foi bem-sucedida
        response.raise_for_status()

        # Obtendo o JSON da resposta
        resposta_json = response.json()

        # Retornando apenas o texto da resposta
        return resposta_json["response"]
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {str(e)}"
    except (KeyError, json.JSONDecodeError) as e:
        return f"Erro ao processar resposta: {str(e)}"
