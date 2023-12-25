class Robot:

    def __init__(self, width: int, height: int):
        self.direction = "E"
        self.position = [0,0]
        self.x = width
        self.y = height
        self.parameter = ((self.x - 1) * 2) + ((self.y - 1) * 2)

    def step(self, num: int) -> None:
        if num == 0:
            return
        temp = num % self.parameter
        if temp == 0 and self.position[0] == 0 and self.position[1] == 0:
            self.direction = "S"
        elif temp == 0 and self.position[0] == 0 and self.position[1] == self.y -1:
            self.direction = "W"
        elif temp == 0 and self.position[0] == self.x - 1 and self.position[1] == 0:
            self.direction = "E"
        elif temp == 0 and self.position[0] == self.x -1 and self.position[1] == self.y -1:
            self.direction = "N"
        self.check(temp)
    # def step(self, num: int) -> None:
    def check(self, num):
        # num = num % self.parameter
        if self.direction in ["E","W"]:
            if self.direction == "E":
                if self.x - self.position[0] > num:
                    self.position[0] += num
                else:
                    step = self.x - self.position[0] - 1
                    self.position[0] += step
                    self.direction = "N"
                    self.check(num-step)
            else:
                if self.position[0] >= num:
                    self.position[0] -= num
                else:
                    step = self.position[0]
                    self.position[0] = 0 
                    self.direction = "S"
                    self.check(num-step)
        else:
            if self.direction == "N":
                if self.y - self.position[1] > num:
                    self.position[1] += num
                else:
                    step = self.y - self.position[1] - 1
                    self.position[1] += step
                    self.direction = "W"
                    self.check(num-step)
            else:
                if self.position[1] >= num:
                    self.position[1] -= num
                else:
                    step = self.position[1]
                    self.position[1] = 0 
                    self.direction = "E"
                    self.check(num-step)

    def getPos(self) -> List[int]:
        return self.position

    def getDir(self) -> str:
        direction = {"E":"East" ,"N":"North", "S":"South", "W":"West"}
        return direction[self.direction]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()