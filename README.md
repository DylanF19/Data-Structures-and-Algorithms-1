# Data-Structures-and-Algorithms-1

## Algorithm 1: Brute Force Approach
This is a brute force approach to finding the best solution(s). I have had to optimise some parts so it can actually conclude execution in a reasonable amount of time. The 3rd scenario still took 6 minutes and 45 seconds to compute. This is mostly because this approach has an complexity of O(2^n) which gives it poor scalability. Clearly, a smarter approach is needed for large groups of events.

### Results
#### scenario 1:  
Max Time: 10 Hours  
Max Budget: 200 Pounds  
Number of Events: 5  
Max Length:  5  
Valid Solution List Length:  21  

Events 1  
 [[['Game-Night', 3, 80, 120], ['Pizza-Workshop', 2, 60, 100], ['Hiking', 5, 30, 140]]]  
Total Time Cost: 10 Hours  
Total Money Cost: 170 Pounds  
Total Enjoyment Score: 360 Enjoyment  
 
#### scenario 2:
Max Time: 15 Hours  
Max Budget: 300 Pounds  
Number of Events: 12  
Max Length:  8  
Valid Solution List Length:  1092  

Events 2  
 [[['Film-Screening', 3, 30, 90], ['Sports-Tournament', 4, 60, 110], ['Art-Workshop', 2, 70, 95], ['Pub-Quiz', 2, 25, 60], ['Laser-Tag', 2, 90, 130], ['Open-Mic', 2, 20, 50]]]  
Total Time Cost: 15 Hours  
Total Money Cost: 295 Pounds  
Total Enjoyment Score: 535 Enjoyment  

#### scenario 3:
Max Time: 20 Hours  
Max Budget: 500 Pounds  
Length of event pool:  25  
Max Length:  16  
Valid Solution List Length:  454962  

Events 3  
 [[['Trivia-Night', 2, 30, 65], ['Wine-Tasting', 2, 100, 150], ['Rock-Climbing', 4, 110, 160], ['Dance-Workshop', 2, 50, 90], ['Baking-Competition', 3, 55, 95], ['Comedy-Show', 3, 80, 135], ['Yoga-Session', 2, 35, 70], ['Crafts-Fair', 2, 40, 75]]]  
Total Time Cost: 20 Hours  
Total Money Cost: 500 Pounds  
Total Enjoyment Score: 840 Enjoyment  

 ### Notes: Brute Force Approach
 The best solutions tend to use the most events in total with a bias towards events that use few time and money resources.

## Algorithm 2: ---Insert Name of Approach Here---

###Data
 ![./Analysis_Resources/DSA Tree Diagram](https://github.com/DylanF19/Data-Structures-and-Algorithms-1/blob/main/Analysis_Resources/DSA%20Tree%20Diagram.png)

 ##### Dylan Foster - Author; Programmer
