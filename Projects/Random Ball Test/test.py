import random

red = 13
blue = 20
total_balls = red+blue

while total_balls > 1 and red > 0 and blue >0:  
    ball_1 = random.choice(['red', 'blue'])
    ball_2 = random.choice(['red', 'blue'])
    if ball_1 == ball_2:
        blue -=1
    else:
        red -= 1
    total_balls = red + blue

    print(ball_1,ball_2)
    print(f'{blue} blue balls, {red} red balls')

