from collections import deque


n, m = map(int, input().split())


graph = [] 

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i,j

distance = [[0 for _ in range(m)] for _ in range(n)]

dx= [-1,1,0,0]
dy = [0,0,-1,1]
 
visited = [[0]*m for _ in range(n)]

def bfs(x, y):
    queue= deque()
    visited[x][y]= True
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < n and 0<= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))
                distance[nx][ny] = distance[x][y] +1 
                
                
                    
                
bfs(start_x,start_y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            distance[i][j] = -1


for i in distance:
    for j in i:
        print(j, end = ' ')
    print()