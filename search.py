# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
   
    """Available functions:

    *.push()
    *.pop() 
    *.isEmpty()
    *.getSuccessors()
    *.getStartState()
    *.isGoalState()


    """

    """

    fringe = util.Stack()
    # Making a new instance of the class stack and assigning to fringe
    successors = problem.getSuccessors(problem.getStartState())
    for successor in successors:
        fringe.push((successor[0], [successor[1]], []))
    #fringe.push( (problem.getStartState(), [], []) )
    #explored = set()
    # We are pushing [] [] along with problem.getStartState as it expects a 
    # tuple and we'll get an error stated as:
    ########## Python error: need more than two values to unpack
    # so we're giving empty values for the direction and the cost since for initial
    # state neither of them exist
    # Initializing the frontier using the initial state of the problem
    # If case and else case must end with a : in the end of the same line
    # otherwise it won't work
    #  if fringe.isEmpty == True : #True must be in capitals in python
    #      print "failure"
    # else:
    ## Not a good method as it isn't written in the problem statement that
    ## we need to print "failure" in case it doesn't work
    while fringe.isEmpty() != True:
    ## We'll use while here instead of if as while keeps on looping until the
    ## condition becomes false, and if would only run once so this is better
        leafNode, actions, exploredNodes = fringe.pop()
    ## adding the value being popped to the ones written above    
        for currentNode, direction, steps in problem.getSuccessors(leafNode):
    ## Checking for successors
            if not currentNode in exploredNodes:
    #Although, unless would be better in ruby but it's not available in python (CHECK LATER?)
    # using if not instead of unless
                if problem.isGoalState(currentNode):
    # return if we've reached the goal state
                    return actions + [direction]
    # returning the value in the correct format
                fringe.push((currentNode, actions + [direction], exploredNodes + [leafNode] ))
    # if not reached goal state then push the values into the stack
    return[]
    """

    "util.raiseNotDefined()"

    """

    exploredNodes = set()

    successors = problem.getSuccessors(problem.getStartState())
    # print "SUCCESSORS::"
    # print successors
    exploredNodes.add(problem.getStartState())

    stack = util.Stack()

    for successor in successors:
        stack.push((successor[0], [successor[1]]))
    # for successor in successors:
    #     stack.push((successor[0], [successor[1]]))
    # print "SUCCESSORS[0]"
    # print successor[0]
    # print "SUCCESSORS[1]"
    # print [successor[1]]
      
    while stack.isEmpty() != True:
        tup = stack.pop()
        # print "TUPLE::::"
        # print tup[1]
        if tup[0] in exploredNodes:
            continue
        else:
            exploredNodes.add(tup[0])
        if problem.isGoalState(tup[0]):
            return tup[1]
        else:
            successors = problem.getSuccessors(tup[0])
            for successor in successors:
                updated_move_list = tup[1][:]
                # print "Move List"
                # print updated_move_list
                updated_move_list.append(successor[1])
                stack.push((successor[0], updated_move_list))

    return []

    """

    ## Initialize the frontier using the initial state of problem
    frontier = util.Stack()
    ## Initializing the explored set to be empty
    exploredNodes = set()
    ## a list might work better for python
    childrens = problem.getSuccessors(problem.getStartState())
    print "Childrens::"
    print childrens

    for childrens in childrens:
        frontier.push((childrens[0], [childrens[1]]))
        print "Childrens[0]"
        print childrens[0]
        print "Childrens[1]"
        print [childrens[1]]
      
    while frontier.isEmpty() != True:
        sol = frontier.pop()
        ## choose a leaf node and remove it from frontier
        print "TUPLE::::"
        print sol[1]
        ## Add the first value to explored nodes so that we don't get it again
        if sol[0] in exploredNodes:
            continue
        else:
            exploredNodes.add(sol[0])
        ## Check if node contains a goal state?
        if problem.isGoalState(sol[0]):
            return sol[1]
            ## !!!!! Check that it returns the next element otherwise last element won't be there like previous try
        else:
            exploredNodes.add(problem.getStartState())
            ## Add the node to the explored state
            childrens = problem.getSuccessors(sol[0])
            for childrens in childrens:
                updated_move_list = sol[1][:]
                print "Move List"
                print updated_move_list
                updated_move_list.append(childrens[1])
                frontier.push((childrens[0], updated_move_list))
                ## Add the successors of the current state
                ## Add the nodes to frontier and get the final answer, hopefully

    return []

    """

    exploredNodes = set()

    fringe = util.Stack()

    children = problem.getSuccessors(problem.getStartState())
    """

    ###############################
    #What DFS may be doing wrong?###############################################
    ## It's trying to go too deep without looking for nodes which might be near
    ## which might be considered the better thing to do as our maze is not very
    ## deep as such, but it may be better for very deep mazes 

    #############################################################
    ######### NOTE ##############################################
    ##################### CHECK IF DFS IS BETTER FOR ALL CASES?
    ############################################################

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    
    ## Initialize the frontier using the initial state of problem
    frontier = util.Queue()
    ## Initializing the explored set to be empty
    exploredNodes = set()
    ## a list might work better for python
    childrens = problem.getSuccessors(problem.getStartState())
    print "Childrens::"
    print childrens

    for childrens in childrens:
        frontier.push((childrens[0], [childrens[1]]))
        print "Childrens[0]"
        print childrens[0]
        print "Childrens[1]"
        print [childrens[1]]
      
    while frontier.isEmpty() != True:
        sol = frontier.pop()
        ## choose a leaf node and remove it from frontier
        print "TUPLE::::"
        print sol[1]
        ## Add the first value to explored nodes so that we don't get it again
        if sol[0] in exploredNodes:
            continue
        else:
            exploredNodes.add(sol[0])
        ## Check if node contains a goal state?
        if problem.isGoalState(sol[0]):
            return sol[1]
            ## !!!!! Check that it returns the next element otherwise last element won't be there like previous try
        else:
            exploredNodes.add(problem.getStartState())
            ## Add the node to the explored state
            childrens = problem.getSuccessors(sol[0])
            for childrens in childrens:
                updated_move_list = sol[1][:]
                print "Move List"
                print updated_move_list
                updated_move_list.append(childrens[1])
                frontier.push((childrens[0], updated_move_list))
                ## Add the successors of the current state
                ## Add the nodes to frontier and get the final answer, hopefully

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
