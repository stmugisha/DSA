# A Finite State Machine is an abstract machine that
# consists of a set of states(initial and terminal state(s)),
# a set of input and output events and a state transition function
import exceptions as e

class StateMachine():
    """Implements a Finite state machine."""
    def __init__(self):
        self.states = {}  
        self.initial_state = None
        self.terminal_states = []

    def add_state(self, name, state, terminal_state=False):
        """ Add a new state to the set of states/handlers."""
        name = name.upper()
        self.states[name] = state
        if terminal_state:
            self.terminal_states.append(name)

    def set_start(self, name):
        """ Initial state setter."""
        self.initial_state = name.upper()

    def run(self, data):
        """ Run state machine."""
        try:
            state = self.states[self.initial_state]
        except:
            raise e.InitializationError("Initial_state must be set before run!")
        if not self.terminal_states:
            raise e.InitializationError("There must be atleast 1 terminal/end state")

        while True:
            (new_state, data) = state(data)
            if new_state.upper() in self.terminal_states:
                print(f"Final_state: {new_state}")
                break
            else:
                state = self.states[new_state.upper()]


