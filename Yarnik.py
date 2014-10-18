'''Минимальное связывающее дерево, заданное в виде списков смежностей.
Для каждой точки исходного множества указать порядковые номера точек, смежных с ней.
Список начинать с новой строки, точки внутри списка упорядочить по возрастанию номеров.
Каждый список заканчивается 0. В последней строке файла записать вес.'''


# вычисляем расстояние
def distance(first_point, second_point):
    return abs(first_point[0] - second_point[0]) + abs(first_point[1] - second_point[1])


# возвращает [индекс вершины, вес ребра до неё]
def searching_for_the_most_cheap(list_of_costs):
    resultind = 0
    if list_of_costs[resultind] != 0:
        mini = list_of_costs[resultind]
    else:
        mini = list_of_costs[resultind + 1]
    for im in range(1, len(list_of_costs)):
        if (list_of_costs[im] < mini) and (list_of_costs[im] > 0) and (im not in selectedVertices):
            print(im, "element =", list_of_costs[im], "is not in", selectedVertices, im not in selectedVertices)
            mini = list_of_costs[im]
            resultind = im
    return [resultind, mini]


# возвращает строку, в которой находится элемент с известным столбцовым индексом
def searching_for_damn_index(column_ind, its_value):
    for ind in range(numOfStrings):
        if adjacencyMatrix[ind][column_ind] == its_value:
            return ind

f = open('in.txt', 'r')
numOfStrings = int(f.readline())
dictOfCoordinates = {}
for i in range(numOfStrings):
    tempStr = f.readline().split()
    dictOfCoordinates[i] = [int(tempStr[0]), int(tempStr[1])]
# print("dictOfCoordinates", dictOfCoordinates)
f.close()

# для работы
adjacencyMatrix = [[0 for x in range(numOfStrings)] for y in range(numOfStrings)]
# для вывода в файл
adjacencyList = [[] for y in range(numOfStrings)]

for n in range(numOfStrings):
    for p in range(numOfStrings):
        if n == p:
            adjacencyMatrix[n][p] = 0
        elif n > p:
            adjacencyMatrix[n][p] = adjacencyMatrix[p][n]
        else:
            adjacencyMatrix[n][p] = distance(dictOfCoordinates[n], dictOfCoordinates[p])
# print("adjacencyMatrix", adjacencyMatrix)
# выбираем начальную точку
selectedVertices = [0]
selectedVertices[0] = 0

# первая итерация - запускаем цикл поиска самого дешёвого ребра, инцидентного ей.
# для этого сравниваем числа в строке, соответствующей номеру вершины
first_iteration_result = searching_for_the_most_cheap(adjacencyMatrix[0])[0]
selectedVertices.append(first_iteration_result)
adjacencyList[0].append(first_iteration_result)
adjacencyList[first_iteration_result].append(0)

# далее повторяем процедуру, но уже для двух точек: начальной и добавленной (и так далее)
# условие остановки: len(selectedVertices) = numOfStrings
# глобальный цикл
for n in range(numOfStrings - 1):
    print("selected vertices:", selectedVertices)
    dictOfTempCostsAndInd = {}
    # тут мы получаем m=len(selectedVertices) списков вида "n" : [result, min] (ключ - вершина из selectedVertices)
    # нам нужно выбрать наименьший min и добавить к selectedVertices соответствующий ему result
    # но всё не так-то просто. нужно помнить, для какой из вершин мы нашли
    # каждый из списков [result, min], среди которых - определивший результат
    for m in selectedVertices:
        dictOfTempCostsAndInd[m] = searching_for_the_most_cheap(adjacencyMatrix[m])
    print("dictOfTempCostsAndInd", dictOfTempCostsAndInd)
    listOfTempCosts = [0 for x in range(len(selectedVertices))]
    listOfTempIndexes = [0 for x in range(len(selectedVertices))]
    # отдельно выделяем стоимости
    d = 0
    for p in selectedVertices:
        print("p", p, "dictOfTempCostsAndInd[p][1]", dictOfTempCostsAndInd[p][1])
        listOfTempCosts[d] = dictOfTempCostsAndInd[p][1]
        listOfTempIndexes[d] = dictOfTempCostsAndInd[p][0]
        d += 1
    tempList = searching_for_the_most_cheap(listOfTempCosts)
    # индекс искомой стоимости в промежуточном массиве
    tempInd = listOfTempCosts.index(tempList[1])
    # индекс искомой стоимости в изначальном списке
    desiredInd = listOfTempIndexes[tempInd]
    selectedVertices.append(desiredInd)
    initialIndex = searching_for_damn_index(desiredInd, tempList[1])
    adjacencyList[initialIndex].append(desiredInd)
    adjacencyList[desiredInd].append(initialIndex)


for index in adjacencyList:
    print (index)
# создаём список списков, длиной = numOfStrings, элемент - список смежных данной вершин
# f = open('out.txt', 'w')
# TODO
# for index in adjacencyList:
#    f.write(index + ' 0\n')