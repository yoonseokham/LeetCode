class Allocator:
    def __init__(self, n: int):
        self._memory = [0 for _ in range(n)]

    @property
    def memory(self):
        return self._memory

    def allocate(self, size: int, mID: int) -> int:
        counter = 0
        for i, value in enumerate(self.memory):
            if value:
                counter = 0
            else:
                counter += 1
                if counter == size:
                    for j in range(size):
                        self.memory[i - j] = mID
                    return i - size + 1
        return -1

    def free(self, mID: int) -> int:
        counter = 0
        for i, value in enumerate(self.memory):
            if value == mID:
                self.memory[i] = 0
                counter += 1
        return counter
