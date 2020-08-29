class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []
        self.cur = 0
    
    def append(self, value):
        if len(self.store) == self.capacity:
            self.store[self.cur] = value
            self.cur = self.cur + 1

            if self.cur == self.capacity:
                self.cur = 0

        else:
            self.store.append(value)
    
    def get(self):
        return self.store