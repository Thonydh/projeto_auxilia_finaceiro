import api
from calculos import redimento, calcular_volatilidade,drawdonw_maximo
Api_Key = '9IZKALK83MT3S0T5'

def main():
    #ticker = input('digite o ticker da ação (exemplo: IBM):')
    ticker = 'PETR4.SA'
    
    try:
        preco = []
        dado =  api.busca_dados_na_api(ticker,Api_Key)
        for data_serie, valores in dado['Time Series (Daily)'].items():
            preço_de_fechamento = valores['4. close']
            preco.append(float(preço_de_fechamento))
        r = redimento(preco)    

        print(calcular_volatilidade(preco))
        print(drawdonw_maximo(preco))
        print(r)
        print(preco)
    except:
        print('Ocoreu um erro')
    
if __name__ == '__main__':
    main()