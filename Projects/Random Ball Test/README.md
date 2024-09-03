# Random Ball Test
 This was a question on an I.Q. tests page. I wanted to write a program that would give me the answer, using an object pool for the first time.

## Question -
 The question was:
 You have 20 blue balls and 13 red balls.
 Randomly remove 2 balls, then do the following:
 - If they are the same color, replace them with a blue ball
 - If they are different colors, replace them with a red ball
 Repeat until only 1 ball remains.
 What is the color of that ball?

## Thoughts
 At first I just wanted to solve the problem programmatically, learning about object pools along the way. 
 In the middle of it, I started getting infinite loops, where there were multiple red balls still in the bag, but no blue balls to replace them with.
 That lead to me realizing that the player could randomly pull multiple of the same color sets, depleeting the blue ball population, leaving only reds.