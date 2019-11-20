from os import listdir
from os.path import isfile, join
from sklearn import metrics

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


def readReal(nome):
    file = open(nome)
    partition = []
    for i in range(0,12):
        partition.append([])
    for line in file:
        aux = line.split()
        partition[int(aux[1])].append(aux[0])
    file.close()
    return partition

def getFiles(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


def main():
    monkeyReal = []
    c2ds12spReal = []
    c2ds32gReal = []
    monkeyReal = readReal('outs/real/monkeyReal1.clu')
    c2ds32gReal = readReal('outs/real/c2ds3-2gReal.clu')
    c2ds12spReal = readReal('outs/real/c2ds1-2spReal.clu')
    path = 'backup/clu/singleLink/'
    #path = 'datasets/clu/'
    myf = getFiles(path)
    for each in myf:
        partition = readReal(path + each)
        print(partition)
        aux = input()
        if each[:5] == 'c2ds1':
            print(each + ': '+str(metrics.adjusted_rand_score(c2ds12spReal, partition)))
        elif each[:5] == 'c2ds3':
            print(each + ': '+str(metrics.adjusted_rand_score(c2ds32gReal, partition)))
        elif each[:6] == 'monkey':
            print(each + ': '+str(metrics.adjusted_rand_score(monkeyReal, partition)))
        aux = input()    
if __name__ == '__main__':
    main()
