from collections import deque


n, m = map(int, input().split())


graph = [] 

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i,j

distance = [[0 for i in range(n)] for j in range(m)]

dx= [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue= deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny]== 1: 
                distance[nx][ny] = distance[x][y]+1
                queue.append((nx,ny))
            if graph[nx][ny]== 0:
                distance[nx][ny]=0
                

bfs(start_x, start_y)

print(distance)