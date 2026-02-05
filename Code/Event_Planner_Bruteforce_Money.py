"""Event_Planner.py"""
#=====Imports=====
import itertools
import numpy
import time
try:
    from Utilities import function_port_money_only, array_to_readable_output_money_only
except ImportError:
    from Code.Utilities import function_port_money_only, array_to_readable_output_money_only
#======Code=======
def event_planner_brute_force_money_only(file_name=None, input_details=None, quiet=False):
    """
    This is the main engine of the brute force approach. It takes the lists of events
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

    start = time.perf_counter()
    # Sets the starting conditions.
    n, max_budget, event_list, name_list = function_port_money_only(file_name, input_details)

    def validset(subset):
        """
        A mini-function that sums the cost of a set and checks it against
        the max time and money availible. Returns True if a set is valid 
        and False otherwise 
        """
        set_sum = numpy.sum(subset, axis=0, dtype=int)
        if set_sum[1] <= max_budget:
            return True
        return False

    # This is the main engine that computes every legal permutaion of the events.
    # There can be hundreds of millions of permutations for a given event set
    # which was the main hurdle of doing this
    event_combo_list = []
    event_combo_list += [([0,0,0],)]
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
    subset_details = []
    for i in range(0, event_combo_list_length):
        info = numpy.sum(event_combo_list[i], axis=0, dtype=int).tolist()
        info.remove(info[0])
    subset_details += [[event_combo_list[i],info]]

    best_combo_numeric = max(subset_details, key=lambda x: x[1][1])

    # this converts the original solution(which was just numbers) in to a list
    # that can be used to print solution information.
    best_combo, details = array_to_readable_output_money_only(best_combo_numeric[0], name_list)
    
    end = time.perf_counter()
    #===============result================
    # The juicy, juicy results
    if quiet == False:
        print(" ======Brute Force======= \n")
        print(f"Input: {file_name}")
        print("\n ---------Solution-------- \n")
        for i in best_combo:
            print(f" - {i}")
        print("\n ----------Stats---------- \n")
        print(f"Money used:      {details[1]} Pounds")
        print(f"Total enjoyment: {details[2]} Enjoyment")
        print(f"Time to Compute: {end-start} Seconds")
        print("\n ======================== \n")

