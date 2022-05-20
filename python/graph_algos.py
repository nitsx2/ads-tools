import heapq

class GraphAlgo:
	def __init__(self):
		self.ans = None
		self.stack = []
		self.vis = []

	def dijkstra(self, adjlist, source):#single source shortest path, tc-v+e

		container = []
		heapq.heapify(container)
		for item in adjlist[source]:
			heapq.heappush(container, item)

		proccessed = {i+1: False for i in range(len(adjlist))}
		shortest_path = {i+1: float('inf') for i in range(len(adjlist))}
		proccessed[source] = True
		shortest_path[source] = 0


		while container:
			node = heapq.heappop(container)
			distance, node = node
			if proccessed[node]: continue
			# proccessed[node] = True
			shortest_path[node] = distance

			for neighbour in adjlist[node]:
				neighbour_distance, neighbour = neighbour
				if proccessed[neighbour] == False:
					heapq.heappush(container, (neighbour_distance+distance, neighbour))
			proccessed[node] = True


		return shortest_path




	def floyed_warshell(self, graph):#all pair shortest path #tc v3
		dist = [[graph[i][j] for j in range(len(graph[0]))] for i in range(len(graph))]

		v = len(graph)

		for k in range(v):
			for i in range(v):
				for j in range(v):
					if dist[i][k] == float('inf') or dist[k][j] == float('inf'): continue
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


		for i in range(v):
			if dist[i][i] < 0:
				print('negative cycle in graph')
				return


		return dist


	def can_bipartite(self, adjlist): #if can color with <=2 colors, or we can say chromatic number <= 2
		# use dfs only
		color = 0
		vis = {key: False for key in adjlist}
		clist = {key: None for key in adjlist}
		u = 1
		self.ans = True
		self.bipartite_dfs(u, color, adjlist, vis, clist)
		print(vis,clist)
		return self.ans
	

	def bipartite_dfs(self, u, color, adjlist, vis, clist):
		clist[u] = color
		vis[u] = True

		for v in adjlist[u]:
			if vis[v] == True:
				if clist[u] == clist[v]:
					self.ans = False
			else:
				self.bipartite_dfs(v, color^1, adjlist, vis, clist)



	def prims(self, nodes, data):
		adj = {i+1: [] for i in range(nodes)}
		vis = {i+1: False for i in range(nodes)}

		for triplet in data:
			u,v,w = triplet
			adj[u].append( (v,w) )
			adj[v].append( (u,w) )

		container = []

		vis[1] = True

		for vdata in adj[1]:
			v,w = vdata
			container.append( (w,(v,1)) )

		heapq.heapify(container)
		res = []

		while container:
			w, upair = heapq.heappop(container)
			u,uparent = upair
			if vis[u] == False:
				res.append( (u,uparent, w) )
				vis[u] = True
				for vdata in adj[u]:
					v, vw = vdata
					if vis[v] == False:
						heapq.heappush(container, (vw, (v, u)) )
		return res


	#dsu. 
	def dsu(self, nodes):
		parent = [i for i in range(nodes)]
		height = [1 for i in range(nodes)]

		self.union(parent[0], parent[1], parent, height)
		self.union(parent[2], parent[3], parent, height)
		self.union(parent[0], parent[2], parent, height)
		return parent, height



	def _union(self, x, y, p):#trivial
		px = self._find(x, p)
		py = self._find(y,p)
		if px == py: return False
		p[x] = y
		return True


	def union(self, x, y, p, h):
		px = self.find(x, p)
		py = self.find(y, p)
		if px == py: return False
		if h[x] > h[y]:
			p[y] = x
		elif h[y] > h[x]:
			p[x] = y
		else:
			p[y] = x
			h[x] += 1
		return True
		

	def _find(self, x,p):#trivial
		while p[x] != x:
			x = p[x]
		return x

	def find(self, x, p):#optimal
		if p[x] == x: return x

		p[x] = self.find(p[x], p)
		return p[x]


	def kosaraju(self, nodes, edges):
		adj = {node: [] for node in nodes}
		self.vis = {node: False for node in nodes}

		for edge in edges:
			adj[edge[0]].append(edge[1])

		#first dfs
		for node in nodes:
			if not self.vis[node]:
				self.kosaraju_dfs(adj, node)


		#reverse
		adj = {node: [] for node in nodes}
		self.vis = {node: False for node in nodes}

		for edge in edges:
			adj[edge[1]].append(edge[0])


		res = []
		while self.stack:
			node = self.stack.pop()
			if not self.vis[node]:
				component = {}
				self.kosaraju_dfs2(adj, node, component, node)
				res.append(component)

		return res 


	def kosaraju_dfs(self, adj, u):
		self.vis[u] = True

		for v in adj[u]:
			if not self.vis[v]:
				self.kosaraju_dfs(adj, v)
		self.stack.append(u)

	def kosaraju_dfs2(self, adj, u,component, start_node):
		self.vis[u] = True
		component[u] = start_node
		for v in adj[u]:
			if not self.vis[v]:
				self.kosaraju_dfs2(adj,v,component,start_node)




#KRUSHKAL


import heapq
class Solution:

    def __init__(self):
        self.vis = {}
        self.res = 0

	def solve(self, A, B):
        self.vis = {i+1: False for i in range(A)}
        self.who = [i for i in range(A+1)]
        self.h = [1 for i in range(A+1)]
        self.krushkal(B)
        
        return self.res


    def krushkal(self, edges):
        edges = sorted(edges, key=lambda item: item[2])

        for edge in edges:
            x,y,w =  edge
            x = self.find(x)
            y = self.find(y)
            if x != y:
                self.res += w
                self.union(x,y)



    def find(self, x):
        if x == self.who[x]: return x
        self.who[x] = self.find(self.who[x])
        return self.who[x]


    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return False # cycle

        if self.h[x] > self.h[y]:
            self.who[y] = x
        elif self.h[y] > self.h[x]:
            self.who[x] = y
        else:
            self.who[y] = x
            self.h[x] += 1
        return True






# adjlist = {1: [(1,2),(20,4)], 2: [(1,1), (37,3), (10,5)], 3: [(1,6), (37,2)], 4: [(20,1), (35,5)], 5: [(10,2), (35,4), (100,6)], 6: [(1,3), (100,5), (5,7)],  7: [(5,6), (2,8)], 8: [(2,7)]}

algo = GraphAlgo()
# o = algo.dijkstra(adjlist, 5)
# print(o)


# matrix = [[0,1,4,float('inf'), float('inf'), float('inf')],
# 		  [float('inf'), 0,4,2,7,float('inf')],
# 		  [float('inf'), float('inf'), 0, 3, 4, float('inf')],
# 		  [float('inf'),float('inf'), float('inf'), 0, float('inf'), 4],
# 		  [float('inf'),float('inf'),float('inf'),3,0,float('inf')],
# 		  [float('inf'),float('inf'),float('inf'),float('inf'),5,0]

# 		]

# o = algo.floyed_warshell(matrix)
# print(o)


# adjlist = {1: [2, 4], 2: [1,3], 3: [2,4], 4: [1,3]}
# o = algo.can_bipartite(adjlist)
# print(o)

# nodes = 6
# data = [[1,2,7], [1,6,7], [2,6,8], [2,3,6], [6,5,10], [3,5,2], [3,4,5], [5,4,5]]

# o = algo.prims(nodes, data)
# print(o)

# a,b = algo.dsu(5)
# print(a,b)

nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']
edges = [['a', 'b'], ['b', 'c'], ['c', 'i'],['c', 'd'], ['i', 'a'], ['d', 'e'], ['e', 'f'], ['f', 'd'], ['g', 'f'], ['g', 'h'], ['h', 'g'], ['h', 'k'] ]

o = algo.kosaraju(nodes, edges)
print(o)