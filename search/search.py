# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
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

    #declare stack of unexplored nodes
    unexploredNodes = util.Stack()

    #declare and init starting point
    start = problem.getStartState()

    #add starting point to stack
    unexploredNodes.push((start, []))

    #declare set of visited nodes
    visited = set()

    #iterate through all nodes until all have been explored or until the goal is found
    while not unexploredNodes.isEmpty():

        #pop a node to explore
        state, path = unexploredNodes.pop()

        #check if the node is the goal, return if yes
        if problem.isGoalState(state):
            return path

        #expand if node is not visited
        if state not in visited:
            visited.add(state)
            for succ, action, _ in problem.getSuccessors(state):
                if succ not in visited:
                    unexploredNodes.push((succ, path + [action]))

    #code falls through if there is no solution, return nothing
    return []

def breadthFirstSearch(problem):

    #declare queue of unexplored nodes
    unexploredNodes = util.Queue()

    #initialize starting point
    start = problem.getStartState()


    unexploredNodes.push((start, []))

    # Track visited nodes
    visited = set()

    while not unexploredNodes.isEmpty():
        state, path = unexploredNodes.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)
            for succ, action, _ in problem.getSuccessors(state):
                if succ not in visited:
                    unexploredNodes.push((succ, path + [action]))

    return []

def uniformCostSearch(problem):
    # Priority queue for UCS: (state, path, cost)
    unexploredNodes = util.PriorityQueue()
    start = problem.getStartState()
    unexploredNodes.push((start, [], 0), 0)
    visited = {}

    while not unexploredNodes.isEmpty():
        state, path, cost = unexploredNodes.pop()

        if problem.isGoalState(state):
            return path

        # Only expand if this is the lowest cost to this state seen so far
        if state not in visited or cost < visited[state]:
            visited[state] = cost
            for succ, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost
                unexploredNodes.push((succ, path + [action], newCost), newCost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from search import util
    frontier = util.PriorityQueue()
    start = problem.getStartState()
    frontier.push((start, [], 0), heuristic(start, problem))
    visited = {}

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()

        if problem.isGoalState(state):
            return path

        # Only expand if this is the lowest cost to this state seen so far
        if state not in visited or cost < visited[state]:
            visited[state] = cost
            for succ, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost
                priority = newCost + heuristic(succ, problem)
                frontier.push((succ, path + [action], newCost), priority)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
