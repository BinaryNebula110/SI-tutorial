class entity:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.xspeed = dx
        self.yspeed = dy
    
    def updatepos(self):
        self.x += self.dx*dt
        self.y += self.dy*dt
        
class enemy(entity):
    def __init__(self, x, y, xspeed, yspeed):
        super().__init__(x, y, xspeed, yspeed)
    
    def mvup(self):
        print("you shouldnt be seing this yet...")