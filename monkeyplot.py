import plots as pl

path = 'datasets/monkey.txt'
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

for k in range(5,13):
    teste = ''
    file = open('backup/clu/avgLink/monkeyReal_'+str(k)+'.clu')
    partition = []
    for line in file:
        partition.append([line.split()[0],line.split()[1]])
    for each in partition:
        print(each)
    pl.plotSingleLinkMonkey(dataSet,partition,k)
    file.close()
