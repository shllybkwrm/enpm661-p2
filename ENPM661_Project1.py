# ENPM661, Spring 2020, Project 1
# Shelly Bagchi


import numpy as np

indexCounter = 0;

class Node:

    node_state = [];
    node_index = 0;
    parent_node_index = 0;
    
    (i,j) = (0,0);

    code = "";

    def __init__(self, list=[[0,0,0],[0,0,0],[0,0,0]], parent_index=0):
        self.node_state = np.array(list);
        self.parent_node_index = parent_index;

        
        global indexCounter;
        indexCounter += 1;
        self.node_index = indexCounter;

        self.code = self.EncodeState();
        (self.i,self.j) = self.BlankTileLocation();

    
    def EncodeState(self):
        #code = "";
        # Match output textfile
        #for i in range(3):
        #    for j in range(3):
        #        code += str(self.node_state[i,j]);
        
        code_1 = ' '.join(str(x) for x in self.node_state[:,0]);
        code_2 = ' '.join(str(x) for x in self.node_state[:,1]);
        code_3 = ' '.join(str(x) for x in self.node_state[:,2]);

        return ' '.join([code_1, code_2, code_3]);


    def BlankTileLocation(self):
        for i in range(3):
            for j in range(3):
                if self.node_state[i,j]==0:
                    return (i,j);
                else: pass

    
    def ActionMoveLeft(self):
        (i,j) = (self.i,self.j);
        game_state = self.node_state.copy();
        if j>0:
            game_state[i,j] = game_state[i,j-1];
            game_state[i,j-1] = 0;
            return Node(game_state, self.node_index);
        else: return None;

    def ActionMoveRight(self):
        (i,j) = (self.i,self.j);
        game_state = self.node_state.copy();
        if j<2:
            game_state[i,j] = game_state[i,j+1];
            game_state[i,j+1] = 0;
            return Node(game_state, self.node_index);
        else: return None;

    def ActionMoveUp(self):
        (i,j) = (self.i,self.j);
        game_state = self.node_state.copy();
        if i>0:
            game_state[i,j] = game_state[i-1,j];
            game_state[i-1,j] = 0;
            return Node(game_state, self.node_index);
        else: return None;

    def ActionMoveDown(self):
        (i,j) = (self.i,self.j);
        game_state = self.node_state.copy();
        if i<2:
            game_state[i,j] = game_state[i+1,j];
            game_state[i+1,j] = 0;
            return Node(game_state, self.node_index);
        else: return None;
    
    def GetChildren(self):
        ChildList = [];

        Child = self.ActionMoveLeft();
        ChildList.append(Child) if Child!=None else None;
        Child = self.ActionMoveRight();
        ChildList.append(Child) if Child!=None else None;
        Child = self.ActionMoveUp();
        ChildList.append(Child) if Child!=None else None;
        Child = self.ActionMoveDown();
        ChildList.append(Child) if Child!=None else None;

        print(" > Found children,", len(ChildList));
        return ChildList;


    def Print(self):
        print(self.node_state[:,0], self.node_state[:,1], self.node_state[:,2]);


def CheckGoal(node):
    goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])
    return np.array_equal(node.node_state, goal_state);



def AddNodes(NewNodes):
    global Matrix_8puzzle_Nodes, Matrix_8puzzle_Indices, Matrix_8puzzle_Parents;
    global NodesInfoFile, AllNodesFile;

    for node in NewNodes:
        # Need to check if new node STATE or not

        if node.code not in Matrix_8puzzle_States:
            print("Adding node", node.node_index);

            #Matrix_8puzzle_Nodes.append(node);
            Matrix_8puzzle_Nodes[node.node_index] = node;
            Matrix_8puzzle_Indices.append(node.node_index);
            Matrix_8puzzle_Parents.append(node.parent_node_index);
            Matrix_8puzzle_States.append(node.code);

            AllNodesFile.write(node.code+'\n');
            NodesInfoFile.write(str(node.node_index) + ' ' + str(node.parent_node_index) + ' 0 \n');

            #print(node.node_state);
            #print("Code:", node.code);
            if CheckGoal(node):
                print("--- Goal found! ---");
                return True;

        else:
            print("Game state already visited!  Skipping node", node.node_index);

    return False;


def BuildTree(NodeList):
    res = False;
    ChildList = [];

    # Build tree level by level
    print(">> Tree level ", NodeList[0].parent_node_index+1);
    for node in NodeList:
        Children = node.GetChildren();
        res = AddNodes(Children);
        if res:  # Returns true if goal found
            return;

        ChildList.extend(Children);

    BuildTree(ChildList);


def Backtrack():
    print('\n', ">> Backtracking...");
    global Matrix_8puzzle_Nodes, Matrix_8puzzle_Indices, Matrix_8puzzle_Parents;
    global nodePathFile;
    path = [];

    # Start with goal, should be last visited node
    goal_node = Matrix_8puzzle_Nodes[Matrix_8puzzle_Indices[-1]];
    parent_index = goal_node.parent_node_index;
    
    print(goal_node.node_state);
    print("Code:", goal_node.code);
    path.append(goal_node.code);
    #nodePathFile.write(goal_node.code+'\n');  # Need to reverse this!!

    while parent_index != 0:
        parent = Matrix_8puzzle_Nodes[parent_index];
    
        print(parent.node_state);
        print("Code:", parent.code);
        path.append(parent.code);
        #nodePathFile.write(parent.code+'\n');

        # Get next parent
        parent_index = parent.parent_node_index;

    # Write to file in traversal order (reversed)
    for node_code in reversed(path):
        nodePathFile.write(node_code + '\n');

    return;


# See https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
# https://datawookie.netlify.com/blog/2019/04/sliding-puzzle-solvable/
def Solvable(node):
    game_state = node.node_state.copy();
    state_list = game_state.flatten();
    #print(state_list);

    # Count number of inversions (number swaps)
    num_inversions = 0;
    for i in range(8):
        for j in range(i+1, 9):
            if state_list[j] and state_list[i] and state_list[i] > state_list[j]:
                  num_inversions += 1; 

    # Check if odd or even & return (odd -> unsolvable!)
    print("(Inversions: ", num_inversions, ") \n");
    return (num_inversions%2 == 0);


# ----- MAIN -----

# Global variables to hold visited nodes
Matrix_8puzzle_Nodes = {};
Matrix_8puzzle_Indices = [];
Matrix_8puzzle_Parents = [];
Matrix_8puzzle_States = [];  # Plaintext game states


# File objects for output
nodePathFile = open('nodePath.txt', 'w');
NodesInfoFile = open('NodesInfo.txt', 'w');
AllNodesFile = open('Nodes.txt', 'w');


# Get user input for initial game state
print("Enter initial game state:");
print("Enter first row of puzzle, e.g. \'1 2 3\'");
input1 = input();
print("Enter second row of puzzle");
input2 = input();
print("Enter third row of puzzle");
input3 = input();

# Convert input
row1 = [int(a) for a in input1.split(' ')]; 
row2 = [int(a) for a in input2.split(' ')]; 
row3 = [int(a) for a in input3.split(' ')]; 
#print(row1, row2, row3) ;
puzzle_state = [row1, row2, row3];
#print(puzzle_state);

# Check if valid
if len(row1)!=3 or len(row2)!=3 or len(row3)!=3:
    print("Input was incorrectly formatted.  Exiting...");
    exit();

# Create initial node
root_node = Node(puzzle_state);
print(root_node.node_state, '\n');
#  Check if initial state is solvable
if not Solvable(root_node):
    print("Entered game state is unsolvable!  Exiting...");
    exit();
    #quit();

AddNodes([root_node]);
#print(root_node.node_state);
#root_node.Print();
print("Empty tile starts at ", root_node.i, root_node.j);

BuildTree([root_node]);

Backtrack();



#print(Matrix_8puzzle_Nodes);
print("Indices visited: ", Matrix_8puzzle_Indices);
print("Parents of nodes: ", Matrix_8puzzle_Parents);
#print(Matrix_8puzzle_States);


nodePathFile.close();
NodesInfoFile.close();
AllNodesFile.close();