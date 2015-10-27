# valueIterationAgents.py
# -----------------------
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


import mdp, util
import sys

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        availableStates = self.mdp.getStates()
        
        
        
        


        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        ## should return a utility function (maximize reward, obv)
        ## we need to take in:
        ### States S
        ### Actions A
        ### Transition model P(s'|s,a)
        ### Rewards R(s)
        ### discount (delta)
        ### epsilon is max permissible error

        ## repeat (run a loop for all?)
        ## for loop: (all states in s)
        ## apply formula for value-iteration
        ## if case: (or maybe for by restricting it within a condition)
        for i in range(self.iterations):
          vs = self.values.copy()
          for state in availableStates:
            availableActions = self.mdp.getPossibleActions(state)
            
            
            
            base_value = -sys.maxint
            for action in availableActions:
              sum = 0
              for trans_state, probOfAction in self.mdp.getTransitionStatesAndProbs(state, action):
                ## utility of a state is the immediate reward for that state plus the
                ## the expected discount utility of the next state
                #statesAndProbs = self.mdp.getTransitionStatesAndProbs(state, action)
                rewardForState = self.mdp.getReward(state, action, trans_state)

                sum += probOfAction*(rewardForState + self.discount* self.getValue(trans_state))
                if base_value <= sum:
                  base_value = sum
                  self.values[state] = base_value

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()

        qValue = 0
        for trans_state, probOfAction in self.mdp.getTransitionStatesAndProbs(state, action):

          rewardForState = self.mdp.getReward(state, action, trans_state)
                ## utility of a state is the immediate reward for that state plus the
                ## the expected discount utility of the next state
          qValue += probOfAction*(rewardForState + self.discount* self.getValue(trans_state))
        return qValue


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        terminalState = self.mdp.isTerminal(state)
        availableActions = self.mdp.getPossibleActions(state)

        if terminalState or not availableActions:
          return None
        #max(iterable[, key])
        
        for action in availableActions:
          return max(self.computeQValueFromValues(state, action), action)

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
