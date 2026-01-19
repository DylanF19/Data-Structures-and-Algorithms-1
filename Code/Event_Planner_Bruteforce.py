"""Event_Planner.py"""

#Brute Force
def event_planner_brute_force(file_name=None, input_details=None): # input details as [max time, max budget, event_list]
    import itertools
    import numpy
    #Starting variables
    if file_name is not None:
        max_time, max_budget, event_list = text_document_to_internal_array_translator(str(file_name))
    elif len(input_details) == 3:
        max_time, max_budget, event_list = input_details
    else:
        raise NameError("InputError: input details cannot be read")


    event_list_numerical = []
    for i, event in enumerate(event_list):
        index = [i+1]
        event_numerical = [index + event[2]]
        event_list_numerical += event_numerical


    #Starting variables
    event_combo_list = []
    event_combo_list += [[[0,0,0,0]]]
    number_of_events = len(event_list_numerical)
    #print("Length of event pool: ",number_of_events)

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
    # for l in range(1, max_length+1):
    for l in range(1, number_of_events+1):
        #print("At length ",l)
        for subset in itertools.combinations(event_list_numerical, l):
            if validset(subset) is True:
                event_combo_list += [subset]
    event_combo_list_length = len(event_combo_list)
    #print("List Created. Length: ", event_combo_list_length)

    # these lines create details for each subset such as total cost of time
    # and money as well as the total enjoyment value. The best combo is the
    # one with the highest total enjoyment score
    subset_details = []
    for i in range(0, event_combo_list_length):
        subset_details += [[i] + [numpy.sum(event_combo_list[i], axis=0, dtype=int).tolist()]]

    # Just in case there is a tie for the best score, the code is built
    # to handle multiple winners
    best_combo = []
    j = None
    for i in sorted(subset_details, key=lambda x: x[1][3], reverse=True):
        if i[1][3] == j or j is None:
            best_combo += [i]
            j = i[1][3]
        else:
            break

    # this converts the original solution(which was just numbers) in to a list
    # containing the names of the events
    def convert_numeric_solution_to_names(array, event_combo_list, event_list):
        combo = event_combo_list[array[0]]
        events = []
        details = [array[1][1:]]
        if combo[0][0] != 0:
            for i in combo:
                events += [event_list[i[0]-1][1]]
        else:
            events = [""]
        solution = [events + details]
        return solution

    best_list_with_names = []
    for subset in best_combo:
        best_list_with_names += convert_numeric_solution_to_names(subset, event_combo_list, event_list)

    #if len(best_list_with_names) == 1:
    #    print("1 solution found")
    #else:
    #    print(len(best_list_with_names),"solutions found.")
    return best_list_with_names


def text_document_to_internal_array_translator(file_name):

    import os 

    file_path = os.path.join(r"Input_Files",file_name)
    # print(f" :- File path: {file_path}")
    try:
        if os.path.exists(file_path):

            os.chmod(file_path, 0o666)
            # print(" :- File permissions modified successfully!")
            pass
        else:
            # print(" !! File not found:", file_path)
            pass
    except PermissionError:
        print(" !! Permission denied: You don't have the necessary permissions to change the permissions of this file.")

    with open(file_path, "r", encoding="utf-8") as file:
        event_index = int(file.readline())
        time_limit, money_limit = ((file.readline().strip("\n")).split(" "))
        time_limit = int(time_limit)
        money_limit = int(money_limit)
        ID_index = 1
        event_list_translated = []
        for x in file:
            event_name, time_value, money_value, enjoyment_value = x.strip("\n").split(" ")
            event_list_translated += [[[ID_index],[event_name],[int(time_value), int(money_value), int(enjoyment_value)]]]
            ID_index += 1

    # print(" :- File content accessed successfully!")

    return time_limit, money_limit, event_list_translated


#Name, Time, Cost, Fun_Value
Event_List_1 = [ 
    [[1],["Campus-Tour"],[2,20,50]],
    [[2],["Game-Night"],[3,80,120]],
    [[3],["Museum-Trip"],[4,100,150]],
    [[4],["Pizza-Workshop"],[2,60,100]],
    [[5],["Hiking"],[5,30,140]],
]

#Name, Time, Cost, Fun_Value
Event_List_2 = [
    [[1],["Welcome-BBQ"],[3,50,80]],
    [[2],["Karaoke-Night"],[2,40,70]],
    [[3],["Film-Screening"],[3,30,90]],
    [[4],["Sports-Tournament"],[4,60,110]],
    [[5],["Art-Workshop"],[2,70,95]],
    [[6],["Pub-Quiz"],[2,25,60]],
    [[7],["Bowling"],[3,80,100]],
    [[8],["Laser-Tag"],[2,90,130]],
    [[9],["Cooking-Class"],[3,75,105]],
    [[10],["Beach-Trip"],[6,120,180]],
    [[11],["Escape-Room"],[2,85,115]],
    [[12],["Open-Mic"],[2,20,50]]
]

#Name, Time, Cost, Fun_Value
Event_List_3 = [
    [[1],["Orientation-Walk"],[1,10,30]],
    [[2],["Ice-Breaker-Games"],[2,20,50]],
    [[3],["Movie-Marathon"],[5,60,140]],
    [[4],["City-Tour"],[4,80,120]],
    [[5],["Charity-Run"],[3,15,70]],
    [[6],["Trivia-Night"],[2,30,65]],
    [[7],["Wine-Tasting"],[2,100,150]],
    [[8],["Rock-Climbing"],[4,110,160]],
    [[9],["Theatre-Trip"],[4,90,130]],
    [[10],["Pottery-Class"],[3,85,125]],
    [[11],["Campus-Scavenger-Hunt"],[3,25,75]],
    [[12],["Photography-Walk"],[3,40,85]],
    [[13],["Poetry-Slam"],[2,20,55]],
    [[14],["Dance-Workshop"],[2,50,90]],
    [[15],["Baking-Competition"],[3,55,95]],
    [[16],["Outdoor-Cinema"],[4,70,115]],
    [[17],["Kayaking"],[5,130,190]],
    [[18],["Board-Game-Cafe"],[3,45,80]],
    [[19],["Comedy-Show"],[3,80,135]],
    [[20],["Volunteering-Event"],[4,10,60]],
    [[21],["Yoga-Session"],[2,35,70]],
    [[22],["Park-Picnic"],[3,30,65]],
    [[23],["Museum-Evening"],[3,75,110]],
    [[24],["Stargazing-Trip"],[4,50,100]],
    [[25],["Crafts-Fair"],[2,40,75]]
]
