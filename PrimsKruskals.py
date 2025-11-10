import heapq
class Graph:
        def __init__(self, edges, vertices, undirected = True):
            self.edges = edges
            self.vertices = vertices
            self.graph = {} #adjacency list
            for start, end, weight in edges:
                prev = self.graph.get(start, [])
                prev.append([end, weight])
                self.graph[start] = prev
        
        def prims(self):
            mst = []
            visited = set()
            totalWeight = 0
            heap = []
            initial = list(self.graph.keys())[0]
            def addEdges(vertex):
                visited.add(vertex)
                for neighbour, weight in self.graph[vertex]:
                    if neighbour not in visited:
                        heapq.heappush(heap, (weight, vertex, neighbour))
            addEdges(initial)

            while heap and len(visited)<len(self.graph):
                weight, u, v = heapq.heappop(heap)
                if v in visited: continue
                mst.append((u, v, weight))
                totalWeight += weight
                addEdges(v)
            
            if len(visited) < len(self.graph):
                return "Disconnected Graph"
            
            return mst, totalWeight

        def find(self, parent, x):
            if parent[x]==x: return x
            return self.find(parent, parent[x])

        def union(self, parent, x, y):
            rootOfX = self.find(parent, x)
            rootOfY = self.find(parent, y)
            parent[rootOfY] = rootOfX

        def Kruskals(self):
            self.edges.sort(key=lambda x: x[2])
            parent = [i for i in range(self.vertices+1)]
            mst = []
            totalWeight = 0
            for u, v, w in self.edges:
                if self.find(parent, u)!=self.find(parent, v):
                    self.union(parent, u, v)
                    mst.append([u, v, w])
                    totalWeight += w
            if len(mst) == self.vertices-1:
                return mst, totalWeight
            else:
                return "Disconnected Graph"
n = int(input("Enter the number of edges: "))
m =  int(input("Enter the number of vertices: "))
edges = []
for _ in range(n):
    inp = input("Enter edges as start, end, weight (2 3 4): ")
    if inp == "": break
    start, end, weight = map(int, inp.split())
    edges.append([start, end, weight])
g = Graph(edges, m)
out = g.prims()
if out == "Disconnected Graph": print("Disconnected Graph")
else:
    mst, totalWeight = out
    print("Edges in MST are: \n", mst)
    print("Total Weight: ", totalWeight)
