# Testing suite for both algorithms
## Algorithm 1: Brute Force
### Test Results
#### scenario 1:  
##### Details
Max Time: 10 Hours  
Max Budget: 200 Pounds  
Size of Event Pool: 5  
Max Length:  5  
Valid Solution List Length:  22  
##### Results
Solution:
 [[['Game-Night', 3, 80, 120], 
	 ['Pizza-Workshop', 2, 60, 100], 
	 ['Hiking', 5, 30, 140]]]  
	 
Total Time Cost: 10 Hours  
Total Money Cost: 170 Pounds  
Total Enjoyment Score: 360 Enjoyment  
 
#### scenario 2:
##### Details
Max Time: 15 Hours  
Max Budget: 300 Pounds  
Size of Event Pool: 12  
Max Length:  8  
Valid Solution List Length:  1093  
##### Results
Solution:  
 [[['Film-Screening', 3, 30, 90], 
	 ['Sports-Tournament', 4, 60, 110], 
	 ['Art-Workshop', 2, 70, 95], 
	 ['Pub-Quiz', 2, 25, 60], 
	 ['Laser-Tag', 2, 90, 130], 
	 ['Open-Mic', 2, 20, 50]]]  
	 
Total Time Cost: 15 Hours  
Total Money Cost: 295 Pounds  
Total Enjoyment Score: 535 Enjoyment  

#### scenario 3:
##### Details
Max Time: 20 Hours  
Max Budget: 500 Pounds  
Size of Event Pool:  25  
Max Length:  16  
Valid Solution List Length:  454963  
##### Results
Solution:
['Trivia-Night'], 
		 ['Wine-Tasting'], 
		 ['Rock-Climbing'], 
		 ['Dance-Workshop'], 
		 ['Baking-Competition'], 
		 ['Comedy-Show'], 
		 ['Yoga-Session'], 
		 ['Crafts-Fair']  

Total Time Cost: 20 Hours  
Total Money Cost: 500 Pounds  
Total Enjoyment Score: 840 Enjoyment  

## Algorithm 2: Dynamic Tree Search

### Test Results

#### Scenario 1:

##### Details

Max Time: 10  
Max Budget: 200  
Size of Event Pool: 5  
Valid Solution List Length: 22  

##### Results

###### Solution: 
['Game-Night'], 
	['Pizza-Workshop'], 
	['Hiking']
				
Total Time Cost: 10 Hours  
Total Money Cost: 170 Pounds  
Total Enjoyment Score: 360 Enjoyment  

#### Scenario 2:

##### Details

Max Time: 15 
Max Budget: 300
Size of Event Pool: 12 
Valid Solution List Length: 1093 

##### Results

###### Solution:
['Film-Screening'],
	['Sports-Tournament'],
	['Art-Workshop'], 
	['Pub-Quiz'],
	['Laser-Tag'], 
	['Open-Mic']

Total Time Cost: 15 Hours  
Total Money Cost: 295 Pounds  
Total Enjoyment Score: 535 Enjoyment  

#### Scenario 3:

##### Details

Max Time: 20
Max Budget: 500
Size of Event Pool: 25
Valid Solution List Length: 454963 

##### Results

###### Solution 1: 
['Orientation-Walk'], 
	['Wine-Tasting'], 
	['Rock-Climbing'],
	['Pottery-Class'],
	['Campus-Scavenger-Hunt'],
	['Dance-Workshop'],
	['Comedy-Show'],
	['Crafts-Fair'], 

Total Time Cost: 20 Hours  
Total Money Cost: 500 Pounds  
Total Enjoyment Score: 840 Enjoyment  


###### Solution 2:
['Orientation-Walk'],
	['Wine-Tasting'],
	['Pottery-Class'],
	['Poetry-Slam'],
	['Dance-Workshop'],
	['Comedy-Show'],
	['Yoga-Session'],
	['Museum-Evening'],
	['Crafts-Fair']

Total Time Cost: 20 Hours  
Total Money Cost: 495 Pounds  
Total Enjoyment Score: 840 Enjoyment 


###### Solution 3:
['Trivia-Night'],
	['Wine-Tasting'],
	['Rock-Climbing'],
	['Dance-Workshop'],
	['Baking-Competition'],
	['Comedy-Show'],
	['Yoga-Session'],
	['Crafts-Fair']

Total Time Cost: 20 Hours  
Total Money Cost: 500 Pounds  
Total Enjoyment Score: 840 Enjoyment 





 ###### Dylan Foster - Author; Programmer
