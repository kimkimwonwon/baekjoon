
# n 개의 입국 심사대
# m명 지나가야함 

n , m = map(int, input().split())

require_times = []

for i in range(n):
    require_times.append(int(input()))

require_times = list(require_times)



lt = 0 
rt =  100000 * 1000000000
mid = (lt + rt) // 2


def test(x):
    target= 0 
    for require_time in require_times:
        target = target + (x//require_time)
    
    return target 


final = []

while lt <= rt :
    mid = (lt + rt) // 2
    
    if test(mid) >= m:
        final.append(mid)   
        rt = mid -1 
    elif test(mid) < m: 
        lt = mid + 1 
        

print(min(final))