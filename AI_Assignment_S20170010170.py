def function_DFS():
    f = open("capitals.csv", "r")
    x = f.readlines()
    #print(x[0])

    sup_dict = {}
    x1_list = []
    y1_list = []
    for i in range(1,len(x)):
        x1,y1,gn,hn = x[i].split(',')
        #sup_dict[x1] = y1
        x1_list.append(x1)
        y1_list.append(y1)

    x1_list_set_list = list(dict.fromkeys(x1_list))
    #print(x1_list_set_list)


    for k in range(len(x1_list_set_list)):
        connections = []
        for i in range(len(x1_list)):
            if x1_list[i] == x1_list_set_list[k]:
                connections.append(y1_list[i])
        sup_dict[x1_list_set_list[k]] = connections
    #print(sup_dict)
    #print(sup_dict)
    #x1_list_set_list = list(set(x1_list))
    #print(x1_list_set_list[0])
    #x = [1,2,3]
    #print(x[-1])

    #print(sup_dict['Sri Nagar'])

    stack = []
    visited = []

    def Depth_first_search(start,goal):
        if not visited:
            visited.append(start)
            return Depth_first_search(start,goal)

        if start == goal:
            #visited.append(goal)
            #print(visited)
            pass
        else:
            # frontier.append(start)
            #visited.append(start)
            #if len(stack) < 1:

                # count = 0
                #print(sup_dict[start])
            for i in sup_dict[start]:

                if (i not in stack) and (i not in visited):
                    stack.append(i)
                    if i == goal:
                        #print(i)
                        #stack.append(i)
                        visited.append(i)
                        return visited

            x = stack.pop()
            visited.append(x)
            return Depth_first_search(x,goal)


    path= []
    print('Please start the state names with capital letter...')
    source = input('source for DFS :')
    destination = input('destination for DFS: ')
    traversal = Depth_first_search(source,destination)
    print('traversal :',traversal)
    print()

    a,b=0,len(traversal)-1
    while(b!=0):
        while(traversal[b] not in sup_dict[traversal[a]]):
            a=a+1
        path.append(traversal[b])
        b=a
        a=0
    path.append(traversal[0])
    print()
    print('path :',path[::-1])




    #traversal = [1,2,3,4,5,6]
    #sup_dict = {1:[2,3],2:[3,4],3:[4,5],4:[5,6],5:[6]}

def function_BFS():
    f = open("capitals.csv", "r")
    x = f.readlines()
    #print(x[0])

    sup_dict = {}
    x1_list = []
    y1_list = []
    for i in range(1,len(x)):
        x1,y1,gn,hn = x[i].split(',')
        #sup_dict[x1] = y1
        x1_list.append(x1)
        y1_list.append(y1)

    x1_list_set_list = list(dict.fromkeys(x1_list))
    #print(x1_list_set_list)


    for k in range(len(x1_list_set_list)):
        connections = []
        for i in range(len(x1_list)):
            if x1_list[i] == x1_list_set_list[k]:
                connections.append(y1_list[i])
        sup_dict[x1_list_set_list[k]] = connections
    #print(sup_dict)
    #print(sup_dict)
    #x1_list_set_list = list(set(x1_list))
    #print(x1_list_set_list[0])
    #x = [1,2,3]
    #print(x[-1])

    #print(sup_dict['Sri Nagar'])

    stack = []
    visited = []

    def Breadth_first_search(start,goal):
        if start == goal:
            #visited.append(goal)
            #print(visited)
            pass
        else:
            # frontier.append(start)
            visited.append(start)
            #if len(stack) < 1:

                # count = 0
                #print(sup_dict[start])
            for i in sup_dict[start]:

                if (i not in stack) and (i not in visited):
                    stack.append(i)
                    if i == goal:
                        #print(i)
                        #stack.append(i)
                        visited.append(i)
                        return visited

            x = stack.pop(0)
            visited.append(x)
            return Breadth_first_search(x,goal)


    path= []
    print('Please start the state names with capital letter...')
    source = input('source for BFS :')
    destination = input('destination for BFS: ')
    
    traversal = Breadth_first_search(source,destination)
    traversal_list = list(dict.fromkeys(traversal))
    print('traversal :',traversal_list)
    print()
    a,b=0,len(traversal_list)-1
    while(b!=0):
        while(traversal_list[b] not in sup_dict[traversal_list[a]]):
            a=a+1
        path.append(traversal_list[b])
        b=a
        a=0
    path.append(traversal_list[0])
    print()
    print('path :',path[::-1])




    #traversal = [1,2,3,4,5,6]
    #sup_dict = {1:[2,3],2:[3,4],3:[4,5],4:[5,6],5:[6]}
def function_GBFS():
    f = open("capitals.csv", "r")
    x = f.readlines()
    #print(x[0])
    fa = open("Bangalore_distance.csv", "r")
    z = fa.readlines()

    ### first csv ######################################
    sup_dict = {}
    x1_list = []
    y1_list = []
    for i in range(1,len(x)):
        x1,y1,gn,hn = x[i].split(',')
        #sup_dict[x1] = y1
        x1_list.append(x1)
        y1_list.append(y1)

    x1_list_set_list = list(dict.fromkeys(x1_list))
    #print(x1_list_set_list)


    for k in range(len(x1_list_set_list)):
        connections = []
        for i in range(len(x1_list)):
            if x1_list[i] == x1_list_set_list[k]:
                connections.append(y1_list[i])
        sup_dict[x1_list_set_list[k]] = connections
    #print(sup_dict)
    ###### end of first csv ####################################
    sup_dict1 = {}
    x1_list1 = []
    y1_list1 = []
    hn_list1 = []
    import re
    for i in range(0,len(z)):
        x11,y11,hn1 = z[i].split(',')
        #sup_dict[x1] = y1
        x1_list1.append(x11)
        y1_list1.append(y11)
        for s in re.findall(r'-?\d+\.?\d*',hn1):
            hn_list1.append(float(s))    

    for j in range(len(x1_list1)):
        connections1 = []
        #connections1.append(y1_list1[j])
        connections1.append(hn_list1[j])
        sup_dict1[x1_list1[j]] = connections1

    ############## end of second csv ###############################
    #print(sup_dict1)
    def distance(state):
        return float(sup_dict1[state][0])

    def search(num):
        num =float(num)
        for key in sup_dict1:
            if num == sup_dict1[key][0]:
                return key
    #print(search(1561.59))
    #j = 'Agartala'
    #print(distance(j))
    visited = []
    frontier = []

    node = []


    node_min = []
    for i in (sup_dict):
        node.append(i)

    def GBFS(start,goal,sup_dict):
        if not visited:
            visited.append(start)
            GBFS(start,goal,sup_dict)
        elif start == goal:
            #visited.append(goal)
            print('visited end')
        else:
            #print(sup_dict[start])
            #print(distance(start))
            #visited.append(start)
            #frontier.append(start)

            for j in sup_dict[start]:
                #print(j)
                #print(distance(j))
                if (j not in frontier) and (j not in visited):
                    node_min.append(distance(j))
                    frontier.append(j)
            mi = sorted(node_min)
            #print(mi[0])     
            node_min.pop(0)
            mi = str(mi[0])
            #node_min = []

            #print(frontier)
            #print(search(mi))

            visited.append(search(mi))
            frontier.pop(0)
            #print('frontier :' ,frontier)
            #print('visited:' ,visited)
            #print('------------------')
            if search(mi) == goal:
                GBFS(search(mi),goal,sup_dict)
            else:
                GBFS(search(mi),goal,sup_dict)

    #print(node_min)
    print('Please start the state names with capital letter...')
    source = input('source for Greedy BFS :')
    #destination = input('destination for DFS: ')
    
    GBFS(source,'Bengaluru',sup_dict)
    path = []
    print()
    #print('traversal :' ,visited)
    traversal = visited
    a,b=0,len(traversal)-1
    while(b!=0):
        while(traversal[b] not in sup_dict[traversal[a]]):
            a=a+1
        path.append(traversal[b])
        b=a
        a=0
    path.append(traversal[0])
    print()
    print('shortest path: ',path[::-1])
def function_A_star():
    f = open("capitals.csv", "r")
    x = f.readlines()
    #print(x[0])
    fa = open("Bangalore_distance.csv", "r")
    z = fa.readlines()

    ### first csv ######################################
    sup_dict = {}
    x1_list = []
    y1_list = []
    g1_list = []
    for i in range(1,len(x)):
        x1,y1,gn,hn = x[i].split(',')
        #sup_dict[x1] = y1
        x1_list.append(x1)
        y1_list.append(y1)
        g1_list.append(gn)

    x1_list_set_list = list(dict.fromkeys(x1_list))
    #print(x1_list_set_list)


    for k in range(len(x1_list_set_list)):
        connections = []
        gn_dict_list = []
        for i in range(len(x1_list)):
            if x1_list[i] == x1_list_set_list[k]:
                temp_list = []
                temp_list.append(y1_list[i])
                temp_list.append(float(g1_list[i]))
                connections.append(temp_list)
        sup_dict[x1_list_set_list[k]] = connections


    #print(gn_dict)
    #print(sup_dict)
    sup_dict_copy = {}
    for k in range(len(x1_list_set_list)):
        connections = []
        for i in range(len(x1_list)):
            if x1_list[i] == x1_list_set_list[k]:
                connections.append(y1_list[i])
        sup_dict_copy[x1_list_set_list[k]] = connections
    # print(sup_dict_copy)
    ###### end of first csv ####################################

    sup_dict1 = {}
    x1_list1 = []
    y1_list1 = []
    hn_list1 = []
    import re
    for i in range(0,len(z)):
        x11,y11,hn1 = z[i].split(',')
        #sup_dict[x1] = y1
        x1_list1.append(x11)
        y1_list1.append(y11)
        for s in re.findall(r'-?\d+\.?\d*',hn1):
            hn_list1.append(float(s))    

    for j in range(len(x1_list1)):
        connections1 = []
        #connections1.append(y1_list1[j])
        connections1.append(hn_list1[j])
        sup_dict1[x1_list1[j]] = connections1


    ############## end of second csv ###############################

    def hn_function(Node):
        return float(sup_dict1[Node][0])
    #print(Nodes_function('Sri Nagar','Chandigarh',[498,123]))
    def find_min(find_list):
        #x = []

        #print(x)
        #print(find_list)
        for k in range(len(find_list)):
            for l in range(len(find_list)-k -1):
                #print(find_list[l][1])
                if find_list[l][1] > find_list[l+1][1]:

                    find_list[l],find_list[l+1] = find_list[l+1],find_list[l]
        #print(find_list)
        return find_list[0]
    #print(find_min('Sri Nagar',['Shimla','Chandigarh']))
    visited = []
    frontier = []

    find_min_list = []
    summ = []


    def A_star(start,goal,sup_dict):
        if not visited:
            frontier.append([start,hn_function(start)])
            #print(frontier[0][0])
            visited.append(frontier[0][0])
            f_node=frontier.pop()
            A_star(f_node,goal,sup_dict)
        elif start[0] == goal:
            #visited.append(goal)
            print('visited end')
        else:
            #print(start)

            for j in sup_dict[start[0]]:
                if (j[0] not in [m[0] for m in frontier] ) and (j[0] not in visited):
                    frontier.append([j[0],j[1]+hn_function(j[0])+start[1]-hn_function(start[0])])
                    if j[0] == goal:
                        frontier.append(j)
                        #visited.append(j[0])
                        A_star(j,'Bengaluru',sup_dict)  
                        #break

            #print(frontier) 
            next_node = find_min(frontier)
            #print(frontier)
            frontier.remove(next_node)
            visited.append(next_node[0])
            #next_start = next_node[0]
            #print(frontier)
            #print(visited)
            #print(next_node)
            #print('--------------------------')
            #next_val = next_node[1]
            #print(next_val,next_start)


            A_star(next_node,'Bengaluru',sup_dict)


    print('Please start the state names with capital letter...')
    source = input('source for  A_star  :')
            
    A_star(source,'Bengaluru',sup_dict)

    # print(visited)
    print()
    print()
    path =[]
    traversal = visited
    print('traversal :',traversal)
    a,b=0,len(traversal)-1
    while(b!=0):
        while(traversal[b] not in sup_dict_copy[traversal[a]]):
            a=a+1
        path.append(traversal[b])
        b=a
        a=0
    path.append(traversal[0])
    print()
    print('path :',path[::-1])
def function_DFS_8_tile():
    source = []
    destination = []
    print('source numbers if u want [1,2,3,4,5,6,7,0,8] then type 1 and press enter and next type 2 press enter and son on..')
    for i in range(9):
        inp = int(input())
        source.append(inp)
    print('destination numbers if u want [1,2,0,4,5,3,7,8,6] then type 1 and press enter and next type 2 press enter and son on..')
    for j in range(9):
        des1 = int(input())
        destination.append(des1)
        
    pattern = source
    goal = destination
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

    
    #x = [['R',1],['D',3]]
    #print(x[0][0])

    #print(move_position(0,pattern))
    #dump_pattern.append(1)
    frontier = []
    visited = []
    #print(pattern,dump_pattern)
    def DFS_8_tile(start,dest):
        if not visited:
            visited.append(start)
            DFS_8_tile(start,dest)
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
                                    #DFS_8_tile(dump_pattern,dest)
                                    return frontier

                            #print('left',dump_pattern)
                        if x[j][0] == 'R':
                            dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                            if (dump_pattern not in frontier) and (dump_pattern not in visited):
                                frontier.append(dump_pattern)
                                if dump_pattern == dest:
                                    #DFS_8_tile(dump_pattern,dest)
                                    return frontier

                            #print('right',dump_pattern)
                        if x[j][0] == 'U':
                            dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                            if (dump_pattern not in frontier) and (dump_pattern not in visited):
                                frontier.append(dump_pattern)
                                if dump_pattern == dest:
                                    #DFS_8_tile(dump_pattern,dest)
                                    return frontier

                            #print('up',dump_pattern)
                        if x[j][0] == 'D':
                            dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]

                            if (dump_pattern not in frontier) and (dump_pattern not in visited):
                                frontier.append(dump_pattern)
                                if dump_pattern == dest:
                                    #DFS_8_tile(dump_pattern,dest)
                                    return frontier
        #print('frontier')
        #print(frontier)

        #print((frontier))
        next_state = frontier.pop()
        visited.append(next_state)
        #print('visited')
        #print(visited)
        #next_node = frontier.pop()
        #print(next_node)
        #next_node = frontier.pop(0)
        DFS_8_tile(next_state,dest)    

    #print(pattern)
    DFS_8_tile(pattern,goal)

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
                                #DFS_8_tile(dump_pattern,dest)
                        #        return frontier1

                        #print('left',dump_pattern)
                    if x[j][0] == 'R':
                        dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                        #if (dump_pattern not in frontier1) and (dump_pattern not in visited):
                        frontier1.append(dump_pattern)
                        #    if dump_pattern == dest:
                                #DFS_8_tile(dump_pattern,dest)
                        #       return frontier1

                        #print('right',dump_pattern)
                    if x[j][0] == 'U':
                        dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]
                        #if (dump_pattern not in frontier1) and (dump_pattern not in visited):
                        frontier1.append(dump_pattern)
                        #    if dump_pattern == dest:
                                #DFS_8_tile(dump_pattern,dest)
                        #        return frontier1

                        #print('up',dump_pattern)
                    if x[j][0] == 'D':
                        dump_pattern[i],dump_pattern[x[j][1]] = dump_pattern[x[j][1]],dump_pattern[i]

                        #if (dump_pattern not in frontier1) and (dump_pattern not in visited):
                        frontier1.append(dump_pattern)
                        #    if dump_pattern == dest:
                                #DFS_8_tile(dump_pattern,dest)
                        #        return frontier1
        return frontier1

    # sup_dict = {}
    # for i in visited:
    #     print(type(i))
    #     x = func(i)
    #     connections = []
    #     for j in x:
    #         connections.append(j)
    #     #print(connections)
    #     i = str(i)
    #     sup_dict[i] = connections
    #x = func(i)
    # print(sup_dict)
    # print()
    # print()
    # print(visited)
    # x= [1,2,3,4,5,0,7,8,6]
    # s = str(x)
    # print(sup_dict[x])
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


#function_DFS_8_tile()

def function_BFS_8_tile():
    source = []
    destination = []
    print('source numbers if u want [1,4,2,3,7,5,6,0,8] then type 1 and press enter and next type 2 press enter and son on..')
    for i in range(9):
        inp = int(input())
        source.append(inp)
    print('destination numbers if u want [0,1,2,3,4,5,6,7,8] then type 1 and press enter and next type 2 press enter and son on..')
    for j in range(9):
        des1 = int(input())
        destination.append(des1)
        
    pattern = source
    goal = destination
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

#function_BFS_8_tile()
def function_Greedy_8_tile():
    def IID_func(Node):
        IID_list = []
        for i in [0,3,6]:
            IID_list.append([Node[i],Node[i+1],Node[i+2]])
        return IID_list
    
    source = []
    destination = []
    print('source numbers if u want [7,6,3,2,5,8,1,0,4] then type 1 and press enter and next type 2 press enter and son on..')
    for i in range(9):
        inp = int(input())
        source.append(inp)
    print('destination numbers if u want [0,1,2,3,4,5,6,7,8] then type 1 and press enter and next type 2 press enter and son on..')
    for j in range(9):
        des1 = int(input())
        destination.append(des1)

    sou = IID_func(source)
    des = IID_func(destination)
    
    start = sou
    goal = des
    #start = [[7,6,3],[2,5,8],[1,0,4]]
    #goal = [[0,1,2],[3,4,5],[6,7,8]]
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

#function_Greedy_8_tile()

def function_A_star_8_tile():
    def IID_func(Node):
        IID_list = []
        for i in [0,3,6]:
            IID_list.append([Node[i],Node[i+1],Node[i+2]])
        return IID_list
    
    source = []
    destination = []
    print('source numbers if u want [1,2,3,4,5,6,7,0,8] then type 1 and press enter and next type 2 press enter and son on..')
    for i in range(9):
        inp = int(input())
        source.append(inp)
    print('destination numbers if u want [1,0,2,3,5,6,4,7,8] then type 1 and press enter and next type 2 press enter and son on..')
    for j in range(9):
        des1 = int(input())
        destination.append(des1)

    sou = IID_func(source)
    des = IID_func(destination)
    
    start = sou
    goal = des
    
    #start = [[1,2,3],[4,5,6],[7,0,8]]
    #goal = [[1,0,2],[3,5,6],[4,7,8]]
    
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
    
    #def IID_func(Node):
    #    IID_list = []
    #    for i in [0,3,6]:
    #        IID_list.append([Node[i],Node[i+1],Node[i+2]])
    #    return IID_list
    
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

    def A_star_8_tile(start1,goal1):
        if not visited:
            start2 =ID_func(start1)
            frontier.append([start2,hn_function(start1)])
            #print(frontier)
            visited.append(start2)
            #print(visited)
            f_node = frontier.pop()
            A_star_8_tile(f_node,ID_func(goal1))
        elif start1 == goal1:
            #visited.append(goal)
            #visited.pop()
            print('visited end')
            #return visited
        else:
            #print(start1)
            for i in func(start1[0]):
                #print(i[0])
                if (i not in [m[0] for m in frontier]) and (i not in visited):
                    #node_min.append(i)
                    frontier.append([i,(1 + hn_function(IID_func(i)) + start1[1] - hn_function(IID_func(start1[0])))])

                    if i == (goal1):
                        #visited.append(i)
                        frontier.append(i)
                        A_star_8_tile(i,(goal1))

            #print(frontier)
            x = find_min(frontier)
            frontier.remove(x)
            visited.append(x[0])
            #print('visited--------------------------------------------')
            #print(visited)
            #print('-----------------------------------------------')
            A_star_8_tile(x,goal1)
            #print(visited)



    A_star_8_tile(start,goal)
    ##########################
    visited.pop()#############################
    ###########################################
    
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
    
#function_A_star_8_tile()

print('Choose a number you want  :')
print('\n 1. function_DFS \n 2. function_BFS \n 3. function_GBFS \n 4. function_A_star \n 5. function_DFS_8_tile \n 6. function_BFS_8_tile \n 7. function_Greedy_8_tile \n 8. function_A_star_8_tile \n')
x = int(input())
if x == 1:
    print('DFS of capitals ')
    function_DFS()
elif x == 2:
    print('BFS of capitals ')
    function_BFS()
elif x == 3:
    print('GBFS of capitals ')
    function_GBFS()
elif x == 4:
    print('A_star of capitals ')
    function_A_star()
elif x == 5:
    print('DFS of 8 tiles problem ')
    function_DFS_8_tile()
elif x == 6:
    print('BFS of 8 tiles problem ')
    function_BFS_8_tile()
elif x == 7:
    print('Greedy of 8 tiles problem ')
    function_Greedy_8_tile()
elif x == 8:
    print('A_star of 8 tiles problem ')
    function_A_star_8_tile()


    