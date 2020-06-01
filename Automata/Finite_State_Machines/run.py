# Credit: https://www.python-course.eu/finite_state_machine.php

from StateMachine import StateMachine

positive_adjectives = ["great","super", "fun", "entertaining", "easy"]
negative_adjectives = ["boring", "difficult", "ugly", "bad"]

def start_transition(text: str):
    """ Begins state transition starting at the initial/start state."""
    split_text = text.split()
    word, text = split_text if len(split_text) > 1 else (text, "")
    if(word == "Python"):
        new_state = "Python_state"
    else:
        new_state = "Null"

    return new_state, text

def python_state_transition(text: str):
    """ Transition from the python state to another state."""
    split_text = text.split()
    word, text = split_text if len(split_text) > 1 else (text, "")
    if(word == "is"):
        new_state = "is_state"
    else:
        new_state = "Null"

    return new_state, text

def is_state_transition(text: str):
    """ Transition control from the is_state."""
    split_text = text.split()
    word, text = split_text if len(split_text) > 1 else (text, "")
    if(word == "not"):
        new_state = "not_state"
    elif word in positive_adjectives:
        new_state = "positive_state"
    elif word in negative_adjectives:
        new_state = "negative_state"
    else:
        new_state = "Null"

    return new_state, text

def  not_state_transition(text: str):
    """ Transition control from the not_state."""
    split_text = text.split()
    word, text = split_text if len(split_text) > 1 else (text, "")
    if word in positive_adjectives:
        new_state = "negative_state"
    elif word in negative_adjectives:
        new_state = "positive_state"
    else:
        new_state = "Null"

    return new_state, text
    
    