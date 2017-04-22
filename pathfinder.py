#!/usr/bin/env python
# Four spaces as indentation [no tabs]
import sys
import Queue
import math
from common import *
from node import *
from priorityqueue import *

# ==========================================
# PathFinder A Star
# ==========================================

class PathFinder_A_Star:

    def __init__(self):
        # TODO initialize your attributes here if needed
        self.has_solution = False
        self.closeList = {}
        self.openQueue = None
        self.openHash = {}
        self.goal = None
        self.start = None
        self.cost = 0
        self.greedy = False

    # ------------------------------------------
    # Cost
    # ------------------------------------------

    def function(self, p1, p2):
        # TODO priority function to use with the PriorityQueue
        # You are free not to use this function
        # (it is not tested in the unit test)
        return None

    # ------------------------------------------
    # Heuristic
    # ------------------------------------------

    def heuristic(self, p1, p2):
       # TODO heuristic function 
       # Here, you must use Manhattan distance
       # (it is graded in the unit test)
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)



    # ------------------------------------------
    # Solve
    # ------------------------------------------

    def solve(self, map):
        # TODO returns a list of movements (may be empty) 
        # if plan found, otherwise return None.
        self.initProblem(map)
        node = None
        path = []
        actions = None
        while not self.openQueue.empty():
            node = self.getFromQueue()
            if self.isGoal(node):
                self.has_solution = True
                break

            self.closeList[node.getKey()] = node    
            self.evaluateSuccessors(map, node)
        
        if not self.has_solution :
            return None
        self.cost = node.getCost()
        path = self.getPathToGoal(node)
        actions = self.buildActions(path)
        return actions

    # ------------------------------------------
    # Get solvable
    # ------------------------------------------

    def get_solvable(self, map):
        # TODO returns True if plan found, 
        # otherwise returns False
        self.greedy = True
        actions = self.solve(map)
        return actions != None

    # ------------------------------------------
    # Get max tree height
    # ------------------------------------------

    def get_max_tree_height(self, map):
        # TODO returns max tree height if plan found, 
        # otherwise, returns None
        actions = self.solve(map)
        if actions != None:
            return self.cost
        else:
            return None

    # ------------------------------------------
    # Get min moves
    # ------------------------------------------

    def get_min_moves(self, map):
        # TODO returns size of minimal plan to reach goal if plan found, 
        # otherwise returns None
        actions = self.solve(map)
        if actions != None:
            return len(actions)
        else:
            return None



    # ------------------------------------------
    # Aux Methods 
    # ------------------------------------------



    # ------------------------------------------
    # Add a node to the open queue
    # -----------------------------------------
    def addToQueue(self, node):
        priority = 0
        if self.greedy:
            priority = node.getHeuristic()
        else:
            priority = node.getPriority()
        self.openQueue.put(node, priority)
        self.openHash[node.getKey()] = node

    # ------------------------------------------
    # Get a node from the queue and remove it. 
    # ------------------------------------------
    def getFromQueue(self):
        node = self.openQueue.get()
        del self.openHash[node.getKey()]
        return node

    # ------------------------------------------
    # calc heuristic of point to the goal
    # ------------------------------------------
    def heuristicToGoal(self, p1):
        return self.heuristic(p1, self.goal)

    def initProblem(self, map):
        self.start = map.start
        self.cost = 0
        self.goal = map.goal
        self.closeList = {}
        self.openQueue = None
        self.openHash = None
        self.initOpenQueue(map)


    def initOpenQueue(self, map):
       self.openQueue = PriorityQueue()
       self.openHash = {}
       heuristic = self.heuristicToGoal(self.start)
       start_node = Node(self.start, 0, heuristic)
       start_node.setParent(None)
       self.addToQueue(start_node)


    def isGoal(self, node):
        isXGoal = self.goal.x == node.getX()
        isYGoal = self.goal.y == node.getY()
        return isXGoal and isYGoal
        

    def notInCloseList(self, node):
        return not node.getKey() in self.closeList


    def evaluateSuccessors(self, map, node):
        successors = map.successors(node.getX(), node.getY())
        for successor in successors:
            node_suc = Node(successor, 0, 0)
            node_suc.setParent(node)
            self.evaluateSuccessor(node, node_suc)

    # ------------------------------------------
    # Set the cost and heuristic to a node, cosidering the previus node
    # ------------------------------------------
    def setCostAndHeuristic(self, node, node_suc):
        successor_cost = node.getCost() + 1;
        heuristic = self.heuristicToGoal(node_suc.getPoint())
        node_suc.setCost(successor_cost) 
        node_suc.setHeuristic(heuristic)

    def treatIfNodeIsInOpenList(self, node, node_suc):
        key = node_suc.getKey()
        inOpenList = self.openHash[key]
        if node_suc.getCost() < inOpenList.getCost():
            inOpenList.setParent(node)
            inOpenList.setHeuristic(node_suc.getHeuristic())
            inOpenList.setCost(node_suc.getCost())

    def evaluateSuccessor(self, node, node_suc):
        if self.notInCloseList(node_suc):
            self.setCostAndHeuristic(node,node_suc)
            if not node_suc.getKey() in self.openHash:
                self.addToQueue(node_suc)
            else:
                self.treatIfNodeIsInOpenList(node,node_suc)


    def getPathToGoal(self, node):
        path = []
        current = node
        while  current != None:
            path.append(current.getPoint())
            current = current.getParent()
        path.reverse()
        return path

    # ------------------------------------------
    # Return a list of actions considering the direction tuple
    # -----------------------------------------
    def buildActions(self, path):
        actions = []
        i = 0    
        for i in range(1,len(path)):
            current = path[i-1]
            next    = path[i]
            direc = direction(current.x, current.y, next.x,next.y)     
            actions.append(direc)
        return actions

# ------------------------------------------
# Main
# ------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 2:
        map_name = sys.argv[1]
    else:
        map_name = DEFAULT_MAP
    print "Loading map: " + map_name
    plan = PathFinder_A_Star().solve(read_map(map_name))
    if plan == None:
        print "No plan was found"
    else:
        print "Plan found:"
        for i, move in enumerate(plan):
            if move == MOVE_UP:
                print i, ": Move Up"
            elif move == MOVE_DOWN:
                print i, ": Move Down"
            elif move == MOVE_LEFT:
                print i, ": Move Left"
            elif move == MOVE_RIGHT:
                print i, ": Move Right"
            else:
                print i, ": Movement unknown = ", move
