#允许状态集合，例num=3
#S={(x,y)|x=0,y=0,1,2,3;x=3,y=0,1,2,3;x=y=1,2} x是此岸的传教士数，y是此岸的野人数
#允许决策集合，例boat_limit=2
#D={(u,v)|1<=u+v<=2,u,v=0,1,2} u是撘载的传教士数，v是搭载的野人数
num=3
boat_limit=2
temp=[]
for i in range(0,num+1):
    if i==0 or i==num:
        for j in range(0,num+1):
            temp.append((i,j))
    else:
        temp.append((i,i))
S=set(temp)
D=[]
for u in range(0,boat_limit+1):
    for v in range(0,boat_limit+1):
        if u+v>=1 and u+v<=boat_limit :
            D.append((u,v))
start=(num,num)
end=(0,0)
queue=[]
queue.append((0,start)) #前面的元素如果是0，说明是船在此岸，是1，说明船在对岸
step_dict={}
flag=0
finish=[]
while len(queue)!=0:
    q_pop=queue.pop(0)
    if q_pop[0]==0:
        for x in D:
            temp_s=(q_pop[1][0]-x[0],q_pop[1][1]-x[1])
            if temp_s not in S:
                continue
            if (1,temp_s) in step_dict:
                continue
            queue.append((1,temp_s))
            step_dict[(1,temp_s)]=q_pop
            if temp_s==end:
                flag=1
                finish=(1,temp_s)
                break
    else:
        for x in D:
            temp_s=(q_pop[1][0]+x[0],q_pop[1][1]+x[1])
            if temp_s not in S:
                continue
            if (0,temp_s) in step_dict:
                continue
            queue.append((0,temp_s))
            step_dict[(0,temp_s)]=q_pop
    if flag==1:
        break
if flag==1:
    print('该问题有解！最短路径：')
    path=[]
    path.append(finish)
    while path[-1]!=(0,start):
        path.append(step_dict[path[-1]])
    path.reverse()
    real_path=list(map(str,path))
    for i in range(len(real_path)):
        if i!=len(real_path)-1:
            print(real_path[i] + '->')
        else:
            print(real_path[i])
else:
    print('该问题无解')