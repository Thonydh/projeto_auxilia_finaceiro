import numpy as np
def redimento(preço):
    if len(preço) < 2 :
        raise ValueError('dados insuficienes para fazer o calculo')
    else:
        preço_atual = preço[0]
        preço_inicial = preço[-1]
        rentabilidade = preço_atual - preço_inicial
        rentabilidade = rentabilidade / preço_inicial
        rentabilidade = rentabilidade * 100
        return f"{rentabilidade:.2f}%"

def  calcular_volatilidade(preco):
    variacao = [(preco[i]-preco[i+1])/preco[i+1] for i in range(len(preco)-1)]
    volatilidade = np.std(variacao)
    return f"{volatilidade:.2f}%"
def drawdonw_maximo(precos):
     
    pico = precos[0]  
    drawdown_max = 0  

    for preco in precos:  
        if preco > pico:  
            pico = preco
        drawdown = (pico - preco) / pico  
        drawdown_max = max(drawdown_max, drawdown)  
    
    return f'{drawdown_max * 100:.2f}% ' 
