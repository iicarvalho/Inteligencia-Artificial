import clustering as cl
import plots as pl

# read the data from a file
def readDataSet(name):
    path = 'datasets/' + name
    print(path)
    file = open(path)
    element = ['', []]
    dataSet = []
    for line in file:
        #print('line: ' + line)
        for word in line.split():
        #    print('word: ' + word)
            if(word == 'sample_label'): #ignore the first line
                break
            else:
                if(line.split().index(word) == 0): #capting the name
                    element[0] = word
                else:
                    element[1].append(float(word))  #capting the data
        if(element[0]!=''):
            dataSet.append(element)
        element = ['', []]
    file.close()
    return dataSet

# makes a .clu file
def printPartition(name, partition):
    path = 'outs/' + name
    print(path)
    file = open(path, 'w')
    for each in partition:
        file.write(str(each[0])+' '+str(each[1])+'\n')

    file.close()

# prints the dataSet
def printData(dataSet):
    for data in dataSet:
        print(data)

# builds the list for the .clu
def outPartition(dataSet,partition):
    list = []
    k = 0
    for i in range(len(partition)):
        for each in partition[i]:
            list.append([])
            list[k].append(each)
            list[k].append(i)
            aux = list[k][0]
            list[k][0] = dataSet[aux][0]
            k+=1

    sorted(list, key=lambda index: index[0])
    print(list)
    return list


def main():
    dataSet = []
    nomeArquivo = ''
    while True:
        opcao = int(input('Entre com a opcao:\n[1] - Escolher o arquivo de dados \n[2] - Aplicar kMeans\n[3] - Aplicar Single-Link\n[4] - Aplicar Avg-Link\n[0] - Sair\n'))
        if(opcao == 1):
            oparquivo = int(input('[1] - c2ds1-2sp.txt\n[2] - c2ds3-2g.txt\n[3] - monkey.txt\n'))
            if(oparquivo == 1):
                nomeArquivo = 'c2ds1-2sp.txt'
            elif(oparquivo == 2):
                nomeArquivo = 'c2ds3-2g.txt'
            elif(oparquivo == 3):
                nomeArquivo = 'monkey.txt'
            dataSet = readDataSet(nomeArquivo)
        elif(opcao == 0):
            break
        elif(nomeArquivo == ''):
            print('Nenhum arquivo selecionado.')
        elif(opcao == 2):
            name = nomeArquivo
            nClusters = int(input('Digite a quantidade de clusters: '))
            times = int(input('Digite a quantidade de iteracoes: '))
            partition = cl.kMeans(dataSet,nClusters,times)
            rmkPartition = outPartition(dataSet,partition)
            complete = 'k'+str(nClusters)+'t'+str(times)+'.clu'
            printPartition('kMeans/'+name.replace('.txt', complete), rmkPartition)
            #pl.plotKMeansMonkey(dataSet, rmkPartition)
        elif(opcao == 3):
            name = nomeArquivo
            kMin = int(input('Digite a quantidade minima de clusters: '))
            kMax = int(input('Digite a quantidade maxima de clusters: '))
            partition = cl.singleLink(dataSet, kMin, kMax)
            k = kMax
            for each in partition:
                rmkPartition = outPartition(dataSet,each)
                complete = 'k'+str(k)+'.clu'
                printPartition('singleLink/'+name.replace('.txt', complete), rmkPartition)
                pl.plotSingleLinkMonkey(dataSet, rmkPartition, k)
                k-=1
        elif(opcao == 4):
            kMin = int(input('Digite a quantidade minima de clusters: '))
            kMax = int(input('Digite a quantidade maxima de clusters: '))
            partition = cl.avgLink(dataSet, kMin, kMax)

if __name__ == '__main__':
    main()
