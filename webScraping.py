import pandas as pd
import matplotlib.pyplot as plt
import os

archive = pd.read_csv(
    'IBOVDia_27-06-25.csv',
    encoding='latin-1',
    sep=';',
    skiprows=1,
    usecols=range(5)
) # Lê o arquivo CSV gerado no site público da B3

archive.columns = ['Codigo', 'Acao', 'Tipo', 'Qtde_Teorica', 'Part (%)']
archive['Part (%)'] = archive['Part (%)'].str.replace(',', '.', regex=False).astype(float) #Converte os dados da participação para float 

ibov = archive.sort_values("Part (%)", ascending=False) # Ordem decrecente pela participação
top10 = ibov.head(10) # Seleciona as top 10 ações com maior participação

def plotar_grafico():
    plt.figure(figsize=(8, 10))
    plt.pie(top10["Part (%)"], labels=top10["Codigo"], autopct="%1.1f%%", startangle=140)
    plt.title("Top 10 Ações na Carteira Teórica do IBOV 27/06/2025")
    plt.axis('equal') 
    plt.show()

def menu():
    S = 0
    while S == 0:
        
        print("\nMenu:")
        resposta = input("1 - Ver Top 10 Ações\n2 - Ver Gráfico\n3 - Sair\nEscolha uma opção: ")
        
        match resposta:
            case "1":
                os.system('cls')
                print("Top 10 Ações com mais participação na Carteira Teórica do IBOV 27/06/2025:")
                print(top10)
            case "2":
                os.system('cls')
                print("Gerando gráfico...")
                print("Top 10 Ações com mais participação na Carteira Teórica do IBOV 27/06/2025:")
                plotar_grafico()
            case "3":
                os.system('cls')
                print("Saindo...")
                S = 1
            case _:
                print("Opção inválida. Tente novamente.")

menu()
    
        