
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
traversal = Breadth_first_search('Kohima','Chennai')
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
