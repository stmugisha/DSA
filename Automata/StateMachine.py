# A Finite State Machine is an abstract machine that
# consists of a set of states(initial and terminal state(s)),
# a set of input and output events and a state transition function

class StateMachine():
    def __init__(self):
        self.handlers = {}
        self.initial_state = None
        self.terminal_state = []