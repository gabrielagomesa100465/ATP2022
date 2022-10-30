import csv
import matplotlib.pyplot as plt
def readDataset(fnome) :
    f = open(fnome, encoding= "utf-8")
    f.readline() 
    csv_reader = csv.reader(f, delimiter = ";")
    obras = []
    for row in csv_reader :
        obras.append(tuple(row))
    return obras 

def pp(obra) :
    print(f'{obra[0][:25]:25} | {obra[4][:30]:30} | {obra[3][:15]:15} | {obra[2][:6]:6}')

def listar_obras(obras):
    print("\n", "Nome                     | Descrição                     | Compositor                     | Ano ")
    print("----------------------------------------------------------------")
    for composição in obras:
        nome,desc,ano,_,compositor,*_ = composição
        print(f" {nome[0:30]:30} | {desc[0:50]:50} | {compositor[0:30]:30} | {ano:14}")


def titAno(obras):
    listaTitAno = []
    for composição in obras:
        nome,_,ano,*_ = composição
        listaTitAno.append((nome,ano))
    listaTitAno.sort()
    print("\n", "Nome             |   Ano")
    print("---------------------------------")
    for partTitAno in listaTitAno:
        nome, ano = partTitAno
        print(f" {nome[0:30]:30} | {ano:14}")
    return()  
    

def titPorAno(obras): 
    listaTitPorAno = []
    for composição in obras :
       nome,_,ano,*_ = composição
       listaTitPorAno.append((ano, nome))
    listaTitPorAno.sort()
    print("-----------------------------------------")
    for partTitAno in listaTitPorAno:
        ano, nome = partTitAno
        print(f" {ano:14} | {nome[0:30]:30}")
    return()

def dicAnoObras(obras):
    dicAnos = {}
    for composição in obras:
        nome,_,ano,*_ = composição
        if ano in dicAnos.keys():
            dicAnos[ano].append(nome)
        else :
            dicAnos[ano] = [nome]
    return dicAnos

def numObras(obras) :
    return len(obras)

def ordenadaCompositor (obras) :
    listaCompositores = []
    for composição in obras:
        _,_,_,_, compositor,_,_ = composição
        if compositor not in listaCompositores:
            listaCompositores.append(compositor)
    listaCompositores.sort()
    print("\n", "Lista de compositores")
    print("-----------------------------------")
    for n in listaCompositores:
        print(" -", n)
    return 

def tabelarDistribuição(distrib):
    print("")
    for par in distrib:
        print(f" {par[0:17]:25} | {distrib[par]}")
    print("")
    return()

def distribuição_período (obras):
    distrib = {}
    for _,_,_,período,_,_,_ in obras:
        intervalo = "[" + str(período) + "]"
        if intervalo in distrib :
            distrib[período] += 1
        else :
            distrib[período] = 1
    return(distrib)

def distribuição_ano(obras):
    distrib = {}
    for _,_,ano,_,_,_,_ in obras:
        intervalo = "[" + str(ano) + "]"
        if intervalo in distrib :
            distrib[ano] += 1
        else :
            distrib[ano] = 1
    return distrib

def distribuição_compositor(obras):
    distrib = {}
    for _,_,_,_,compositor,_,_ in obras:
        intervalo = "[" + str(compositor) + "]"
        if intervalo in distrib :
            distrib[compositor] += 1
        else :
            distrib[compositor] = 1
    return(distrib)

def plotdistrib(distrib):
    plt.bar(distrib.keys(), distrib.values(), color = 'blue')
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.title("Gráfico da distribuição das obras")
    plt.show()
    return
def desenhar_gráficos(obras):
    print("""
    --------------------------------------------------
                    Menu de gráficos
    --------------------------------------------------
    Deseja consultar o gráfico de que distribuição? :
    1- Distribuição das obras por período
    2- Distribuição das obras por ano
    3- Distribuição das obras por compositor
    """)
    opção = input("Introduza a sua opção: ")
    if opção == "1" :
        plotdistrib(distribuição_período(obras))
    elif opção == "2" :
        plotdistrib(distribuição_ano(obras))
    elif opção == "3" :
        plotdistrib(distribuição_compositor(obras))


def tuplCompObras(obras):
    listaTuplos = list(inversão_estrutural(obras).items())
    return listaTuplos

def inversão_estrutural (obras):
    disObrAux = {}
    for título,_,_,_,compositor,*_ in obras:
        if compositor in disObrAux.keys():
            disObrAux[compositor].append(título)
        else :
            disObrAux[compositor] = [título]
    return disObrAux

import obras 
myObras = obras.readDataset("obras.csv")
opção = 1
def menu():
    print("""
    ----------------------------------------------------
                        Menu
    ----------------------------------------------------
    (1) Ler a base de daos 
    (2) Número de obras existentes
    (3) Lista das obras ordenada por ordem alfabética
    (4) Lista das obras ordenada crescentemente por ano
    (5) Lista ordenada dos compositores
    (6) Distribuição das obras por período
    (7) Distribuição das obras por ano
    (8) Distribuição das obras por compositor
    (9) Visualização de gráficos
    (0) Sair)
    """) 



while opção != "0" :
    menu()
    opção = input("Introduza uma opção: ")
    if opção == "1":
        lista = obras.listar_obras(myObras)
    elif opção == "2" :
        contagem = obras.numObras(myObras)
        print("A base de dados tem ", contagem, "obras.")
    elif opção == "3" :
        listaTitAno = obras.titAno(myObras)
        print(listaTitAno)
    elif opção == "4" :
        listaTitPorAno = obras.titPorAno(myObras)
        print(listaTitPorAno)
    elif opção == "5" :
        lcomp = obras.ordenadaCompositor(myObras)
        print(lcomp)
    elif opção == "6" :
        obras.tabelarDistribuição(obras.distribuição_período(myObras))
    elif opção == "7" :
        obras.tabelarDistribuição(obras.distribuição_ano(myObras))
    elif opção == "8" :
        obras.tabelarDistribuição(obras.distribuição_compositor(myObras))
    elif opção == "9" :
        obras.desenhar_gráficos(myObras)
    elif opção == "0" :
        break
    else :
        print("A opção selecionada não é válida")
