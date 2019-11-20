class MinMaxStack:
    def __init__(self):
        self.values = []
        self.min_max = [[float('inf'), float('-inf')]]

    def pop(self):
        self.min_max.pop()
        return self.values.pop()

    def push(self, number):
        prev_min, prev_max = self.min_max[-1]
        new_min, new_max = min(prev_min, number), max(prev_max, number)
        self.min_max.append([new_min, new_max])
        self.values.append(number)

    def peek(self): return self.values[-1] if len(self.values) > 0 else None

    def getMin(self): return self.min_max[-1][0]

    def getMax(self): return self.min_max[-1][1]
