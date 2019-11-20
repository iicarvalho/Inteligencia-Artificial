import matplotlib.pyplot as plt
'''
import sys

year = [1960, 1970, 1980, 1990, 2000, 2010]
pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]

plt.plot(year, pop_pakistan, color='g')
plt.plot(year, pop_india, color='orange')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('Pakistan India Population till 2010')
plt.savefig('books_read.png')
'''
def plotKMeans(dataSet, partition):
    plt.xlabel('x')
    plt.ylabel('y')
    #for each in dataSet:
    #    print(each)
    for each in partition:
        index = int(each[0][5:]) - 1
        if each[1] == 0:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'green')
        elif each[1] == 1:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'blue')
        elif each[1] == 2:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'red')
        elif each[1] == 3:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'purple')
        elif each[1] == 4:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'yellow')
    plt.savefig('imgs/kMeans/c2ds3-2gk5.png')
    plt.show()

def plotKMeansMonkey(dataSet, partition):
    plt.xlabel('x')
    plt.ylabel('y')
    corte = 10
    #for each in dataSet:
    #    print(each)
    for each in partition:
        aux = each[0].split('s')
        index = int(aux[-1]) - 1
        if each[1] == 0:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'green')
        elif each[1] == 1:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'blue')
        elif each[1] == 2:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'red')
        elif each[1] == 3:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'purple')
        elif each[1] == 4:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'yellow')
        elif each[1] == 5:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'gray')
        elif each[1] == 6:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'black')
        elif each[1] == 7:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'pink')
        elif each[1] == 8:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'aqua')
        elif each[1] == 9:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'lavender')
        elif each[1] == 10:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'olive')
        elif each[1] == 11:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'yellowgreen')
    plt.savefig('imgs/kMeans/monkeyk12.png')
    plt.show()

def plotSingleLink(dataSet, partition,k):
    plt.xlabel('x')
    plt.ylabel('y')
    #for each in dataSet:
    #    print(each)
    for each in partition:
        index = int(each[0][6:]) - 1
        if each[1] == 0:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'green')
        elif each[1] == 1:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'blue')
        elif each[1] == 2:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'red')
        elif each[1] == 3:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'purple')
        elif each[1] == 4:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'yellow')
    plt.savefig('imgs/singleLink/c2ds1-2sp'+'k'+str(k)+'.png')
    plt.show()

def plotSingleLinkMonkey(dataSet, partition, k):
    plt.xlabel('x')
    plt.ylabel('y')
    corte = 10
    teste = ''
    #for each in dataSet:
    #    print(each)
    for each in partition:
        aux = each[0].split('s')
        index = int(aux[-1]) - 1
        if int(each[1]) == 0:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'green')
        elif int(each[1]) == 1:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'blue')
        elif int(each[1]) == 2:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'red')
        elif int(each[1]) == 3:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'purple')
        elif int(each[1]) == 4:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'yellow')
        elif int(each[1]) == 5:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'gray')
        elif int(each[1]) == 6:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'black')
        elif int(each[1]) == 7:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'pink')
        elif int(each[1]) == 8:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'aqua')
        elif int(each[1]) == 9:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'lavender')
        elif int(each[1]) == 10:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'olive')
        elif int(each[1]) == 11:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'yellowgreen')
        #teste = input('')
        #print(dataSet[index][1][0])
        #print(dataSet[index][1][1])
    plt.savefig('imgs/avgLink/c2ds3-2gk'+str(k)+'.png')
    plt.show()

def monkey(dataSet, monkey, k):
    plt.xlabel('x')
    plt.ylabel('y')

    for index in range(len(monkey)):
        if each[1] == 0:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'green')
        elif each[1] == 1:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'blue')
        elif each[1] == 2:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'red')
        elif each[1] == 3:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'purple')
        elif each[1] == 4:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'yellow')
        elif each[1] == 5:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'gray')
        elif each[1] == 6:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'black')
        elif each[1] == 7:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'pink')
        elif each[1] == 8:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'aqua')
        elif each[1] == 9:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'lavender')
        elif each[1] == 10:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'olive')
        elif each[1] == 11:
            plt.scatter(dataSet[index][1][0],dataSet[index][1][1], c = 'yellowgreen')
    plt.savefig('imgs/kMeans/monkeyk'+str(k)+'.png')
    plt.show()
