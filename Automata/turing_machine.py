# The Turing machine is a mathematical model of a computer

class Tape():
    blank = " "
    def __init__(self, tape_string=""):
        self.__tape = dict((enumerate(tape_string)))

    def __str__(self):
        """ Retrieves and returns a tape string."""
        string = ""
        min_used_index = min(self.__tape.keys())
        max_used_index =max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            string += self.__tape[i]
        return string

    def __setitem__(self, key, value):
        """ Enables access to writing data to the tape."""
        self.__tape[key] = value


    def __getitem__(self, index):
        """ Reading tape-strings/objects via indexing."""
        if index in self.__tape:
            return self.__tape[index]
        return Tape.blank


class TuringMachine():
    def __init__(self, 
                 tape = "",
                 blank = " ",
                 initial_state = "",
                 final_state = None,
                 transition_function = None
                 ):
        self.__tape = Tape()
        self.__head_position = 0
        self.__blank = blank
        self.__current_state = initial_state
        
        if transition_function == None:
            self.__transition_function = {}
        self.__transition_function = transition_function

        if final_state == None:
            self.__final_state = set()
        self.__final_state = set(final_state)

    def get_tape(self):
        return str(self.__tape)

    def step(self):
        value_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, value_under_head)
        if(x in self.__transition_function):
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if(y[2] == "R"):
                self.__head_position += 1
            elif(y[2] == "L"):
                self.__head_position -= 1
            self.__current_state = y[0]

    def final(self):
        if self.__current_state in self.__final_state:
            return True
        return False


if __name__=="__main__":
    initial_state = "init"
    acceptor_states = ["final"]
    transition_function = {("init", "0") : ("init", "1", "R"),
                           ("init", "1") : ("init", "0", "R"),
                           ("init", " ") : ("final", " ", "N")
                           }
    final_states = {"final"}

    tm = TuringMachine(tape="010011 ",
                       initial_state="init",
                       final_state=final_states,
                       transition_function=transition_function
                       )

    print(f"Input to tape: {tm.get_tape()}")

    while not tm.final():
        tm.step()

    print(f"Result from turing computation: {tm.get_tape()}")
        
