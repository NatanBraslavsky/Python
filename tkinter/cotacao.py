import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_disc = requisicao.json()

    cotacao_dolar = requisicao_disc['USDBRL']['bid']
    cotacao_euro = requisicao_disc['EURBRL']['bid']
    cotacao_btc = requisicao_disc['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    print(texto)

pegar_cotacoes()
    
janela = Tk()
janela.title("Cotação Atual das Moedas")

texto_orientacao = Label(janela, text='Clique no botão para exibir as cotações das moedas')
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Buscar cotações Dólar/Euro/BTC", command=pegar_cotacoes)
botao.grid(column=0, row=1)

janela.mainloop()
