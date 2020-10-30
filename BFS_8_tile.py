pattern = [1,2,3,4,5,6,7,0,8]
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
        
goal = [1,2,3,4,5,0,7,8,6]
#x = [['R',1],['D',3]]
#print(x[0][0])

#print(move_position(0,pattern))
#dump_pattern.append(1)
frontier = []
visited = []
#print(pattern,dump_pattern)
def BFS_8_tile(start,dest):
    if not visited:
        visited.append(start)
        BFS_8_tile(start,dest)
    if start == dest:
        #print(frontier)
        return frontier
        #print(frontier)
        #print('ended!!')
    else:
        #print('start')
        #rint(start)
        for i in range(len(start)):
            if start[i] == 0:
                x = move_position(start[i],start)
                
                for j in range(len(x)):
                    dump_pattern = start.copy()
                    #pattern = dump_pattern
                    #print(pattern,dump_pattern)
                    if x[j][0] == 'L':
                        dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                        if (dump_pattern not in frontier) and (dump_pattern not in visited):
                            frontier.append(dump_pattern)
                            if dump_pattern == dest:
                                #BFS_8_tile(dump_pattern,dest)
                                return frontier

                        #print('left',dump_pattern)
                    if x[j][0] == 'R':
                        dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                        if (dump_pattern not in frontier) and (dump_pattern not in visited):
                            frontier.append(dump_pattern)
                            if dump_pattern == dest:
                                #BFS_8_tile(dump_pattern,dest)
                                return frontier

                        #print('right',dump_pattern)
                    if x[j][0] == 'U':
                        dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                        if (dump_pattern not in frontier) and (dump_pattern not in visited):
                            frontier.append(dump_pattern)
                            if dump_pattern == dest:
                                #BFS_8_tile(dump_pattern,dest)
                                return frontier

                        #print('up',dump_pattern)
                    if x[j][0] == 'D':
                        dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]

                        if (dump_pattern not in frontier) and (dump_pattern not in visited):
                            frontier.append(dump_pattern)
                            if dump_pattern == dest:
                                #BFS_8_tile(dump_pattern,dest)
                                return frontier
    #print('frontier')
    #print(frontier)
    
    #print((frontier))
    next_state = frontier.pop(0)
    visited.append(next_state)
    #print('visited')
    #print(visited)
    #next_node = frontier.pop()
    #print(next_node)
    #next_node = frontier.pop(0)
    BFS_8_tile(next_state,dest)    

#print(pattern)
BFS_8_tile(pattern,goal)

print('visited :',visited)
print()
print()
print('length of visited :',len(visited))

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

#print(func(visited[0]))
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
