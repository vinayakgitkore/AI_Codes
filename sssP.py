def sssP(graph, node,d, dist, parent):
    dist[node] = d
    for child in graph[node]:
        if child != parent:
            sssP(graph,child, dist[node]+1, dist, node )
    
    
    
    
edges = [['A', 'B'], ['A', 'C'], ['C','E'], ['C', 'F'], ['B', 'D'], ['D', 'G'], ['G', 'I'], ['G', 'H']]
nodes = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I']

graph = {}
dist = {}
for key in nodes:
    graph[key] = []
    dist[key] = None

for (u, v) in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)
start = 'A'
dist[start] = 0 
sssP(graph, start,0, dist, -1)
for key, value in dist.items():
    print(key, value)

