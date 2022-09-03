class Car:
    def __init__(self,p,s,c):
        self.price = p
        self.speed = s
        self.color = c
    
    def __str__(self):
        return "Price: "+str(self.price)+" Speed: "+str(self.speed)+" Color: "+self.color
    
    def __repr__(self):
        return "Price: "+str(self.price)+" Speed: "+str(self.speed)+" Color: "+self.color
    def __lt__(self,oth):
        # return (oth.price > self.price)
        # return (oth.speed > self.speed)
        # return self.color < oth.color
        return (oth.price,-oth.speed) > (self.price,-self.speed)


cars = [0 for i in range(5)]
cars[0] = Car(1000,50,"Blue")
cars[1] = Car(10000,80,"Red")
cars[2] = Car(200,70,"Black")
cars[3] = Car(200,50,"White")
cars[4] = Car(1000,80,"Red")

for c in cars:
    print(c)

print("-------------------------")
def Ckey(c):
    return (c.price,-c.speed)
# cars.sort()
cars = sorted(cars,key=Ckey)

for c in cars:
    print(c)