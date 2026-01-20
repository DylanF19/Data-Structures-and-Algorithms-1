"""Event_Planner.py"""

def text_document_to_internal_array_translator(file_name):

    import os
    file_path = os.path.join(r"Input_Files",file_name)
    #print(f" :- File path: {file_path}")
    try:
        if os.path.exists(file_path):

            os.chmod(file_path, 0o666)
            #print(" :- File permissions modified successfully!")
            pass
        else:
            #print(" !! File not found:", file_path)
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
        name_list= []
        for x in file:
            event_name, time_value, money_value, enjoyment_value = x.strip("\n").split(" ")
            event_list_translated += [[ID_index, int(time_value), int(money_value), int(enjoyment_value)]]
            name_list += [event_name]
            ID_index += 1

    #print(" :- File content accessed successfully!")

    return time_limit, money_limit, event_list_translated, name_list

def function_port_brute(file_name=None, input_details=None):
    event_list = None
    name_list = None
    max_time = 0
    max_budget = 0

    if file_name is not None:
        max_time, max_budget, event_list, name_list = text_document_to_internal_array_translator(str(file_name))
    if input_details is not None and len(input_details) == 3:
        if input_details[0] is not None:
            max_time = input_details[0]
        if input_details[1] is not None:
            max_budget = input_details[1]
        if input_details[2] is not None:
            event_list = input_details[2]
    if file_name is None and input_details is None:
        raise NameError("Input cannot be interprteted")
    if event_list is None and file_name is None:
        raise NameError("Input cannot be interprteted")
    n = len(event_list)
    return n, max_time, max_budget, event_list, name_list

def array_to_readable_output(array, name_list):
    import numpy as np
    translated_list = []
    stats = 0
    stats = np.sum(array, axis=0).tolist()
    for i in array:
        translated_list += [name_list[i[0]-1]]
    return translated_list, stats

#Brute Force
def event_planner_brute_force(file_name=None, input_details=None, Quiet=False): # input details as [max time, max budget, event_list]
    import itertools
    import numpy
    import time
    start = time.perf_counter()

    n, max_time, max_budget, event_list, name_list = function_port_brute(file_name, input_details)


    #Starting variables
    event_combo_list = []
    event_combo_list += [[[0,0,0,0]]]


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
    for l in range(1, n+1):
        #print("At length ",l)
        for subset in itertools.combinations(event_list, l):
            if validset(subset) is True:
                event_combo_list += [subset]
    event_combo_list_length = len(event_combo_list)
    #print("List Created. Length: ", event_combo_list_length)

    # these lines create details for each subset such as total cost of time
    # and money as well as the total enjoyment value. The best combo is the
    # one with the highest total enjoyment score
    subset_details = [[[0],[0,0,0]]]
    for i in range(0, event_combo_list_length):
        sequence = []
        info = numpy.sum(event_combo_list[i], axis=0, dtype=int).tolist()
        info.remove(info[0])
    subset_details += [[event_combo_list[i],info]]

    best_combo_numeric = max(subset_details, key=lambda x: x[1][2])


    # this converts the original solution(which was just numbers) in to a list
    # containing the names of the events

    best_combo, details = array_to_readable_output(best_combo_numeric[0], name_list)
    
    end = time.perf_counter()
    #===============result================
    if Quiet == False:
        print(" ======Brute Force======= \n")
        print(" --------Solution-------- \n")
        for i in best_combo:
            print(f" - {i}")
        print("\n ----------Stats---------- \n")
        print(f"Time used:       {details[1]} Hours")
        print(f"Money used:      {details[2]} Pounds")
        print(f"Total enjoyment: {details[3]} Enjoyment")
        print(f"Time to Compute: {end-start} Seconds")
        print("\n ======================== \n")
