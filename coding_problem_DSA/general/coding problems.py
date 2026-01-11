#find the number of island where a island is defined as a bunch of 1s connecting to each
#other horizontally and vertically
def numOfisalnd(island):
    ylen=len(island)
    xlen=len(island[0])
    #island is a 2d array of integers
    def countIsland():
        count=0
        for i in range(ylen):
            for j in range(xlen):
                if island[i][j]==1:
                    dfs(i,j)
                    count=count+1
        return count
    def dfs(x,y):
        if x<0 or y<0 or x>=ylen or y>=xlen or island[x][y]!=1:
            return
        if island[x][y]==1:
            island[x][y]=0
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)
    return countIsland()

#finding the largest component of a graph
def largestComponent(nodes,graph):
    #important note:define the inner function before we write code in the outer function
    def getsize(node):
        if node in s:
            return 0
        s.add(node)
        size=1
        for neighbour in graph[node]:
            return size+getsize(neighbour)
        
    s=set()
    max=-99
    for node in nodes:
        if node not in s:
            size=getsize(node)
            if size>max:
                max=size 
    return max

nodes=[1,2,3,4]
graph={1:[2],  2:[1,3],  3:[2,4],  4:[3]}
print(largestComponent(nodes,graph))

