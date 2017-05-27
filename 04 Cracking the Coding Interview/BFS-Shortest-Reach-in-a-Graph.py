from queue import Queue

def readInputs_buildGraph():
    n, m = map(int, input().strip().split(' '))
    graph = [0]
    for j in range(n):
        graph.append([])

    for j in range(m):
        (x, y) = map(int, input().strip().split(' '))
        graph[x].append(y)
        graph[y].append(x)

    return n, graph

def computeDistance(s, graph):
    distances = {s: 0}
    q = Queue ()
    q.put(s)
    while (not q.empty()):
        e = q.get()
        d = distances[e] + 6
        for neighbor in graph[e]:
            if neighbor in distances:
                continue

            distances[neighbor] = d
            q.put(neighbor)
    return distances

def showDistances(s, n, distances):
    for i in range(1, n + 1):
        if (i == s):
            continue
        if i in distances:
            print(distances[i], end = ' ')
        else:
            print(-1, end = ' ')
    print()


t = int(input())
for i in range(t):
    n, graph = readInputs_buildGraph()
    s = int (input().strip())
    distances = computeDistance(s, graph)
    showDistances(s, n, distances)
