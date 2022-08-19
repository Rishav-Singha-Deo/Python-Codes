graph={1:[2,3],
       2:[1,4,5],
       3:[1,6],
       4:[2],
       5:[2,6],
       6:[3,5]}

visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,1)