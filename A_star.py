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
        

A_star('Patna','Bengaluru',sup_dict)

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
