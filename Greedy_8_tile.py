start = [[7,6,3],[2,5,8],[1,0,4]]
goal = [[0,1,2],[3,4,5],[6,7,8]]
def hn_function(start):
    sum = 0
    for i in range(len(start)):
        for j in range(len(start)):
            for k in range(len(goal)):
                for l in range(len(goal)):
                    if start[i][j] == 0:
                        continue
                    if start[i][j] == goal[k][l]:
                        sum = sum + (abs(i-k)+abs(j-l))
    return (sum)
#print(sum)
#print(hn_function(start))
def ID_func(start):
    ID_list = []
    for i in range(len(start)):
        for j in range(len(start)):
            ID_list.append(start[i][j])
    return ID_list
#print(ID_func(start))
def move_position(node,lis):
    if lis[0] == node:
        return [['R',1],['D',3]]
    if lis[1] == node:
        return [['L',0],['R',2],['D',4]]
    if lis[2] == node:
        return [['L',1],['D',5]]
    if lis[3] == node:
        return [['U',0],['D',6],['R',4]]
    if lis[4] == node:
        return [['U',1],['L',3],['R',5],['D',7]]
    if lis[5] == node:
        return [['U',2],['D',8],['L',4]]
    if lis[6] == node:
        return [['U',3],['R',7]]
    if lis[7] == node:
        return [['U',4],['L',6],['R',8]]
    if lis[8] == node:
        return [['U',5],['L',7]]


def func(start):
    frontier1 = []
    for i in range(len(start)):
        if start[i] == 0:
            x = move_position(start[i],start)
            
            for j in range(len(x)):
                dump_pattern = start.copy()
                #pattern = dump_pattern
                #print(pattern,dump_pattern)
                if x[j][0] == 'L':
                    dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                    #if (dump_pattern not in frontier) and (dump_pattern not in visited):
                    frontier1.append(dump_pattern)
                    #    if dump_pattern == dest:
                            #BFS_8_tile(dump_pattern,dest)
                    #        return frontier1

                    #print('left',dump_pattern)
                if x[j][0] == 'R':
                    dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                    #if (dump_pattern not in frontier1) and (dump_pattern not in visited):
                    frontier1.append(dump_pattern)
                    #    if dump_pattern == dest:
                            #BFS_8_tile(dump_pattern,dest)
                    #       return frontier1

                    #print('right',dump_pattern)
                if x[j][0] == 'U':
                    dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                    #if (dump_pattern not in frontier1) and (dump_pattern not in visited):
                    frontier1.append(dump_pattern)
                    #    if dump_pattern == dest:
                            #BFS_8_tile(dump_pattern,dest)
                    #        return frontier1

                    #print('up',dump_pattern)
                if x[j][0] == 'D':
                    dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]

                    #if (dump_pattern not in frontier1) and (dump_pattern not in visited):
                    frontier1.append(dump_pattern)
                    #    if dump_pattern == dest:
                            #BFS_8_tile(dump_pattern,dest)
                    #        return frontier1
    return frontier1

#print(func(ID_func(start))) ### frontier_list
#hn_lis = []
def IID_func(Node):
    IID_list = []
    for i in [0,3,6]:
        IID_list.append([Node[i],Node[i+1],Node[i+2]])
    return IID_list
#IID_func(ID_func(start))
# def hn_lis_func(Nodes):
#     hn_lis = []             ## Nodes == frontier_list
#     for i in Nodes:             
#         hn_lis.append([i,hn_function(IID_func(i))])
#     return hn_lis

#print(hn_lis_func(func(ID_func(start))))
def find_min(find_list): 
    for k in range(len(find_list)):
        for l in range(len(find_list)-k -1):
            #print(find_list[l][1])
            if find_list[l][1] > find_list[l+1][1]:
                
                find_list[l],find_list[l+1] = find_list[l+1],find_list[l]
    #print(find_list)
    return find_list[0]

def find_min_list(find_list): 
    for k in range(len(find_list)):
        for l in range(len(find_list)-k -1):
            #print(find_list[l][1])
            if find_list[l][1] > find_list[l+1][1]:
                
                find_list[l],find_list[l+1] = find_list[l+1],find_list[l]
    #print(find_list)
    return find_list

#print(find_min(hn_lis_func(func(ID_func(start)))))
visited = []
frontier = []
node_min = []

def Greedy_8_tile(start1,goal1):
    if not visited:
        start2 =ID_func(start1)
        frontier.append([start2,hn_function(start1)])
        #print(frontier)
        visited.append(start2)
        #print(visited)
        f_node = frontier.pop()
        Greedy_8_tile(f_node[0],ID_func(goal1))
    elif start1 == goal1:
        #visited.append(goal)
        print('visited end')
        #return visited
    else:
        #print(start1)
        for i in func(start1):
            #print(i[0])
            if (i not in [m[0] for m in frontier]) and (i not in visited):
                #node_min.append(i)
                frontier.append([i,hn_function(IID_func(i))])
                
                if i == (goal1):
                    #visited.append(i)
                    Greedy_8_tile(i,(goal1))

        #print(frontier)
        x = find_min(frontier)
        frontier.remove(x)
        visited.append(x[0])

        #print(visited)
        #print('--------------------')
        Greedy_8_tile(x[0],goal1)
        #print(visited)



Greedy_8_tile(start,goal)

print('visited :',visited)
print()
print()
print('length of visited :',len(visited))

path = []
a,b=0,len(visited)-1
while(b!=0):
    while(visited[b] not in func(visited[a])):
        a=a+1
    path.append(visited[b])
    b=a
    a=0
path.append(visited[0])
print()
print('path :',path[::-1])
print()
print()
print('length of path :',len(path))

