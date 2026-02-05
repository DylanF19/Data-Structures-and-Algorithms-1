# Data-Structures-and-Algorithms-1

To run algorithm 1:
paste this command into the command line, replacing `input` with the desired file. Note: file extentions are mandatory.
```
python -c "from Code.Event_Planner_Bruteforce_Both_Limits import event_planner_brute_force_both_limits; event_planner_brute_force_both_limits('input')"
```
or
```
python -c "from Code.Event_Planner_Bruteforce_Money import event_planner_brute_force_money_only; event_planner_brute_force_money_only('input')"
```
To run algorithm 2:
paste this command into the command line, replacing `input` with the desired file. Note: file extentions are mandatory.
```
python -c "from Code.Event_Planner_Dynamic_Both_Limits import event_planner_dynamic_search_both_limits; event_planner_dynamic_search_both_limits('input')"
```
or
```
python -c "from Code.Event_Planner_Dynamic_Money import event_planner_dynamic_search_money_only; event_planner_dynamic_search_money_only('input')"
```

## Algorithm 1: Brute Force Approach
This is a brute force approach to finding the best solution(s). I have had to optimize some parts so it can actually conclude execution in a reasonable amount of time. It is an intuative way of finding the solution. `input_large.txt` with only 25 events still took 6 minutes and 45 seconds to compute. This is mostly because this approach has an complexity of O(2^n) which gives it poor scalability. Clearly, a smarter approach is needed for large groups of events.

### `event_planner_brute_force():`

The brute force algorithm calculates the result through a few steps. First it uses the input to set the starting conditions in a form the function understands. Using those starting conditions, it uses the Itertools module to create every combination from the event list. If any of the generated combinations is valid, it is added to a list of valid combinations. Using that list, the algorith takes the combination with the largest enjoyment value and prints a readable result to the command line.

## Algorithm 2: Dynamic Search

The dynamic algorithm uses a clever method of calculating what the highest enjoyment could be and works backwards from that to deduce what the solution could be. This gives the algorithm a complexity of O(n*m*t) where n is the nuber of events, m is the max budget and t is the max time availible. This makes it much more efficient for larger values of n but does negligably make it slower than the brute force method for very low values of n.

### `event_planner_dynamic_search():`

Like the other algorithm, it first sets the starting variables from the input text file. It then creates a 3D grid that is (number of events)n by (max budget)m by (max time)t filled with zeros. 
```
26: data_field_3d = [[[0 for _ in range(max_budget + 1)] for _ in range(max_time + 1)] for _ in range(n+1)]
```
It then goes through a triple for loop, itterating through every cell in the 3D grid. The for loop also changes the value of the cells inside the grid depending on a few conditions. For each cell, it's coordinates of (n,m,t) are used to calculate what the max enjoyment is with these limits. For example, if the cell was at (2,50,4), it would find the highest enjoyment value that could be made with the first 2 events in the list, 50 max budget and 4 max time. Crucially, it uses the values of the cells above it to calculate the value by comparing that value to the sum of the considered event and the cell above that fits the event, selecting which ever is greater to fill the cell. 

At the end of it all, once it has itterated through every cell, it selects the the cell who's coordinates match the constraints of the given input, which will be in the lower corner of the grid.

With that value, being the greatest enjoyment that can be made from the constraints, it works backwards to deduce the sequence of events that could have resulted in the value given by the 3D grid. It finally prints the result to the command line in the same form as the brute force algorithm.

## Utilities

In programming, it's good practice not to repeat yourself. In the code there are functions that are used in both algorithms, such as reading input files or interpreting the input. They're stored in their own file and are imported in either algorithm. I'm not going to go too much into them because their names are pretty self explanitory and have plenty of comments. Just look at the code if you're so inclined.






 ###### Dylan Foster - Author; Programmer
