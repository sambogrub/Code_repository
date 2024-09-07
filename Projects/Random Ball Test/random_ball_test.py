import random

red = []
blue = []

num_red = 13
num_blue = 20

num_tests = 1000

class Ball():
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

class Bag():
    def __init__(self):
        self.bag = []

    def add_ball(self, ball):
        self.bag.append(ball)

    def remove_specific_ball(self, color):
        if self.bag:
            for i, ball in enumerate(self.bag):
                if ball.color == color:
                    return self.bag.pop(i)
            return None   
        else:
            return None

    def get_random_ball(self):
        if self.bag:
            index = random.randrange(len(self.bag))

            return self.bag.pop(index)
        else:
            return None
        
    def bag_size(self):
        return len(self.bag)
    
    def bag_contents(self):
        balls = []
        for ball in self.bag:
            balls.append(ball.color)

        return balls

results = []
for i in range(num_tests):

    bag = Bag()

    for i in range(num_blue):
        bag.add_ball(Ball('blue'))

    for i in range(num_red):
        bag.add_ball(Ball('red'))

  

    while bag.bag_size() > 1:
        
        ball_1 = bag.get_random_ball()
        ball_2 = bag.get_random_ball()
        
        if ball_1.color == ball_2.color:
            bag.add_ball(ball_1)
            bag.add_ball(ball_2)
           
            if bag.remove_specific_ball('blue') != None:
                continue
            else:
                break

                    
        else:
            bag.add_ball(ball_1)
            bag.add_ball(ball_2)
            
            bag.remove_specific_ball('red')
        

   

    if 'blue' in bag.bag_contents():
        results.append('blue')
    elif 'red' in bag.bag_contents():
        results.append('red')
                
print('blue: ', results.count('blue'))
print('red: ', results.count('red'))

    



