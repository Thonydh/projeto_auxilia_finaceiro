import requests


def busca_dados_na_api(ticker,api_kay):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_kay}&outputsizer=compact'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "Time Series (Daily)" in data:
            return data
        else:
            raise ValueError('Dados nao encontrados ou ticker não encotrados.')
    else:
        raise ConnectionError("Erro ao conectar com Api")
# def extrair_precos_fechamento(dados):
#     precos_fechamento = []
#     for data_serie, valores in dados["Time Series (Daily)"].items():
#         precos_fechamentos = valores["4. close"]
#         precos_fechamento.append(float(precos_fechamentos))
#     return precos_fechamento
