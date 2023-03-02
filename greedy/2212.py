#https://www.acmicpc.net/problem/2212


import sys 


n = int(sys.stdin.readline())
K = int(sys.stdin.readline())

sequence = sorted(list(map(int, sys.stdin.readline().split())))



if K >= n:
    print(0)
    sys.exit()


dist = sorted([sequence[i] - sequence[i-1] for i in range(1,len(sequence))])


for i in range(K-1):
    dist.pop(-1)

print(sum(dist))