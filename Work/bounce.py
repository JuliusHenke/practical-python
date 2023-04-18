# bounce.py
#
# Exercise 1.5
ball_dropped_from_height = 100
ball_bounce_percentage = 3 / 5

ball_current_bounce_height = ball_dropped_from_height
for bounce in range(10):
    ball_current_bounce_height = ball_current_bounce_height * ball_bounce_percentage
    print(round(ball_current_bounce_height, 4))
