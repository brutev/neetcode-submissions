class MinStack:

    def __init__(self):
      self.test = []
      self.minTest = []  

    def push(self, val: int) -> None:
        self.test.append(val)


    def pop(self) -> None:
        self.test.pop()

    def top(self) -> int:
        return self.test[-1]
        

    def getMin(self) -> int:
        self.minTest = min(self.test)
        return self.minTest        
