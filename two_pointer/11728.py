#   배열합치기



n , m = map(int, input().split())

# 리스트로 입력받기 !! 

lst1 = [*map(int,input().split())]
lst2 =  [*map(int,input().split())]


# start end  start with 0 

p1, p2 = 0, 0 

final_list=[]
while p1 < len(lst1) and p2 < len(lst2):
    if lst1[p1] < lst2[p2]:
        final_list.append(lst1[p1])
        p1+=1
    elif lst1[p1] >= lst2[p2]:
        final_list.append(lst2[p2])
        p2+=1



if p1 == len(lst1):
    for x in lst2[p2:]:
        final_list.append(x)
if p2 == len(lst2):
    for x in lst1[p1:]:
        final_list.append(x)

print(*final_list)