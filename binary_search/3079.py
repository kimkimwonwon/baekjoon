
# n 개의 입국 심사대
# m명 지나가야함 

from sys import stdin 

n, m = map(int, stdin.readline().split())

require_times = [int(stdin.readline()) for _ in range(n)]



lt = min(require_times)
rt =  max(require_times) * m 

answer = rt


def test(x):
    target= 0 
    for require_time in require_times:
        target = target + (x//require_time)
    
    return target 



while lt <= rt :
    mid = (lt + rt) // 2
    
    if test(mid) >= m:
        rt = mid -1 
        answer = min(mid,answer)
    elif test(mid) < m: 
        lt = mid + 1 
        
        

print(answer)