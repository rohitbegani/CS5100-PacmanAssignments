# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import sys
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        ######### (self.evaluationFunction). 

        # we're evaluating
        # ************ states ************* rather than actions, as we were for the reflex agent.
        # Look-ahead agents evaluate future states whereas reflex agents evaluate actions from the current state.

        # Pacman is always agent 0, and the agents move in order of increasing agent index.

        # All states in minimax should be GameStates, either passed in to getAction 
        # or generated via GameState.generateSuccessor.

        # the autograder will be very picky about how many times you call GameState.generateSuccessor

        #util.raiseNotDefined()

        #function MINIMAX-DECISION(state) returns an action
        #return arg max Actions MIN-VALUE(RESULT(state,a))

        # function MAX-VALUE(state) returns a utility value
        #  if TERMINAL-TEST(state) then return UTILITY(state)
        #  v <- infinity
        # for each a in Actions(state) do
        #  v <- MAX (v, MIN-VALUE (RESULT (s,a )))

        # function MIN-VALUE(state) returns a utility value
        #  if TERMINAL-TEST(state) then return UTILITY(state)
        #  v <- infinity
        # for each a in Action(state) do
        #   v <- MIN(v, MAX-VALUE(RESULT(s,a )))
        # return v


        #########################################################
        ### The pacman rushes to the closest ghost because he's trying to finish the game as quickly
        ### as possible and save the penalty for living.
        ### This is so, because the pacman understands that in this situation it is doomed.
        #########################################################

        #function MINIMAX-DECISION(state) returns an action
        def miniMaxDecision(gameState, depth = -1, s = -1):
          s += 1
          s %=  gameState.getNumAgents()
          #print s
          if s == 0 :
              depth += 1
          if gameState.isWin() or gameState.isLose() or depth == self.depth:
              return self.evaluationFunction(gameState)
              # function MAX-VALUE(state) returns a utility value
              #  if TERMINAL-TEST(state) then return UTILITY(state)

              # function MIN-VALUE(state) returns a utility value
              #  if TERMINAL-TEST(state) then return UTILITY(state)

          if s == 0 :
              v = maxValue(gameState, depth)
              #print v
              return v
          else :
              v = minValue(gameState, depth, s)
              return v
              #return v
      
        # function MAX-VALUE(state) returns a utility value  
        def maxValue(gameState, depth):
            #  v <- -infinity
            max = -sys.maxint #to get the negative of max value ~ infintity
            actions = gameState.getLegalActions(0) #get all the legal actions
            if depth == 0:
                max = (max, 'Stop')
                ## run two loops one for final state and else
                for a in actions :
                    successor = gameState.generateSuccessor(0,a)
                    v = ( miniMaxDecision(successor, depth, 0), a)
                    if v[0] > max[0] :
                        max = v
            else : 
                # for each a in Actions(state) do
                #  v <- MAX (v, MIN-VALUE (RESULT (s,a )))
                # run a loop to match and change
                for a in actions :
                    successor = gameState.generateSuccessor(0,a)
                    v = miniMaxDecision(successor, depth, 0)
                    if v > max : #check if v is more than the max till now
                        max = v  #replace max with v so now v is the max value
            return max #return max
    
        # function MIN-VALUE(state) returns a utility value
        def minValue(gameState, depth, ghosts):
            #  v <- infinity
            min = sys.maxint  # compare with infinity
            actions = gameState.getLegalActions(ghosts)  # take all the available actions for the agent

            if len(actions) == 0:   # if list of actions is zero
              return (self.evaluationFunction(gameState)) # return the gamestate

            # for each a in Action(state) do
            #   v <- MIN(v, MAX-VALUE(RESULT(s,a )))
            # do same as above but check for the minimum value
            for a in actions :  
                successor = gameState.generateSuccessor(ghosts, a)
                v = miniMaxDecision(successor, depth, ghosts) #state
                if v < min :
                    min = v
            return min #return min 

        #return arg max Actions MIN-VALUE(RESULT(state,a))
        action = miniMaxDecision(gameState)
        return action[1]

     

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

