# Author: Stephen Mugisha
# FSM exceptions

class InitializationError(Exception):
        """
        State Machine InitializationError
        exception raised.
        """
        def __init__(self, message, payload=None):
            self.message = message
            self.payload = payload #more exception args

        def __str__(self):
            return str(self.message)

