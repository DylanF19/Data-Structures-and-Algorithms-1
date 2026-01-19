# Data-Structures-and-Algorithms-1

## Algorithm 1: Brute Force Approach
This is a brute force approach to finding the best solution(s). I have had to optimize some parts so it can actually conclude execution in a reasonable amount of time. The 3rd scenario still took 6 minutes and 45 seconds to compute. This is mostly because this approach has an complexity of O(2^n) which gives it poor scalability. Clearly, a smarter approach is needed for large groups of events.

 ### Notes: Brute Force Approach
 The best solutions tend to use the most events in total with a bias towards events that use few time and money resources.

## Algorithm 2: Dynamic Tree Search

### The Tree Graph

The diagram below was an invaluable tool in creating the methodology and putting the methods into code. The diagram outlines Valid combinations [Green], combinations at one or both resource limits [Yellow], invalid combinations [Red] resulting from going over one or both resource limits and simulated combinations [Grey] which give an idea of how the code optimizes to only search for valid combinations. A lot of time was dedicated to observing the graph, trying to find patterns in the data and finding ways of covering all points with a simple, recursive algorithm.
 ![./Analysis_Resources/DSA Tree Diagram]([https://github.com/DylanF19/Data-Structures-and-Algorithms-1/blob/main/Analysis_Resources/DSA%20Tree%20Diagram.png](https://github.com/DylanF19/Data-Structures-and-Algorithms-1/blob/main/Documents/Report_Resources/DSA%20Tree%20Diagram.png))

### The Method of the Algorithm

The algorithm that computes the solution or solutions is actually quite simple and merely follows basic rules. Every time the code loops, the "reader" goes down the tree. Which path the "reader" takes is dependent on the state of the selected node. In the graph can be:
 - valid |or| not valid
 - underbudget |or| not underbudget
 - end with the last event in the event list |or| not end with the last event in the event list
 - have a size of one |or| not have a size of one

Combinations of these attributes determine what the "reader" does and how it moves, no memory of previous states required.

### Key Functions of the Algorithm

The algorithm is built of a set of functions that act like measurers and tools.

#### `sum_of_two_arrays():` and `difference_of_two_arrays():`

These functions are very small and very simple but essential regardless. The way the value of a node is stored is through an array, making moving, reading and altering the value easy. The structure of the events are in the form: 
- `[[ID],[Name],[Time,Money,Enjoyment]]` 

while the value of the nodes are in the form:  
- `[[Set of IDs],[Set of Names],[[Time,Money,Enjoyment]]]`

For the use of these functions, only the 3rd part of the arrays are used, adding and subtracting from the details of the node, effectively calculating the valued of nodes below and above it. Also, `Numpy` is used for the math because it's fast and makes the function a single line. 
```
63: def sum_of_two_arrays(arr_1, arr_2):
64: 		return numpy.add(arr_1, arr_2).tolist()
65: 
66: 
67: def difference_of_two_arrays(arr_1, arr_2):
68: 		return numpy.subtract(arr_1, arr_2).tolist()
```

#### `go_down_a_level():`

As the name suggests, `go_down_a_level():` is the main function that allows the "reader" to move down the tree. It takes the current node, the list of events and the current node index, a number that is used to determine what the next value in the combination should be. It first creates a "branch" from the event list. This branch will always be an event after the final value in the node. For example, focusing only on the ID's for clarity, if the node was [1,2], node index would be 2+1 and so branch would be [3].

Next, the function splits apart the node into it's three subsets of its ID list, event list and total resource cost and enjoyment. For ID list and event list, it simply appends the next ID and event to the lists. For the resource cost and enjoyment, the function combines the arrays, making a new 3 by 1 array of the updated node details.

Finally, it puts the subsets together and back into a single array before returning the updated array.

```
71: def go_down_a_level(node, event_list, node_index):
72: 		branch = event_list[node_index-1]
73: 		temp_event_index = node[0]+branch[0]
74: 		temp_event_list = node[1]+branch[1]
75: 		temp_event_sum = sum_of_two_arrays(node[2],branch[2])
76: 		product_set = [temp_event_index,temp_event_list,temp_event_sum]
77: 		return  product_set
```

#### `go_up_a_level():`

As it turns out, going up a level in the tree is as simple as just doing the inverse of `go_down_a_level():`, just with a few alterations. At this point, with full traversal of the tree solved, it was only a matter of figuring out how to structure the logic to find every solution economically.

To go up a level, you just need to subtract the last added value from the node. An index is made from the final value in the given node and referenced against the event list to create `branch_inverse`. The final values in the ID and name lists are removed. The details in `branch_inverse` are subtracted from the original node details. The updated ID list, event list and details are put together again and returns the updated array.

```
80: def go_up_a_level(node, event_list):
81:     temp_event_index = node[0]
82:     temp_event_list = node[1]
83:     branch_inverse = event_list[temp_event_index[-1]-1]
84:     temp_event_list.pop(-1) # Remove last value
85:     temp_event_index.pop(-1)
86:     temp_event_sum = differenceofTwoArrays(node[2],branch_inverse[2])
87:     product_set = [temp_event_index,temp_event_list,temp_event_sum]
88:     return product_set
```

#### `is_valid():` and `is_under_budget:`

These two functions are very similar. I decided to break these functions into two functions to make manipulating the order of functions easier as the behavior of the "reader" is very much dependent of the values these functions give.

both compare the details of the node against the max resource values `max_time` and `max_budget` . `is_valid():` returns True if both the time and cost of a node is less than or equal to the max values and False otherwise. While, `is_under_budget:` does the same but only checks if the details are **strictly** less than the max values.

```
91: def is_valid(node, max_time, max_budget):
92:     if node[2][0] <= max_time and node[2][1] <= max_budget:
93:         return True
94:     return False
```
```
 97: def is_under_budget(node, max_time, max_budget):
 98:     if node[2][0] < max_time and node[2][1] < max_budget:
 99:         return True
100:     return False
```
#### `does_end_with_last_event():`

Short and simple. Reads last value of a node's ID list and if that matches the last value in the event list, it returns True, otherwise it returns False


```
103: def does_end_with_last_event(node, event_list):
104:     last_event = event_list[-1][0][0]
105:     node_end = node[0][-1]
106:     if node_end == last_event:
107:         return True
108:     return False
```

#### `is_length_one():`

I'm going to admit this is probably the most unnecessary function there is. It literally just returns True if the length is less than or equal to 1. I mostly did this for the sake of continuity and making it easier to move values around. 
```
111: def is_length_one(Node):
112:     if len(Node[0]) <= 1:
113:         return True
114:     return False
```
#### `event_planner_itterative_tree_search():`

This is the one, the main recursive function that ties everything together. It takes the event list, the max time and the max budget and returns a list of the best solutions, because there may be a first way tie.

First, it sets the initial values of variables and returns some key setup details. After that, it goes into a loop until it finds all possible solutions - *Technically it stops when it finds the last combination which can be known in advance. It's just a set of size one that contains only the last event.*

In each step/loop the function calculates the current node and determines if the node is:
 - Valid
 - Underbudget
 - Ends with last event
 - Has a length of one

After determining that, it goes into a set of conditionals. The values calculated previously determine the behavior and what the next node will be.

Off the bat, if the node is a valid combination, it adds the node to the list of all legal combinations. If also doesn't end with the last event, it sets the `node_index` to the value of the final number in the node's ID list + 1. If also not underbudget (i.e. if it's at one or both resource limits), the "reader" goes up a level in the tree, allowing the "reader" to go down the next branch next loop, never actually reading the previous node twice. So, it never backtracks, going to the next branch in one motion. Note that `copy.deepcopy()` is used rather than just `+= [node]`. This is required because the arrays are very complex and using such an array to add to another array by pointing to itself alters the value appended to the solution list, almost like the input is being corrupted. To fix that, a deep copy is added to the solution list, a separate array that can be added while keeping the structure of the array secure.

If the node failed the validity check and does not end with the last event, it sets the node index and goes up a level without adding the value to the solution list.

After the if-elif conditionals, the node is checked if it ends with the last event. If it does and length is greater than one, it goes up a level, the node index is set and then goes up another level. This was the key breakthrough for traveling through the tree without the use of memorization or memory. 

If the node does end with the final event and it's length is one, the code determines that it must be at the end of the tree and to sets a flag to True, exiting the while loop.

With the solution list constructed, all that's left to do is to select the combination or combinations that have the greatest enjoyment value and return them, which marks the end of the function.

```
117: def event_planner_itterative_tree_search(event_list, max_time, max_budget):
118: 
119:     print("==================Start====================")
120: 
121:     print("Max Time: ",max_time)
122:     print("Man Budget: ",max_budget)
123:     print("Size of Event Pool: ",len(event_list))
124: 
125:     legal_event_combinations = []
126:     node = [[],[],[0,0,0]]
127:     legal_event_combinations += [node]
128:     node_index = 1
129:     all_solutions_found = False
130: 
131:     while all_solutions_found is False:
132:         node = go_down_a_level(node, event_list, node_index)
133:         valid = is_valid(node, max_time, max_budget)
134:         under_budget = is_under_budget(node, max_time, max_budget)
135:         ends_with_last_event = does_end_with_last_event(node, event_list)
136:         length_is_one = is_length_one(node)
137: 
138: 
139:         if valid:
140:             legal_event_combinations.append(copy.deepcopy(node))
141:             if not ends_with_last_event:
142:                 node_index = node[0][-1]+1
143:                 if not under_budget:
144:                     node = go_up_a_level(node, event_list)
145: 
146:         elif not ends_with_last_event:
147:             node_index = node[0][-1]+1
148:             node = go_up_a_level(node, event_list)
149: 
150:         if ends_with_last_event:
151:             if not length_is_one:
152:                 node = go_up_a_level(node, event_list)
153:                 node_index = node[0][-1]+1
154:                 node = go_up_a_level(node, event_list)
155:              else: # if lengthIsOne is True {and endsWithLastEvent is True}
156:                 all_solutions_found = True
157:         # To fail: must be not Valid, end with last event and not end with last event
158: 
159:     print("Length of solution list: ",len(legal_event_combinations))
160: 
161: 
162:     best_combo = []
163:     j = None
164:     for i in sorted(legal_event_combinations, key=lambda x: x[2][2], reverse=True):
165:         if i[2][2] == j or j is None:
166:             best_combo += [i]
167:             j = i[2][2]
168:         else:
169:             break
170:     print("===================End=====================")
171:     return best_combo
```





 ###### Dylan Foster - Author; Programmer
