import matplotlib.pyplot as plt
from alunos import*
dadosuni = alunos.readDataset("alunos.csv")

def menu():
    print("""
    -----------------------------------------
                    Menu
    -----------------------------------------
    (1) Ler a base de dados
    (2) Distribuição dos alunos por curso
    (3) Distribuição dos alunos por escalões
    (4) Visualização de gráficos
    (0) Sair
    -----------------------------------------
    """)

import alunos
opção = "1"
while opção != 0:
    menu()
    opção = input("Introduza uma opção: ")
    if opção == "1" :
        alunos.listar_dados(alunos.media(dadosuni))
    elif opção == "2" :
        alunos.tabelarDistribuição(alunos.distribuição_curso(dadosuni))
    elif opção == "3":
        alunos.tabelarDistribuição(alunos.distribuição_escalão(alunos.media(dadosuni)))
    elif opção == "4":
        alunos.desenhar_gráficos()
    elif opção == "0" :
        break
    else :
        print("A opção selecionada não é válida")

        

