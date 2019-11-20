# clustering.py
from math import sqrt
import numpy as np
import random

# calculate and return the eucludian distance between 2 points
def euclidian(v1,v2):
    dist = 0.0
    for x in range(len(v1)):
        dist += pow((v1[x] - v2[x]),2)
    eucli = sqrt(dist)
    return eucli

# gets the range between each attr of the datasets
# returns a list of lists of min and max range of each attr
def getRanges(dataSet):
    all = []
    ranges = []
    for i in range(len(dataSet[0][1])):
        all.append([])
        for j in range(len(dataSet)):
            all[i].append(dataSet[j][1][i])
    #ranges = [(min([row[i] for row in dataSet]),
    #           max([row[i] for row in dataSet]))
    #           for i in range(len(dataSet[1]))]
    for each in all:
        ranges.append([min(each), max(each)])
    return ranges

# get the first centroids randomly
def getCentroids(nClusters, ranges):
    centroids = []
    for i in range(nClusters):
        centroids.append([])
        for each in ranges:
            #random between min and max of each and add in centroids[i]
            centroids[i].append(round(random.uniform(each[0], each[1]), 4))
    return centroids

# assigment the data to each centroid
def setAssignments(centroids, dataSet):
    assigments = []
    index = 0
    for i in range(len(centroids)):
        assigments.append([])
    for each in dataSet:
        c = 0
        distance = euclidian(each[1],centroids[0])
        print('a distancia do centroid 0 e '+str(distance))
        for i in range(1,len(centroids)):
            distanceAux = euclidian(each[1],centroids[i])
            print('a distancia do centroid '+str(i)+' e '+str(distanceAux))
            if distance > distanceAux:
                distance = distanceAux
                c = i
        assigments[c].append(index)
        index+=1

    return assigments

# re-calculate the centroids only after the first assigment
def remakeCentroids(dataSet, centroids, assigments):
    listAux = []

    for i in range(len(centroids[0])):
        listAux.append(0)

    for i in range(len(assigments)):
        for j in range(len(assigments[i])):
            print('dataset assigments: ')
            print(dataSet[assigments[i][j]][1])
            listAux = np.add(listAux, dataSet[assigments[i][j]][1])
        print('Lista aux: ')
        print(listAux)
        print('assigments[i]: ')
        print(assigments[i])
        if len(assigments[i]) != 0:
            newCentroid = [x / (len(assigments[i])) for x in listAux]
            listAux = []
            for k in range(len(centroids[0])):
                listAux.append(0)
            centroids[i] = newCentroid.copy()
    return centroids

# create the distance matrix
def setMatrix(dataSet):
    matrix = []
    for i in range(len(dataSet)):
        matrix.append([])
        for j in range(i+1):
            matrix[i].append(round(euclidian(dataSet[i][1],(dataSet[j][1])),4))
    return matrix

# returns the position of the minor value of the matrix
def getMinor(matrix):
    low = 0
    pos = [0,0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0 and (matrix[i][j] < low or low == 0):
                low = matrix[i][j]
                pos[0] = i
                pos[1] = j
    matrix[pos[0]][pos[1]] = -1
    return pos

# creates a initial partition with len(dataSet) clusters
def setPart(dataSet):
    part = []
    for i in range(len(dataSet)):
        part.append([i])
    return part

# group the clusters by the closiest object
def groupObjects(part, minorPos):
    aux = []
    times = 0
    for i in range(len(part)):
        for j in range(len(part[i])):
            if part[i][j] == minorPos[0] or part[i][j] == minorPos[1]:
                aux.append(i)
                times += 1
                if times >= 2:
                    break
    print("aux")
    print(aux)
    if aux[0] != aux[1]:
        part[aux[0]] = list(set().union(part[aux[0]],part[aux[1]]))
        del part[aux[1]]
    #print("teste")
    #print(teste)

# kMeans Algorithm
# in: kMeans(dataSet[], nClusters, times)
#     A data set with item name and its attributes -> ['', []]
#     Number of clusters -> nClusters
#     Number of iterations -> times
# out: a list of the partition
def kMeans(dataSet, nClusters, times):
    ranges = getRanges(dataSet)
    for i in range(len(ranges)):
        print('Atributo '+ str(i+1) +' possui min e max: ' + str(ranges[i][0])+ ' e ' + str(ranges[i][1]))
    centroids = getCentroids(nClusters, ranges)
    print('Os centroides iniciais sao: ')
    for each in centroids:
        print(each)
    newAssignments = setAssignments(centroids, dataSet)
    print('As atribuicoes a cada centroide sao: ')
    for each in newAssignments:
        print(each)
    #for i in range(times):
    #print('Assignments: ')
    #print(newAssignments)
    for i in range(times):
        print('Recalculando pela ' + str(i) + ' vez.')
        centroids = remakeCentroids(dataSet,centroids,newAssignments)

        print('Os novos centroides iniciais sao: ')
        for each in centroids:
            print(each)
        oldAssignments = newAssignments.copy()
        newAssignments = setAssignments(centroids, dataSet)
        if(oldAssignments == newAssignments):
            print('Parou pois os centroides nao mudam.')
            break
        print('As novas atribuicoes a cada centroide sao: ')
        for each in newAssignments:
            print(each)


    print(centroids)
    print(newAssignments)
    return newAssignments
    #print(centroids)

    #for each in assigments:
    #    print(each)

# Single Link Algorithm
# in: singleLink(dataSet[], kMin, kMax)
#     A data set with item name and its attributes -> ['', []]
#     maximum cuts on dendogram  -> kMax
#     minimum cuts on dendogram -> kMin
# out: a file .clu of each k partition
def singleLink(dataSet, kMin, kMax):
    partR = []
    distanceMatrix = setMatrix(dataSet)
    '''
    print("a matriz de distancias: ")
    for each in distanceMatrix:
        print(each)
    '''
    partition = setPart(dataSet)
    '''
    print("particao: ")
    print(partition)
    '''
    while(len(partition) > kMin):
        minor = getMinor(distanceMatrix)
        '''
        print("menor valor se encontra em: ")
        print(minor)
        print("a matriz de distancias 2: ")

        for each in distanceMatrix:
            print(each)
        '''
        groupObjects(partition, minor)
        print("particao apos group: ")
        print(partition)
        if len(partition) <= kMax:
            if partition not in partR:
                partR.append(partition.copy())
    '''
    for each in partR:
        print(each)
    '''
    return partR

def distAvgLink(eachf,eachs,info):
    fa = info[eachf][0]
    sa = info[eachs][0]
    fb = info[eachf][1]
    sb = info[eachs][1]
    dist = euclidian([fa,sa], [fb,sb])
    return dist


def media(fcl, scl, info):
    tf = len(fcl)
    ts = len(scl)
    aux = 0
    for eachf in fcl:
        for eachs in scl:
            aux = aux + distAvgLink(eachf,eachs,info)
    return aux / (tf * ts)

def groupAvgLink(fcluster, scluster, partition):
    partition[scluster].extend(partition[fcluster])
    del partition[fcluster]

def minorAvgLink(distanceMatrix):
    min_i = min_j = 0
    minor = 100000
    tam = len(distanceMatrix)
    for i in range(tam):
        for j in range(tam):
            if (i > j) and (distanceMatrix[i][j] < minor):
                minor = distanceMatrix[i][j]
                min_i = i
                min_j = j
    return [min_i, min_j]

def avgLink(dataSet, kMin, kMax):
    info = {}
    partition = []
    tam = 0
    for each in dataSet:
        #print(each[1][0])
        #print(each[1][1])
        #print(each[1][2])
        info.update({each[0]: [each[1][0],each[1][1]]})
        partition.append([each[0]])

    for each in info:
        print(each)

    while len(partition) > kMin:
        tam = len(partition)
        distanceMatrix = [
            [media(partition[i],partition[j],info) if i > j else 0 for j in range(tam)] for i in range(tam)
        ]
        minor = minorAvgLink(distanceMatrix)
        groupAvgLink(minor[0], minor[1], partition)
        print(tam)
        if len(partition) == kMax:
            arquivo_saida = open('k' + str(kMax) + ".clu", "w")
            for cluster in partition:
                for objeto in cluster:
                    arquivo_saida.write(objeto + " " + str(partition.index(cluster)) + "\n")
            kMax = kMax - 1
