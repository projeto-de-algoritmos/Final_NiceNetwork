from django.urls.resolvers import _PATH_PARAMETER_COMPONENT_RE


alphabet = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ç','Z','X','C','V','B','N','M']
graph = {
    'Q': ['W','A'],
    'W': ['Q','A','S','E'],
    'E': ['W','S','D','R'],
    'R': ['E','D','F','T'],
    'T': ['R','F','G','Y'],
    'Y': ['T','G','H','U'],
    'U': ['Y','H','J','I'],
    'I': ['U','J','K','O'],
    'O': ['I','K','L','P'],
    'P': ['O','L','Ç'],
    'A': ['Q','W','S','Z'],
    'S': ['W','E','D','X','Z','A'],
    'D': ['E','R','F','C','X','S'],
    'F': ['R','T','G','V','C','D'],
    'G': ['T','Y','H','B','V','F'],
    'H': ['Y','U','J','N','B','G'],
    'J': ['U','I','K','M','N','H'],
    'K': ['I','O','L','M','J'],
    'L': ['O','P','Ç','K'],
    'Ç': ['P','L'],
    'Z': ['A','S','X'],
    'X': ['Z','S','D','C'],
    'C': ['X','D','F','V'],
    'V': ['C','F','G','B'],
    'B': ['V','G','H','N'],
    'N': ['B','H','J','M'],
    'M': ['N','J','K']
}

def bellmandford(src, graph):
    dist = {key: float('inf') for key in graph}
    dist[src] = 0
    queue = [src]
    while len(queue) > 0:
        for u in queue:
            for v in graph[u]:
                if dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
            queue.remove(u)
    return tuple(item for item in dist.items())

table = {letter: {dest: dist for dest, dist in bellmandford(letter, graph)} for letter in graph}

def sequence_alignment(x,y):
    """ compara x em relacao a y, qunato menor o retorno mais proximo x esta de y """
    global table
    gapX = 6
    gapY = 6
    x = x.upper()
    y = y.upper()
    m = len(x)
    n = len(y)

    memoization = [[-1 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        memoization[i][0] = i*gapY
    for j in range(n+1):
        memoization[0][j] = j*gapX

    for i in range(1, m+1 ):
        for j in range(1, n+1 ):
            memoization[i][j] = min(
                table[x[i-1]][y[j-1]] + memoization[i-1][j-1],
                gapY + memoization[i-1][j],
                gapX + memoization[i][j-1]
            )
    
    return(memoization[-1][-1])