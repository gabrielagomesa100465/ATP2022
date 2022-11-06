import csv
import matplotlib.pyplot as plt

def readDataset(ficheiro) :
    f = open(ficheiro, encoding= "utf-8")
    f.readline() 
    csv_reader = csv.reader(f, delimiter = ";")
    listauni = []
    for row in csv_reader :
        listauni.append(tuple(row))
    return listauni

dadosuni = readDataset("alunos.csv")

def listar_dados(alunos):
    print("-------------------------------------------------------------------------------------------------")
    print("\n", "ID   | Nome                   | Curso       | TPC1 | TPC2 | TPC3 | TPC4 | Média | Escalão ")
    print("-------------------------------------------------------------------------------------------------")
    for aluno in alunos:
        id,nome,curso,tpc1,tpc2,tpc3,tpc4,média,escalão = aluno
        print(f" {id:4} | {nome:30} | {curso:8} | {tpc1:2} | {tpc2:2} | {tpc3:2} | {tpc4:2} | {média:5} | {escalão:7}")
    return()

def distribuição_curso(alunos):
    distrib = {}
    for aluno in alunos:
        _,_,curso,_,_,_,_ = aluno
        if curso in distrib.keys():
            distrib[curso] = distrib[curso] + 1
        else:
            distrib[curso] = 1
    return(distrib)

def media(alunos):
    listamedia = []
    for id,nome,curso,tpc1,tpc2,tpc3,tpc4 in alunos:
        média = (int(tpc1) + int(tpc2) + int(tpc3) + int(tpc4))/4
        if 1<= média <= 4.4:
           aluno = (id,nome,curso,tpc1,tpc2,tpc3,tpc4,média,"E")
        elif 4.5 <= média <= 8.4:
            aluno = (id,nome,curso,tpc1,tpc2,tpc3,tpc4,média,"D")
        elif 8.5 <= média <= 12.4:
            aluno = (id,nome,curso,tpc1,tpc2,tpc3,tpc4,média,"C")
        elif 12.5 <= média <= 16.4:
            aluno = (id,nome,curso,tpc1,tpc2,tpc3,tpc4,média,"B")
        elif 16.5 <= média <= 20:
            aluno = (id,nome,curso,tpc1,tpc2,tpc3,tpc4,média,"A")
        listamedia.append(aluno)
    return listamedia 

def distribuição_escalão(alunos):
    distrib = {}
    for aluno in alunos:
        _,_,_,_,_,_,_,_,escalão = aluno 
        if escalão in distrib.keys():
            distrib[escalão] = distrib[escalão] + 1
        else:
            distrib[escalão] = 1
    return distrib

def plotdistrib(distrib):
    if distrib == distribuição_curso(dadosuni):
        plt.plot(distrib.keys(), distrib.values())
        plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation = 45)
        plt.title("Distribuição dos alunos por curso")
        plt.show()
    elif distrib == distribuição_escalão(media(dadosuni)):
        plt.plot(distrib.keys(), distrib.values())
        plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation = 45)
        plt.title("Distribuição das médias por escalões")
        plt.show()
    return

def desenhar_gráficos():
    print("""
    --------------------------------------------------
                    Menu de gráficos
    --------------------------------------------------
    Deseja consultar o gráfico de que distribuição? :
    1- Distribuição dos alunos por curso
    2- Distribuição dos alunos por escalões
    """)
    opção = input("Introduza a sua opção: ")
    if opção == "1" :
        plotdistrib(distribuição_curso(dadosuni))
    elif opção == "2" :
        plotdistrib(distribuição_escalão(media(dadosuni)))

def tabelarDistribuição(distrib):
    print("")
    for par in distrib:
        print(f" {par:11} | {distrib[par]:4}")
    print("")
    return()

    

