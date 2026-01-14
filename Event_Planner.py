"""Event_Planner.py"""
import itertools
import numpy
#Brute Force
def best_combo_for_highest_fun_score_brute_force(event_list, event_list_numerical, max_time, max_budget):
    """
    Docstring for best_combo_for_highest_fun_score
    
    :param Event_List: A brute force approach to finding the best combo of events
    """
    #Starting variables
    event_combo_list = []
    event_list_ordered_money = sorted(event_list_numerical, key=lambda x: x[2])
    event_list_ordered_time = sorted(event_list_numerical, key=lambda x: x[1])
    money_sum = 0
    time_sum = 0
    max_length = 0
    
    print("Length of event pool: ",len(event_list_numerical))

    # Initial optimiser:
    # It finds the greates length the solution could be and limits the length of permutations to that
    # for the sake of efficiency and computing speed
    while money_sum <= max_budget or time_sum <= max_time:
        money_sum += event_list_ordered_money[max_length][2]
        time_sum += event_list_ordered_time[max_length][1]
        max_length += 1
    print("Max Length: ",max_length)


    def validset(set):
        """
        Docstring for validset
        
        :Description: A mini-function that sums the cost of a set and checks it against
                      the max time and money availible. 
                      Returns True if a set is valid and False otherwise 
        """
        set_sum = numpy.sum(set, axis=0, dtype=int)
        if set_sum[1] <= max_time and set_sum[2] <= max_budget:
            return True
        return False

    # This is the main engine that computes every legal permutaion of the events.
    # It took a lot of pruning and optimising to get this to compute quickly.
    # There can be hundreds of millions of permutations for a given event set
    # which was the main hurdle of doing this
    for l in range(1, max_length - 1):
        for subset in itertools.combinations(event_list_numerical, l):
            if validset(subset) is True:
                event_combo_list += [subset]
    event_combo_list_length = len(event_combo_list)
    print("List Created. Length: ", event_combo_list_length)

    for i, subset in enumerate(event_combo_list):
        print(subset)
    print("--------------------------------------")    
    # these lines create details for each subset suchy as total cost of time
    # and money as well as the total enjoyment value. The best combo is the
    # one with the highest total enjoymenbt score
    subset_details = []
    for i in range(1, event_combo_list_length):
        subset_details += [numpy.sum(event_combo_list[i], axis=0, dtype=int)]

    for i, detail in enumerate(subset_details):
        print(detail)
    print("--------------------------------------")  
    best_score = max(subset_details, key=lambda x: x[3])

    best_combo_index = []
    for i, subset in enumerate(subset_details):
        if list(subset) == list(best_score):
            best_combo_index += [i+1]

    print("Best Combo Found at: ", best_combo_index)

    # Just in case there is a tie for the best score, the code is built
    # to handle multiple winners
    best_combo = []
    for i in best_combo_index:
        print(event_combo_list[i])
        best_combo += [event_combo_list[i]]

    # this converts the original solution(which was just numbers) in to a list
    # containing the names of the events
    best_list_with_names = []
    for i, subset in enumerate(best_combo):
        best_list_with_names_temp = []
        for subsubset in sorted(subset, key=lambda x: x[0]):
            best_list_with_names_temp += [event_list[subsubset[0]-1]]
        best_list_with_names += [best_list_with_names_temp]

    return best_list_with_names


#Name, Time, Cost, Fun_Value
Event_List_1 = [
    ["Campus-Tour", 2, 20, 50],
    ["Game-Night", 3, 80, 120],
    ["Museum-Trip", 4, 100, 150],
    ["Pizza-Workshop", 2, 60, 100],
    ["Hiking", 5, 30, 140]
]

#Name, Time, Cost, Fun_Value
Event_List_2 = [
    ["Welcome-BBQ", 3, 50, 80],
    ["Karaoke-Night", 2, 40, 70],
    ["Film-Screening", 3, 30, 90],
    ["Sports-Tournament", 4, 60, 110],
    ["Art-Workshop", 2, 70, 95],
    ["Pub-Quiz", 2, 25, 60],
    ["Bowling", 3, 80, 100],
    ["Laser-Tag", 2, 90, 130],
    ["Cooking-Class", 3, 75, 105],
    ["Beach-Trip", 6, 120, 180],
    ["Escape-Room", 2, 85, 115],
    ["Open-Mic", 2, 20, 50]
]

#Name, Time, Cost, Fun_Value
Event_List_3 = [
    ["Orientation-Walk", 1, 10, 30],  
    ["Ice-Breaker-Games", 2, 20, 50],
    ["Movie-Marathon", 5, 60, 140],
    ["City-Tour", 4, 80, 120],
    ["Charity-Run", 3, 15, 70],
    ["Trivia-Night", 2, 30, 65],
    ["Wine-Tasting", 2, 100, 150],
    ["Rock-Climbing", 4, 110, 160],
    ["Theatre-Trip", 4, 90, 130],
    ["Pottery-Class", 3, 85, 125],
    ["Campus-Scavenger-Hunt", 3, 25, 75],
    ["Photography-Walk", 3, 40, 85],
    ["Poetry-Slam", 2, 20, 55],
    ["Dance-Workshop", 2, 50, 90],
    ["Baking-Competition", 3, 55, 95],
    ["Outdoor-Cinema", 4, 70, 115],
    ["Kayaking", 5, 130, 190],
    ["Board-Game-Cafe", 3, 45, 80],
    ["Comedy-Show", 3, 80, 135],
    ["Volunteering-Event", 4, 10, 60],
    ["Yoga-Session", 2, 35, 70],
    ["Park-Picnic", 3, 30, 65],
    ["Museum-Evening", 3, 75, 110],
    ["Stargazing-Trip", 4, 50, 100],
    ["Crafts-Fair", 2, 40, 75]
]

# ID, Time, Money, Enjoyment
Event_List_1_Number = {
    (1, 2, 20, 50),
    (2, 3, 80, 120),
    (3, 4, 100, 150),
    (4, 2, 60, 100),
    (5, 5, 30, 140)
}

# ID, Time, Money, Enjoyment
Event_List_2_Number = {
    (1, 3, 50, 80),
    (2, 2, 40, 70),
    (3, 3, 30, 90),
    (4, 4, 60, 110),
    (5, 2, 70, 95),
    (6, 2, 25, 60),
    (7, 3, 80, 100),
    (8, 2, 90, 130),
    (9, 3, 75, 105),
    (10, 6, 120, 180),
    (11, 2, 85, 115),
    (12, 2, 20, 50)
}

# ID, Time, Money, Enjoyment
Event_List_3_Number = {
    (1, 1, 10, 30),
    (2, 2, 20, 50),
    (3, 5, 60, 140),
    (4, 4, 80, 120),
    (5, 3, 15, 70),
    (6, 2, 30, 65),
    (7, 2, 100, 150),
    (8, 4, 110, 160),
    (9, 4, 90, 130),
    (10, 3, 85, 125),
    (11, 3, 25, 75),
    (12, 3, 40, 85),
    (13, 2, 20, 55),
    (14, 2, 50, 90),
    (15, 3, 55, 95),
    (16, 4, 70, 115),
    (17, 5, 130, 190),
    (18, 3, 45, 80),
    (19, 3, 80, 135),
    (20, 4, 10, 60),
    (21, 2, 35, 70),
    (22, 3, 30, 65),
    (23, 3, 75, 110),
    (24, 4, 50, 100),
    (25, 2, 40, 75)
}

print("Events 1 \n",best_combo_for_highest_fun_score_brute_force(Event_List_1, Event_List_1_Number, 10, 200),"\n\n")

#print("Events 2 \n",best_combo_for_highest_fun_score_brute_force(Event_List_2, Event_List_2_Number, 15, 300),"\n\n")

#print("Events 3 \n",best_combo_for_highest_fun_score_brute_force(Event_List_3, Event_List_3_Number, 20, 500),"\n\n")
