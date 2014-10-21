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
    mini = dict_of_costs[resultind]
    for im in list(dict_of_costs.keys()):
        if dict_of_costs[im] < mini:
            mini = dict_of_costs[im]
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

# для работы
dictOfCosts = {}

# выбираем начальную точку
selectedVertices = [0]
# для вывода в файл
adjacencyList = [[] for y in range(numOfStrings)]

for v in range(1, numOfStrings):
    dictOfCosts[v] = distance(dictOfCoordinates[0], dictOfCoordinates[v])
print("dictOfCosts", dictOfCosts)

# первая итерация - запускаем цикл поиска самого дешёвого ребра, инцидентного ей.
# для этого сравниваем числа в строке, соответствующей номеру вершины
first_iteration_result = searching_for_the_cheapest(dictOfCosts)
selectedVertices.append(first_iteration_result)
adjacencyList[0].append(first_iteration_result)
adjacencyList[first_iteration_result].append(0)
dictOfCosts.pop(first_iteration_result)

# далее повторяем процедуру, но уже для двух точек: начальной и добавленной (и так далее)
# условие остановки: len(selectedVertices) = numOfStrings
# глобальный цикл
for n in range(numOfStrings - 2):
    print("------")
    for m in list(dictOfCosts.keys()):
        tempCost = distance(dictOfCoordinates[selectedVertices[-1]], dictOfCoordinates[m])
        if tempCost < dictOfCosts[m]:
            dictOfCosts[m] = tempCost
    print("dictOfCosts before", dictOfCosts)

    # ищем наименьшее из посчитанных расстояний
    newVertice = searching_for_the_cheapest(dictOfCosts)
    selectedVertices.append(newVertice)
    adjacencyList[selectedVertices[-1]].append(newVertice)
    adjacencyList[newVertice].append(selectedVertices[-1])
    dictOfCosts.pop(newVertice)
    print("dictOfCosts after", dictOfCosts)
    print(n + 2, "step, selected vertices:", selectedVertices)
    for index in adjacencyList:
        print(index)

# for index in adjacencyList:
#     print(index)
# создаём список списков, длиной = numOfStrings, элемент - список смежных данной вершин
# f = open('out.txt', 'w')
# TODO
# for index in adjacencyList:
#    f.write(index + ' 0\n')