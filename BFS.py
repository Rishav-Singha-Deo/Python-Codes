graph={1:[2,3],
       2:[1,4,5],
       3:[1,6],
       4:[2],
       5:[2,6],
       6:[3,5]}

visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        for neighbour in graph:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visited,graph,1)