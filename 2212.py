#https://www.acmicpc.net/problem/2212


from sys import stdin 


n = int(stdin.readline())

K = int(stdin.readline())

sequence = list(map(int, stdin.readline().split()))


sequence= sorted(sequence)

for i in range(K):
    