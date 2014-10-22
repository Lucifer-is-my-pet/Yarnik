'''Минимальное связывающее дерево, заданное в виде списков смежностей.
Для каждой точки исходного множества указать порядковые номера точек, смежных с ней.
Список начинать с новой строки, точки внутри списка упорядочить по возрастанию номеров.
Каждый список заканчивается 0. В последней строке файла записать вес.'''


# вычисляем расстояние
def distance(first_point, second_point):
    return abs(first_point[0] - second_point[0]) + abs(first_point[1] - second_point[1])


# возвращает [индекс вершины, вес ребра до неё]
def searching_for_the_cheapest(dict_of_costs):
    resultind = list(dict_of_costs.keys())[0]
    mini = dict_of_costs[resultind][0]
    for im in list(dict_of_costs.keys()):
        if dict_of_costs[im][0] < mini:
            mini = dict_of_costs[im][0]
            resultind = im
    return resultind


f = open('in.txt', 'r')
numOfStrings = int(f.readline())
dictOfCoordinates = {}
for i in range(numOfStrings):
    tempStr = f.readline().split()
    dictOfCoordinates[i] = [int(tempStr[0]), int(tempStr[1])]
# print("dictOfCoordinates", dictOfCoordinates)
f.close()

# для работы; {до какой вершины : [сколько, от какой]}
dictOfCosts = {}
# для вывода в файл
adjacencyList = [[] for y in range(numOfStrings)]
# вес
weight = 0

for v in range(1, numOfStrings):
    dictOfCosts[v] = [distance(dictOfCoordinates[0], dictOfCoordinates[v]), 0]


# выбираем начальную точку
selectedVertices = [0]
# первая итерация - запускаем цикл поиска самого дешёвого ребра, инцидентного ей.
# для этого сравниваем числа в строке, соответствующей номеру вершины
first_iteration_result = searching_for_the_cheapest(dictOfCosts)
selectedVertices.append(first_iteration_result)
adjacencyList[0].append(first_iteration_result)
adjacencyList[first_iteration_result].append(0)
weight += dictOfCosts[first_iteration_result][0]
dictOfCosts.pop(first_iteration_result)

# далее повторяем процедуру, но уже для двух точек: начальной и добавленной (и так далее)
# условие остановки: len(selectedVertices) = numOfStrings
# глобальный цикл
for n in range(numOfStrings - 2):
    # print("------")
    for m in list(dictOfCosts.keys()):
        tempCost = distance(dictOfCoordinates[selectedVertices[-1]], dictOfCoordinates[m])
        if tempCost < dictOfCosts[m][0]:
            dictOfCosts[m] = [tempCost, selectedVertices[-1]]
    # print("dictOfCosts before", dictOfCosts)

    # ищем наименьшее из посчитанных расстояний
    newVertice = searching_for_the_cheapest(dictOfCosts)
    adjacencyList[dictOfCosts[newVertice][1]].append(newVertice)
    adjacencyList[newVertice].append(dictOfCosts[newVertice][1])
    selectedVertices.append(newVertice)
    weight += dictOfCosts[newVertice][0]
    dictOfCosts.pop(newVertice)
    # print("dictOfCosts after", dictOfCosts)
    # print(n + 2, "step, selected vertices:", selectedVertices)

for index in adjacencyList:
    index.sort()

f = open('out.txt', 'w')
for index in adjacencyList:
    for v in index:
        f.write(str(v + 1) + " ")
    f.write("0\n")
f.write(str(weight))
f.close()