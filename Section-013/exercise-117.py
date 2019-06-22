# List Exercises 5
# Using a nested <strong>list comprehension </strong>and range(), create a variable called <code>answer</code>&nbsp; with the following value - <code>[[0, 1, 2], [0, 1, 2], [0, 1, 2]]</code>&nbsp;.&nbsp; To break it down...start by using range and a list comp to generate the list [0,1,2].&nbsp; And then repeat that whole thing 3 times in a nested list comp.&nbsp; It's all a bit tricky to discuss, so maybe it's just best to look at the solution if you get stuck.&nbsp;&nbsp;</p></div>

answer = [[x for x in range(3)] for nums in range(3)]
