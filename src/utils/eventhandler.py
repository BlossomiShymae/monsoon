class EventHandler:
    """Represents an event handler that resembles C# equivalent.
    """

    def __init__(self):
        self.event_delegate_list = []

    def __iadd__(self, action):
        self.event_delegate_list.append(action)
        return self

    def invoke(self, sender, event_args):
        for action in self.event_delegate_list:
            action(sender, event_args)
