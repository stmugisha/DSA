# Credit: https://www.python-course.eu/finite_state_machine.php

from StateMachine import StateMachine

positive_adjectives = ["great","super", "fun", "entertaining", "easy"]
negative_adjectives = ["boring", "difficult", "ugly", "bad"]

def start_transition(text: str):
    """ Begins state transition starting at the initial/start state."""j
    split_text = text.split()
    word, text = split_text if len(split_text) > 1 else (text, "")
    if word == "Python":
        new_state = "Python_state"
    else:
        new_state = "Null"

    return new_state, text

def python_state_transition(text: str):
    """ Transition from the python state to another state."""
    split_text = text.split()
    word, text = split_text if len(split_text) > 1 else (text, "")
    if word == "is":
        new_state = "is_state"
    else:
        new_state = "Null"

    return new_state, text 