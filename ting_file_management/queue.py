class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None

        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index > self.size() - 1:
            raise IndexError

        return self._data[index]

    def size(self):
        return len(self._data)

    def is_empty(self):
        return not bool(self._data)
