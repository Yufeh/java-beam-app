class Memory:
    def __init__(self):
        self._messages = []

    def add(self, message: str) -> None:
        self._messages.append(message)

    def list(self):
        return list(self._messages)
