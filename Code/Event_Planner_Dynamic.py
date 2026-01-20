#=====Imports=====
import time
import numpy as np
import os
#======Code=======
def function_port_dynamic(file_name=None, input_details=None):
    """
    This is utility function, used to set the initial conditions of the the main function
    
    :param file_name: The desired input file
    :param input_details: An array of details that can be 
                          used to overwrite the pre-existing
                          file values. Usefull for debugging
    """
    # Default values set for  the sake of redundancy
    event_list = None
    name_list = None
    max_time = 0
    max_budget = 0

    # a tree of conditionals to set the starting conditions, allowing for some
    # customisability, useful for testing and debugging.
    #
    # if a given parameter is set to something other than None, it overwrites the initial state
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

def event_planner_dynamic_search(file_name=None, input_details=None, quiet=0):
    """
    This is the main engine of the dynamic approach. It takes the lists of events
    and parameters and prints the solution. Note: does not return a result, printing
    directly to the command line.
    
    :param file_name: The desired input file
    :param input_details: An array of details that can be 
                          used to overwrite the pre-existing
                          file values. Usefull for debugging
    :param quiet: Controls the verbosity of the function
                  (whether it outputs details regarding 
                  the solution or not)
    """

    # Starts timer
    start = time.perf_counter()
    # Gets the starting conditions and event set
    n, max_time, max_budget, event_list, name_list = function_port_dynamic(file_name, input_details)
    # Creates the nunber_of_events(n) by max_time(t) by max_budget(b) 3D grid filled with 0s.
    data_field_3d = [[[0 for _ in range(max_budget + 1)] for _ in range(max_time + 1)] for _ in range(n+1)]

    for i in range(n+1):
        #print(i)
        for t in range(max_time+1):

            for m in range(max_budget+1):

                if i == 0 or t == 0 or m == 0:

                    data_field_3d[i][t][m] = 0

                elif event_list[i-1][1] <= t and event_list[i-1][2] <= m:

                    data_field_3d[i][t][m] = max(
                        data_field_3d[i-1][t][m],
                        event_list[i-1][3] + data_field_3d[i-1][t-event_list[i-1][1]][m-event_list[i-1][2]]
                        )

                else:

                    data_field_3d[i][t][m] = data_field_3d[i-1][t][m]


    i = n
    j = max_time
    k = max_budget
    solution = []
    while i > 0 and j > 0 and k > 0:
        if data_field_3d[i][j][k] != data_field_3d[i-1][j][k]:
            solution += [event_list[i-1]]
            j = j - event_list[i-1][1]
            k = k - event_list[i-1][2]
        i -= 1

    solution_sorted = sorted(solution, key=lambda x: x[0])

    best_combo, details = array_to_readable_output(solution_sorted, name_list)

    end = time.perf_counter()
    #===============result================
    if quiet == False:
        print(" =========Dynamic========= \n")
        print(" ---------Solution-------- \n")
        for i in best_combo:
            print(f" - {i}")
        print("\n ----------Stats---------- \n")
        print(f"Time used:       {details[1]} Hours")
        print(f"Money used:      {details[2]} Pounds")
        print(f"Total enjoyment: {details[3]} Enjoyment")
        print(f"Time to Compute: {end-start} Seconds")
        print("\n ======================== \n")




def array_to_readable_output(array, name_list):
    """
    Converts the internal solution array into a form that can be
    reduced to the names of the events ad its details.
    
    :param array: internal array(only consists of numbers)
    :param name_list: the ordered list of event names for lookup
    """
    translated_list = []
    stats = 0
    stats = np.sum(array, axis=0).tolist()
    for i in array:
        translated_list += [name_list[i[0]-1]]
    return translated_list, stats


def text_document_to_internal_array_translator(file_name):
    """
    This finds the text file, reads it and converts the contents of that
    file into it's key data and arrays.
    
    :param file_name: The desired input file
    """
    file_path = os.path.join(r"Input_Files",file_name)
    #print(f" :- File path: {file_path}")
    try:
        if os.path.exists(file_path):

            os.chmod(file_path, 0o666)
            #print(" :- File permissions modified successfully!")
        else:
            print(" !! File not found:", file_path)
    except PermissionError:
        print(" !! Permission denied: You don't have the necessary permissions to change the permissions of this file.")

    with open(file_path, "r", encoding="utf-8") as file:
        event_index = int(file.readline())
        time_limit, money_limit = ((file.readline().strip("\n")).split(" "))
        time_limit = int(time_limit)
        money_limit = int(money_limit)
        id_index = 1
        event_list_translated = []
        name_list= []
        for x in file:
            event_name, time_value, money_value, enjoyment_value = x.strip("\n").split(" ")
            event_list_translated += [[id_index, int(time_value), int(money_value), int(enjoyment_value)]]
            name_list += [event_name]
            id_index += 1

    #print(" :- File content accessed successfully!")

    return time_limit, money_limit, event_list_translated, name_list
