# keyboardAgents.py
# -----------------
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


from game import Agent
from game import Directions
import random

class KeyboardAgent(Agent):
    """
    An agent controlled by the keyboard.
    """
    # NOTE: Arrow keys also work.
    WEST_KEY  = 'a'
    EAST_KEY  = 'd'
    NORTH_KEY = 'w'
    SOUTH_KEY = 's'
    STOP_KEY = 'q'

    def __init__( self, index = 0 ):

        self.lastMove = Directions.STOP
        self.index = index
        self.keys = []

    # Returns None if no move is ready. This signals the main loop to wait until
    # the player decides the next action.
    def getAction( self, state):
        from graphicsUtils import keys_pressed
        keys = keys_pressed()
        # if keys != []:  # Use this conditional to make Pacman continue in the same dir.
        self.keys = keys

        legal = state.getLegalActions(self.index)
        move = self.getMove(legal)

        return move

    def getMove(self, legal):
        move = None
        if (self.WEST_KEY in self.keys or 'Left' in self.keys) and Directions.WEST in legal:  move = Directions.WEST
        if (self.EAST_KEY in self.keys or 'Right' in self.keys) and Directions.EAST in legal: move = Directions.EAST
        if (self.NORTH_KEY in self.keys or 'Up' in self.keys) and Directions.NORTH in legal:   move = Directions.NORTH
        if (self.SOUTH_KEY in self.keys or 'Down' in self.keys) and Directions.SOUTH in legal: move = Directions.SOUTH
        if (self.STOP_KEY in self.keys) and Directions.STOP in legal: move = Directions.STOP
        return move

class KeyboardAgent2(KeyboardAgent):
    """
    A second agent controlled by the keyboard.
    """
    # NOTE: Arrow keys also work.
    WEST_KEY  = 'j'
    EAST_KEY  = "l"
    NORTH_KEY = 'i'
    SOUTH_KEY = 'k'
    STOP_KEY = 'u'

    def getMove(self, legal):
        move = None
        if (self.WEST_KEY in self.keys) and Directions.WEST in legal:  move = Directions.WEST
        if (self.EAST_KEY in self.keys) and Directions.EAST in legal: move = Directions.EAST
        if (self.NORTH_KEY in self.keys) and Directions.NORTH in legal:   move = Directions.NORTH
        if (self.SOUTH_KEY in self.keys) and Directions.SOUTH in legal: move = Directions.SOUTH
        if (self.STOP_KEY in self.keys) and Directions.STOP in legal: move = Directions.STOP
        return move
