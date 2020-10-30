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
GBFS('Sri Nagar','Bengaluru',sup_dict)
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
