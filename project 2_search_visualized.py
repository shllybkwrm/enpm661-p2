# ENPM661, Spring 2020, Project 2
# Shelly Bagchi & Omololu Makinde

import math
import numpy as np
import cv2


class Node:
    def __init__(self, node_no, map, parent, act, cost):
        self.map = map
        self.parent = parent
        self.act = act
        self.node_no = node_no
        self.cost = cost

def conv_coord_to_row_col(x,y):
    i=int(10-y)
    j=int (x)
    return i,j

def row_col_to_conv_coord(i,j):
    x=int(j)
    y=int (10-i)
    return x,y
###############################This will get X AND Y COORDINATES OF START AND FINISH POINT FROM USER###########00=90
###############################COMMENT OUT WHEN FIXED################
##def get_initial_robcoord():
##    map = np.ones((11,21),dtype=int)
####    print(map)
##    print("Please enter the x and y coordinates of the point robot")
##    x=int(input("Enter the x coordinate "))
##    y=int(input("Enter the y coordinate "))
##    i,j=conv_coord_to_row_col(x,y)
##    map[i,j]=0
##    return x,y,map
##x,y,map1=get_initial_robcoord()
##print("map1",map1,"x",x,"y",y)
##def get_final_robcoord():
##    map = np.ones((11,21),dtype=int)
####    print(map)
##    print("Please enter the x and y coordinates of the point robot")
##    x=int(input("Enter the x coordinate "))
##    y=int(input("Enter the y coordinate "))
##    i,j=conv_coord_to_row_col(x,y)
##    map[i,j]=0
##    return x,y,map
##u,v,map2=get_final_robcoord()
##print("map2",map2,"u",u,"v",v)
###############################RUNNING CODE DURING DEVELOPMENT###########00=90
###############################COMMENT OUT WHEN AUTOMATED################
height = 11
width = 21

x=2
y=3

map1=np.ones((height, width), dtype=int)
map1[y,x]=0
map2=np.ones((height, width), dtype=int)
map2[5,7]=0

map_img = 255*np.ones((height, width, 3), np.uint8)

def draw_map(map):
    global height, width, map_img
    # Create a white base image to draw map onto
    #block_size = 10
    #map_img = 255*np.ones((height*block_size, width*block_size, 3), np.uint8)
    # Convert dtype
    map_img = 255*np.array(map, np.uint8)
    # Upscale before imshow
    scale_percent = 1000 # percent of original size
    w = int(map_img.shape[1] * scale_percent / 100)
    h = int(map_img.shape[0] * scale_percent / 100)
    # resize image
    resized = cv2.resize(map_img, (w,h), interpolation = cv2.INTER_AREA)
    
    cv2.imshow('Current map', resized)
    cv2.waitKey(50)  # in ms - adjust as needed for display speed

    return



def get_robcoord(map):
    i,j=np.where(map ==0)
##    print("row and column of 0 ", np.where(map ==0))
    x,y=row_col_to_conv_coord(i,j)
##    print("x and y coordinates", x,y)
    return x,y
##x,y=get_robcoord(map)


#  FIX THIS
def check_location(map):
    x,y=get_robcoord(map)
##    robcoord=[]
    if 11>=x>=9 and 6>=y>=4:
        print("You are in the rectangular obstacle space, try another location")
        exit(0)
    elif (x-16)**2+(y-5)**2 < 1.5**2:
        print("You are in the circle obstacle space, try another location")
        exit(0)
    else:
##        robcoord=[x,y]
##        map[y,x]=0
        return x,y,map
x,y,map=check_location(map1)


def move_left(map):
    i,j=np.where(map ==0)
    if j == 0:
        return None
    else:
        temp_arr = np.copy(map)
        temp = temp_arr[i, j - 1]
        temp_arr[i,j] = temp
        temp_arr[i, j - 1] = 0
        #print(np.where(temp_arr==0))
        return temp_arr
##map=move_left(map)
##print("map",map,"x",x,"y",y)
##
def move_right(map):
    i,j=np.where(map ==0)
    if j == 20:
        return None
    else:
        temp_arr = np.copy(map)
        temp = temp_arr[i, j + 1]
        temp_arr[i,j] = temp
        temp_arr[i, j +1] = 0
##        print(np.where(temp_arr==0))
        return temp_arr
##map=move_right(map)
##print("map",map)
def move_up(map):
    i,j=np.where(map ==0)
    if i == 0:
        return None
    else:
        temp_arr = np.copy(map)
        temp = temp_arr[i-1, j]
        temp_arr[i,j] = temp
        temp_arr[i-1, j] = 0
##        print(np.where(temp_arr==0))
        return temp_arr
##map=move_up(map)
##print("map",map)    
def move_down(map):
    i,j=np.where(map ==0)
    if i == 9:
        return None
    else:
        temp_arr = np.copy(map)
        temp = temp_arr[i+1, j]
        temp_arr[i,j] = temp
        temp_arr[i+1, j] = 0
##        print(np.where(temp_arr==0))
        return temp_arr
##map=move_down(map)
##print("map",map) 
def move_left_up_diag(map):
    i,j=np.where(map ==0)
    if i==0 or j == 0:
        return None
    else:
        temp_arr = np.copy(map)
        temp = temp_arr[i-1, j-1]
        temp_arr[i,j] = temp
        temp_arr[i-1, j-1] = 0
##        print(np.where(temp_arr==0))
        return temp_arr
##map=move_left_up_diag(map)
##print("move_left_up_diag map",map)

def move_left_down_diag(map):
    i,j=np.where(map ==0)
    if i == 9 or j==0:
        return None
    else:
        temp_arr = np.copy(map)
        temp = temp_arr[i+1, j-1]
        temp_arr[i,j] = temp
        temp_arr[i+1, j-1] = 0
##        print(np.where(temp_arr==0))
        return temp_arr
##map=move_left_down_diag(map)
##print("move_left_down_diag map",map)
##
def move_right_up_diag(map):
    i,j=np.where(map ==0)
    if i==0 or y == 19:
        return None
    else:
        temp_arr = np.copy(map)
        temp = temp_arr[i-1, j+1]
        temp_arr[i,j] = temp
        temp_arr[i-1, j+1] = 0
##        print(np.where(temp_arr==0))
        return temp_arr
##map=move_right_up_diag(map)
##print(" move_right_up_diag map",map)

def move_right_down_diag(map):
    i,j=np.where(map ==0)
    if j == 0:
        return None
    else:
        temp_arr = np.copy(map)
        temp = temp_arr[i+1, j+1]
        temp_arr[i,j] = temp
        temp_arr[i+1, j+1] = 0
##        print(np.where(temp_arr==0))
        return temp_arr
##map=move_right_down_diag(map)
##print(" move_right_down_diag map",map)

####
def get_neighbours(action,map):
    if action == 'up':
##        print(map)
        return move_up(map)
    if action == 'down':
##        print(map)
        return move_down(map)
    if action == 'left':
##        print(map)
        return move_left(map)
    if action == 'right':
##        print(map)
        return move_right(map)
    if action == 'down_right':
##        print(map)
        return move_right_down_diag(map)
    if action == 'up_right':
##        print(map)
        return move_right_up_diag(map)
    if action == "down_left":
##        print(map)
        return move_left_down_diag(map)
    if action == "up_left":
##        print(map)
        return move_left_up_diag(map)        
    else:
        return None
##action = ["down", "up", "left", "right","down_right", "up_right", "down_left", "up_left"]
##for move in action:
##    a=get_neighbours(move,map)
##    print(move,a)

def get_distance(map1,map2):
    p1 = []
    p1.extend(get_robcoord(map1))
##    print(p1,type(p1))
    p2=[]
    p2.extend(get_robcoord(map2))
##    print(p2,type(p2))
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    return distance

##a=get_distance(map1,map2)
##print(a)
##def cost_generator(map):
    

def exploring_nodes(node):
    print("Exploring Nodes")
    actions = ["down", "up", "left", "right","down_right", "up_right", "down_left", "up_left"]
    goal_node = map2
    node_q = [node]
    final_nodes = []
    visited = []
    node_cost_list=[] #13
    
    final_nodes.append(node_q[0].map.tolist())  # Only writing data of nodes in seen
    node_counter = 0  # To define a unique ID to all the nodes formed

##    for i in range(2):#while node_q:  # UNCOMMENT FOR DEBUGGING 
    while node_q:
        current_root = node_q.pop(0)  # Pop the element 0 from the list
        if current_root.map.tolist() == goal_node.tolist():
            print("Goal reached!", '\n', current_root.map, current_root.node_no)
            draw_map(current_root.map)
            return current_root, final_nodes, visited
        print("THE LENGTH OF NODE Q at the beginning IS: ", len(node_q))

        for move in actions:
            temp_data = get_neighbours(move, current_root.map)
            print(move, '\n', temp_data)
            if temp_data is not None:
                draw_map(temp_data)

                node_counter += 1
                print("node count",node_counter)
                node_cost=20000000000000#8b
                move_cost=get_distance(temp_data,current_root.map)
                print("move cost", move_cost)
                cost_to_come= current_root.cost + move_cost#8c
##                print("cost to come", cost_to_comeself.map = map
                child_node = Node(node_counter, np.array(temp_data), current_root, move, node_cost)  # 9
##                print("node_counter", node_counter,"child node point",child_node.map,"parent",child_node.parent,"move",child_node.act,"cost",child_node.cost)
                if node_cost > cost_to_come : #9a
                    child_node.cost= cost_to_come# 9b
                    Dict1={child_node.cost:child_node}
                    for k in Dict1.keys():
                        pass#print("k",k)
                    for i in Dict1.values():
                        pass#print("i",i)
##                print("node_counter", node_counter,"child node point",child_node.map,"parent",child_node.parent,"move",child_node.act,"cost",child_node.cost)

                if child_node.map.tolist() not in final_nodes:  # 10
                    node_q.append(child_node)#12
                    print("THE LENGTH OF NODE Q after children IS: ", len(node_q))
                    final_nodes.append(child_node.map.tolist())#10a
##                    print(final_nodes)
                    visited.append(child_node)#11
                    node_cost_list.append(child_node.cost)
                    min_cost=min(node_cost_list)
                    for k in Dict1.keys():
                        if k==min_cost:
                            #print("Dict1[k]",Dict1[k])
                            node_q.remove(Dict1[k])
                            node_q.insert(0,Dict1[k])
                    print("THE LENGTH OF NODE Q (after shuffling should be the same as after children) IS: ", len(node_q))                   
    return None, None, None  # return statement if the goal node is not reached

"""
get shortest distance from start vertex to each other vertex
get the previous vertex
3 lists
    1. List to keep track of vetexes we have visited
    2. List of vertexes we haven't visited
    3. Distance between visited nodes and start node
Set the value for the distance from start node to start node as zero
set the value for the distance to all other nodes as 20000
START
Visit start node
    Save all locations from all 8 possible moves in List 2
    Get distance from all locations in List 2 to Start node and save in list3
    Add start node to visited list (list 1)
Check to see which node from list 2 has the smallest distance in list3
Visit vertex closest to start node
    Save all locations from all 8 possible moves in List 2
    Get distance from all new locations to current location
    Add distance form above to distance from current location to start location
        if the value of the (distance of current node to start node) + (distance of current nOde to new node) < value for new node and save in list3
    Add current node to visited list (list 1)
    REMOVE IT FROM LIST 2
REPEAT UNTIL NO MORE IN LIST 2"""




    

start_node=Node(0,map1,None,None,0)
draw_map(map1)
goal, s, v = exploring_nodes(start_node)
##print(move_left(start_node.node_loc))


cv2.waitKey(0)
cv2.destroyAllWindows()


